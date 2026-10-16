"""Registreeri mudelid Django haldusliideses ning vali nimekirja veerud ja olekufilter."""
from django.contrib import admin
from .models import Subject, Task

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ["name", "owner"]

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["title", "subject", "due_at", "completed"]
    list_filter = ["completed"]
