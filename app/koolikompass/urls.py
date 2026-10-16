# Faili eesmärk: jagada saabuvad veebiaadressid haldusliidese, kontovaadete ja planeerija vahel.

from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from planner.forms import LoginForm

urlpatterns = [
    path("admin/", admin.site.urls),
    path("konto/logi-sisse/", auth_views.LoginView.as_view(template_name="registration/login.html", authentication_form=LoginForm), name="login"),
    path("konto/logi-valja/", auth_views.LogoutView.as_view(), name="logout"),
    path("", include("planner.urls")),
]
