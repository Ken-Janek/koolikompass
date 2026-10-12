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


def register(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    form = RegisterForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, "Konto on loodud. Lisa oma esimene õppeaine!")
        return redirect("dashboard")
    return render(request, "registration/register.html", {"form": form})


@login_required
def dashboard(request):
    now = timezone.now()
    today = timezone.localdate()
    tasks = Task.objects.filter(subject__owner=request.user).select_related("subject")
    counts = tasks.aggregate(
        pending=Count("id", filter=Q(completed=False)),
        overdue=Count("id", filter=Q(completed=False, due_at__lt=now)),
        today=Count("id", filter=Q(completed=False, due_at__date=today)),
        done=Count("id", filter=Q(completed=True)),
    )
    status = request.GET.get("status", "pending")
    if status not in {"pending", "done", "all", "overdue", "today"}:
        status = "pending"
    if status == "pending":
        tasks = tasks.filter(completed=False)
    elif status == "done":
        tasks = tasks.filter(completed=True)
    elif status == "overdue":
        tasks = tasks.filter(completed=False, due_at__lt=now)
    elif status == "today":
        tasks = tasks.filter(completed=False, due_at__date=today)
    subject = request.GET.get("subject", "")
    if subject.isdecimal():
        tasks = tasks.filter(subject_id=int(subject))
    else:
        subject = ""
    search = request.GET.get("q", "").strip()
    if search:
        tasks = tasks.filter(Q(title__icontains=search) | Q(description__icontains=search))
    from django.core.paginator import Paginator
    page = Paginator(tasks, 25).get_page(request.GET.get("page"))
    query = request.GET.copy()
    query.pop("page", None)
    subjects = Subject.objects.filter(owner=request.user).annotate(pending_count=Count("tasks", filter=Q(tasks__completed=False)))
    return render(request, "planner/dashboard.html", {
        "page": page, "subjects": subjects, "counts": counts,
        "selected_status": status, "selected_subject": subject, "search": search,
        "today": today, "pagination_query": query.urlencode(),
        "next_task": Task.objects.filter(subject__owner=request.user, completed=False, due_at__gte=now).select_related("subject").first(),
    })


@login_required
def subjects(request):
    form = SubjectForm(request.POST or None, owner=request.user)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Õppeaine on lisatud.")
        return redirect("subjects")
    return render(request, "planner/subjects.html", {"form": form, "subjects": Subject.objects.filter(owner=request.user).annotate(task_count=Count("tasks"))})


@login_required
def task_form(request, pk=None):
    task = get_object_or_404(Task, pk=pk, subject__owner=request.user) if pk is not None else None
    if not Subject.objects.filter(owner=request.user).exists():
        messages.info(request, "Lisa enne ülesannet vähemalt üks õppeaine.")
        return redirect("subjects")
    form = TaskForm(request.POST or None, owner=request.user, instance=task)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Ülesanne on uuendatud." if task else "Ülesanne on lisatud.")
        return redirect("dashboard")
    return render(request, "planner/task_form.html", {"form": form, "task": task})


@login_required
@require_POST
def task_toggle(request, pk):
    task = get_object_or_404(Task, pk=pk, subject__owner=request.user)
    # Määrame soovitud oleku, et topeltsaatmine ei pööraks tulemust tagasi.
    desired = request.POST.get("completed")
    if desired not in {"0", "1"}:
        from django.http import HttpResponseBadRequest
        return HttpResponseBadRequest("Vigane olek")
    task.completed = desired == "1"
    task.save(update_fields=["completed"])
    messages.success(request, "Ülesanne on tehtud." if task.completed else "Ülesanne on taas tegemata.")
    status = request.POST.get("return_status", "pending")
    if status not in {"pending", "done", "all", "overdue", "today"}:
        status = "pending"
    from django.urls import reverse
    return redirect(f"{reverse('dashboard')}?status={status}")


@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, subject__owner=request.user)
    if request.method == "POST":
        task.delete()
        messages.success(request, "Ülesanne on kustutatud.")
        return redirect("dashboard")
    return render(request, "planner/task_delete.html", {"task": task})


@login_required
def calendar(request):
    today = timezone.localdate()
    try:
        from datetime import date
        chosen = date.fromisoformat(request.GET.get("week", today.isoformat()))
    except (ValueError, TypeError):
        chosen = today
    monday = chosen - timedelta(days=chosen.weekday())
    # Piiritle päevad ajatempliga, et indeks oleks päringus kasutatav.
    from datetime import datetime, time
    start = timezone.make_aware(datetime.combine(monday, time.min))
    end = start + timedelta(days=7)
    tasks = Task.objects.filter(subject__owner=request.user, due_at__gte=start, due_at__lt=end).select_related("subject")
    days = [{"date": monday + timedelta(days=i), "tasks": []} for i in range(7)]
    for task in tasks:
        days[(timezone.localtime(task.due_at).date() - monday).days]["tasks"].append(task)
    return render(request, "planner/calendar.html", {
        "days": days, "monday": monday, "sunday": monday + timedelta(days=6),
        "previous": (monday - timedelta(days=7)).isoformat(),
        "next": (monday + timedelta(days=7)).isoformat(), "today": today,
    })
