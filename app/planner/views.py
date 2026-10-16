# Faili eesmärk: töödelda brauseri päringuid, valida kasutaja andmed ja koostada kuvatavad lehed.

from datetime import timedelta
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.decorators.http import require_POST
from .forms import RegisterForm, SubjectForm, TaskForm
from .models import Subject, Task


# GET kuvab registreerimisvormi; korrektne POST loob konto ja avab kasutajale sessiooni.
def register(request):
    # request kirjeldab saabunud päringut; user on sessiooni järgi tuvastatud kasutaja.
    if request.user.is_authenticated:
        # redirect saadab brauseri nimelisele aadressile uue GET-päringuga.
        # Nii ei saada lehe värskendamine sama salvestusvormi uuesti.
        return redirect("dashboard")
    # POST-andmed seotakse vormiga; GET-päringul jääb vorm täitmata.
    form = RegisterForm(request.POST or None)
    # Andmebaasi kirjutame alles pärast väljade ja paroolide kontrolli.
    if request.method == "POST" and form.is_valid():
        # save loob andmebaasi uue kasutaja ja tagastab tema objekti.
        user = form.save()
        # Seo kasutaja praeguse sessiooniga, et järgmised päringud tunneksid ta ära.
        login(request, user)
        messages.success(request, "Konto on loodud. Lisa oma esimene õppeaine!")
        # redirect saadab brauseri nimelisele aadressile uue GET-päringuga.
        # Nii ei saada lehe värskendamine sama salvestusvormi uuesti.
        return redirect("dashboard")
    return render(request, "registration/register.html", {"form": form})


# Dekoraator lisab funktsioonile kontrolli: sisse logimata kasutaja suunatakse sisselogimisele.
@login_required
# Koosta töölaud: kokkuvõtted, filtrid, otsing ja üks lehekülg ülesandeid.
def dashboard(request):
    # Praegune ajahetk sobib tähtaegade võrdlemiseks.
    now = timezone.now()
    # Kohalik kuupäev kasutab rakenduse ajavööndit, mitte tingimata UTC kuupäeva.
    today = timezone.localdate()
    # Omanikufilter välistab võõrad tööd; select_related toob aine sama SQL-päringuga.
    tasks = Task.objects.filter(subject__owner=request.user).select_related("subject")
    # Arvuta kõik neli loendurit enne nimekirja filtreerimist ühe koondpäringuga.
    counts = tasks.aggregate(
        # Count loendab kirjeid; Q kirjeldab tingimust, millised tööd loendurisse lähevad.
        pending=Count("id", filter=Q(completed=False)),
        overdue=Count("id", filter=Q(completed=False, due_at__lt=now)),
        today=Count("id", filter=Q(completed=False, due_at__date=today)),
        done=Count("id", filter=Q(completed=True)),
    )
    # GET-parameetrid pärinevad aadressiribalt; tundmatu olek asendatakse vaikevalikuga.
    status = request.GET.get("status", "pending")
    if status not in {"pending", "done", "all", "overdue", "today"}:
        status = "pending"
    if status == "pending":
        # filter kitsendab andmebaasipäringut. False jätab alles tegemata tööd.
        tasks = tasks.filter(completed=False)
    elif status == "done":
        # True jätab alles lõpetatud tööd.
        tasks = tasks.filter(completed=True)
    elif status == "overdue":
        # Topeltalakriipsuga lt tähendab väiksem kui: tähtaeg on praegusest ajast varasem.
        tasks = tasks.filter(completed=False, due_at__lt=now)
    elif status == "today":
        tasks = tasks.filter(completed=False, due_at__date=today)
    subject = request.GET.get("subject", "")
    # Aine ID-d kasutame ainult numbrina; omaniku piirang jääb päringule alles.
    if subject.isdecimal():
        # int teisendab aadressilt saadud teksti täisarvuks, mis vastab aine ID-le.
        tasks = tasks.filter(subject_id=int(subject))
    else:
        subject = ""
    search = request.GET.get("q", "").strip()
    # Q ühendab tingimused VÕI-tehtega; icontains otsib teksti tõstutundetult.
    if search:
        tasks = tasks.filter(Q(title__icontains=search) | Q(description__icontains=search))
    from django.core.paginator import Paginator
    # Näita kuni 25 tööd; get_page käsitleb ka vigaseid ja puuduvaid lehenumbreid.
    page = Paginator(tasks, 25).get_page(request.GET.get("page"))
    # GET-parameetrite originaal on muutmatu; copy annab redigeeritava koopia.
    query = request.GET.copy()
    # Eemalda vana lehenumber, et järgmise lehe lingil säiliksid ülejäänud filtrid.
    query.pop("page", None)
    subjects = Subject.objects.filter(owner=request.user).annotate(pending_count=Count("tasks", filter=Q(tasks__completed=False)))
    return render(request, "planner/dashboard.html", {
        "page": page, "subjects": subjects, "counts": counts,
        "selected_status": status, "selected_subject": subject, "search": search,
        "today": today, "pagination_query": query.urlencode(),
        "next_task": Task.objects.filter(subject__owner=request.user, completed=False, due_at__gte=now).select_related("subject").first(),
    })


# Dekoraator lisab funktsioonile kontrolli: sisse logimata kasutaja suunatakse sisselogimisele.
@login_required
# Kuva kasutaja ained ning salvesta kontrollitud vormiga uus aine.
def subjects(request):
    form = SubjectForm(request.POST or None, owner=request.user)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Õppeaine on lisatud.")
        return redirect("subjects")
    return render(request, "planner/subjects.html", {"form": form, "subjects": Subject.objects.filter(owner=request.user).annotate(task_count=Count("tasks"))})


# Dekoraator lisab funktsioonile kontrolli: sisse logimata kasutaja suunatakse sisselogimisele.
@login_required
# Sama vaade lisab uue töö või muudab pk järgi olemasolevat tööd.
def task_form(request, pk=None):
    # Võõra või puuduva töö korral tagastame 404; loomisel on instance tühi.
    task = get_object_or_404(Task, pk=pk, subject__owner=request.user) if pk is not None else None
    if not Subject.objects.filter(owner=request.user).exists():
        messages.info(request, "Lisa enne ülesannet vähemalt üks õppeaine.")
        return redirect("subjects")
    # instance seob vormi olemasoleva tööga; None korral loob save uue töö.
    form = TaskForm(request.POST or None, owner=request.user, instance=task)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Ülesanne on uuendatud." if task else "Ülesanne on lisatud.")
        # redirect saadab brauseri nimelisele aadressile uue GET-päringuga.
        # Nii ei saada lehe värskendamine sama salvestusvormi uuesti.
        return redirect("dashboard")
    return render(request, "planner/task_form.html", {"form": form, "task": task})


# Dekoraator lisab funktsioonile kontrolli: sisse logimata kasutaja suunatakse sisselogimisele.
@login_required
@require_POST
# Sisselogimine ja require_POST lubavad olekut muuta ainult POST-päringuga.
def task_toggle(request, pk):
    task = get_object_or_404(Task, pk=pk, subject__owner=request.user)
    # Määrame soovitud oleku, et topeltsaatmine ei pööraks tulemust tagasi.
    desired = request.POST.get("completed")
    if desired not in {"0", "1"}:
        from django.http import HttpResponseBadRequest
        return HttpResponseBadRequest("Vigane olek")
    # Võrdlus annab True või False: tekst 1 märgib töö tehtuks, tekst 0 tegemata.
    task.completed = desired == "1"
    # Salvesta ainult olekuväli; teised ülesande andmed jäävad puutumata.
    task.save(update_fields=["completed"])
    messages.success(request, "Ülesanne on tehtud." if task.completed else "Ülesanne on taas tegemata.")
    status = request.POST.get("return_status", "pending")
    if status not in {"pending", "done", "all", "overdue", "today"}:
        status = "pending"
    from django.urls import reverse
    return redirect(f"{reverse('dashboard')}?status={status}")


# Dekoraator lisab funktsioonile kontrolli: sisse logimata kasutaja suunatakse sisselogimisele.
@login_required
# GET näitab kinnitust, POST kustutab ainult praegusele kasutajale kuuluva töö.
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, subject__owner=request.user)
    # Andmeid muutev tegevus toimub vormi saatmisel; GET ainult kuvab kinnitust.
    if request.method == "POST":
        # Eemalda kinnitatud ja omaniku järgi kontrollitud ülesanne andmebaasist.
        task.delete()
        messages.success(request, "Ülesanne on kustutatud.")
        # redirect saadab brauseri nimelisele aadressile uue GET-päringuga.
        # Nii ei saada lehe värskendamine sama salvestusvormi uuesti.
        return redirect("dashboard")
    return render(request, "planner/task_delete.html", {"task": task})


# Dekoraator lisab funktsioonile kontrolli: sisse logimata kasutaja suunatakse sisselogimisele.
@login_required
# Jaota valitud nädala ülesanded seitsmesse kohaliku kuupäeva lahtrisse.
def calendar(request):
    # Kohalik kuupäev kasutab rakenduse ajavööndit, mitte tingimata UTC kuupäeva.
    today = timezone.localdate()
    try:
        from datetime import date
        chosen = date.fromisoformat(request.GET.get("week", today.isoformat()))
    # Vigase kuupäeva korral jätkame tänase päevaga, selle asemel et kuvada serveriviga.
    except (ValueError, TypeError):
        chosen = today
    # weekday annab esmaspäeval 0; lahutamine leiab valitud nädala esmaspäeva.
    monday = chosen - timedelta(days=chosen.weekday())
    # Piiritle päevad ajatempliga, et indeks oleks päringus kasutatav.
    from datetime import datetime, time
    # Muuda esmaspäeva südaöö ajavööndiga ajatempliks.
    start = timezone.make_aware(datetime.combine(monday, time.min))
    # Nädalavahemiku algus on kaasatud ja järgmise esmaspäeva algus välistatud.
    end = start + timedelta(days=7)
    tasks = Task.objects.filter(subject__owner=request.user, due_at__gte=start, due_at__lt=end).select_related("subject")
    # Loendikomprehensioon loob seitse sõnastikku. range(7) annab arvud 0 kuni 6.
    # Iga päev saab oma kuupäeva ja esialgu tühja ülesannete loendi.
    days = [{"date": monday + timedelta(days=i), "tasks": []} for i in range(7)]
    # Päevade vahe annab lahtri indeksi 0–6; teisenda tähtaeg esmalt Eesti aega.
    for task in tasks:
        days[(timezone.localtime(task.due_at).date() - monday).days]["tasks"].append(task)
    return render(request, "planner/calendar.html", {
        "days": days, "monday": monday, "sunday": monday + timedelta(days=6),
        "previous": (monday - timedelta(days=7)).isoformat(),
        "next": (monday + timedelta(days=7)).isoformat(), "today": today,
    })
