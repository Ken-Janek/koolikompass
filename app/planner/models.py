# Faili eesmärk: kirjeldada õppeainete ja ülesannete andmeid, seoseid ning andmebaasireegleid.

from django.conf import settings
from django.db import models
from django.utils import timezone


# Õppeaine kuulub ühele kasutajale ja koondab tema ülesandeid.
# Pärimine: models.Model annab klassile salvestamise ja päringute tegemise võimalused.
# Django loob mudeli põhjal tabeli; iga Subject-objekt vastab ühele ainekirjele.
class Subject(models.Model):
    # CASCADE eemaldab kasutaja kustutamisel tema ained, kui seotud tööde kaitse seda lubab.
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="subjects")
    # CharField hoiab lühikest teksti. max_length piirab aine nime 100 märgini.
    name = models.CharField("Õppeaine", max_length=100)
    # Värv salvestub tekstina, näiteks #8b82f6; default valitakse, kui väärtust ei anta.
    color = models.CharField("Värv", max_length=7, default="#8b82f6")

    # Meta sisaldab Django mudeli lisareegleid, mitte kasutaja sisestatavaid andmeid.
    class Meta:
        ordering = ["name", "id"]
        # Andmebaas keelab samal kasutajal kaks täpselt sama nimega ainet.
        constraints = [models.UniqueConstraint(fields=["owner", "name"], name="unique_owner_subject")]

    # self viitab praegusele objektile. __str__ määrab selle loetava tekstikuju,
    # näiteks haldusliideses ja vormi valikumenüüs.
    def __str__(self):
        return self.name


# Ülesande omanik leitakse seose task.subject.owner kaudu.
class Task(models.Model):
    # PROTECT takistab aine kustutamist, kuni sellega on seotud ülesandeid.
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT, related_name="tasks", verbose_name="Õppeaine")
    title = models.CharField("Pealkiri", max_length=200)
    # TextField sobib pikemale tekstile; blank=True lubab vormis kirjelduse tühjaks jätta.
    description = models.TextField("Kirjeldus", blank=True)
    # DateTimeField salvestab nii kuupäeva kui ka kellaaja.
    due_at = models.DateTimeField("Tähtaeg")
    # BooleanField hoiab tõeväärtust: True tähendab tehtud, False tegemata.
    completed = models.BooleanField("Tehtud", default=False)
    # Loomisaeg täidetakse automaatselt ainult kirje esimesel salvestamisel.
    created_at = models.DateTimeField(auto_now_add=True)

    # Meta sisaldab Django mudeli lisareegleid, mitte kasutaja sisestatavaid andmeid.
    class Meta:
        # Lähim tähtaeg tuleb esimesena; ID teeb võrdsete tähtaegade järjekorra püsivaks.
        ordering = ["due_at", "id"]
        # Liitindeks toetab aine, oleku ja tähtaja järgi tehtavaid päringuid.
        indexes = [models.Index(fields=["subject", "completed", "due_at"], name="task_subject_status_due")]

    @property
    # Arvutatud omadust kasutatakse mallis; see ei ole eraldi andmebaasiveerg.
    def is_overdue(self):
        # and nõuab mõlema tingimuse täitumist: töö on tegemata ja tähtaeg on möödunud.
        return not self.completed and self.due_at < timezone.now()

    # self viitab praegusele objektile. __str__ määrab selle loetava tekstikuju,
    # näiteks haldusliideses ja vormi valikumenüüs.
    def __str__(self):
        return self.title
