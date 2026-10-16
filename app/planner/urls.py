"""Seo aadressid vaadetega. name võimaldab viidata marsruudile ilma aadressi kordamata; pk on kirje ID."""
from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("konto/registreeru/", views.register, name="register"),
    path("ained/", views.subjects, name="subjects"),
    path("ulesanded/lisa/", views.task_form, name="task_create"),
    path("ulesanded/<int:pk>/muuda/", views.task_form, name="task_edit"),
    path("ulesanded/<int:pk>/olek/", views.task_toggle, name="task_toggle"),
    path("ulesanded/<int:pk>/kustuta/", views.task_delete, name="task_delete"),
    path("kalender/", views.calendar, name="calendar"),
]
