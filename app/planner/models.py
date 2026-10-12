from django.conf import settings
from django.db import models
from django.utils import timezone


class Subject(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="subjects")
    name = models.CharField("Õppeaine", max_length=100)
    color = models.CharField("Värv", max_length=7, default="#8b82f6")

    class Meta:
        ordering = ["name", "id"]
        constraints = [models.UniqueConstraint(fields=["owner", "name"], name="unique_owner_subject")]

    def __str__(self):
        return self.name


class Task(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT, related_name="tasks", verbose_name="Õppeaine")
    title = models.CharField("Pealkiri", max_length=200)
    description = models.TextField("Kirjeldus", blank=True)
    due_at = models.DateTimeField("Tähtaeg")
    completed = models.BooleanField("Tehtud", default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["due_at", "id"]
        indexes = [models.Index(fields=["subject", "completed", "due_at"], name="task_subject_status_due")]

    @property
    def is_overdue(self):
        return not self.completed and self.due_at < timezone.now()

    def __str__(self):
        return self.title
