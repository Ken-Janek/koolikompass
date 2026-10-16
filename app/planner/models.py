"""Andmemudel: kasutaja → õppeained → ülesanded. Django loob tabelid migratsioonidega."""
from django.conf import settings
from django.db import models
from django.utils import timezone


# Õppeaine kuulub ühele kasutajale ja koondab tema ülesandeid.
class Subject(models.Model):
    # CASCADE eemaldab kasutaja kustutamisel tema ained, kui seotud tööde kaitse seda lubab.
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="subjects")
    name = models.CharField("Õppeaine", max_length=100)
    color = models.CharField("Värv", max_length=7, default="#8b82f6")

    class Meta:
        ordering = ["name", "id"]
        # Andmebaas keelab samal kasutajal kaks täpselt sama nimega ainet.
        constraints = [models.UniqueConstraint(fields=["owner", "name"], name="unique_owner_subject")]

    def __str__(self):
        return self.name


# Ülesande omanik leitakse seose task.subject.owner kaudu.
class Task(models.Model):
    # PROTECT takistab aine kustutamist, kuni sellega on seotud ülesandeid.
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT, related_name="tasks", verbose_name="Õppeaine")
    title = models.CharField("Pealkiri", max_length=200)
    description = models.TextField("Kirjeldus", blank=True)
    due_at = models.DateTimeField("Tähtaeg")
    completed = models.BooleanField("Tehtud", default=False)
    # Loomisaeg täidetakse automaatselt ainult kirje esimesel salvestamisel.
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Lähim tähtaeg tuleb esimesena; ID teeb võrdsete tähtaegade järjekorra püsivaks.
        ordering = ["due_at", "id"]
        # Liitindeks toetab aine, oleku ja tähtaja järgi tehtavaid päringuid.
        indexes = [models.Index(fields=["subject", "completed", "due_at"], name="task_subject_status_due")]

    @property
    # Arvutatud omadust kasutatakse mallis; see ei ole eraldi andmebaasiveerg.
    def is_overdue(self):
        return not self.completed and self.due_at < timezone.now()

    def __str__(self):
        return self.title
