# Faili eesmärk: siduda planeerija veebiaadressid neid töötlevate funktsioonidega.

from django.urls import path
from . import views

# Django otsib loendist sobiva marsruudi. path seob aadressi funktsiooniga.
# name on nimi, mida kasutavad redirect ja HTML-mallide url-käsud.
urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("konto/registreeru/", views.register, name="register"),
    path("ained/", views.subjects, name="subjects"),
    path("ulesanded/lisa/", views.task_form, name="task_create"),
    # Näiteks /ulesanded/5/muuda/ edastab funktsioonile pk=5; pk tähendab primaarvõtit.
    path("ulesanded/<int:pk>/muuda/", views.task_form, name="task_edit"),
    path("ulesanded/<int:pk>/olek/", views.task_toggle, name="task_toggle"),
    path("ulesanded/<int:pk>/kustuta/", views.task_delete, name="task_delete"),
    path("kalender/", views.calendar, name="calendar"),
]
