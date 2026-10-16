# Faili eesmärk: määrata rakenduse andmebaas, turvaseaded, keel, ajavöönd ning failide asukohad.

import os
import secrets
from pathlib import Path

# Lähtekaust app/: sellest tuletatakse mallide, staatiliste failide ja andmebaasi asukohad.
BASE_DIR = Path(__file__).resolve().parent.parent
# Keskkonnamuutujad lubavad sama koodi kasutada arenduses ja majutuses.
DEBUG = os.getenv("DJANGO_DEBUG", "1") == "1"
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "")
if not SECRET_KEY:
    # Tootmises peab salajane võti tulema keskkonnamuutujast.
    if not DEBUG:
        raise RuntimeError("Tootmiskeskkonnas määra DJANGO_SECRET_KEY.")
    # Arenduse võti säilib kohalikus failis, et sessioonid taaskäivitamisel kehtiksid.
    secret_path = BASE_DIR / ".dev-secret"
    try:
        # Režiim x loob faili ainult siis, kui seda veel pole; olemasolevat võtit ei kirjutata üle.
        with secret_path.open("x", encoding="utf-8") as secret_file:
            secret_file.write(secrets.token_urlsafe(50))
    except FileExistsError:
        pass
    SECRET_KEY = secret_path.read_text(encoding="utf-8").strip()
# Komadega eraldatud hostinimed piiravad lubatud HTTP Host päiseid.
ALLOWED_HOSTS = [h.strip() for h in os.getenv("DJANGO_ALLOWED_HOSTS", "localhost,127.0.0.1,[::1]").split(",") if h.strip()]
# Django moodulid pakuvad kontosid, sessioone, haldust ja meie planner-rakendust.
INSTALLED_APPS = [
    "django.contrib.admin", "django.contrib.auth", "django.contrib.contenttypes",
    "django.contrib.sessions", "django.contrib.messages", "django.contrib.staticfiles",
    "planner",
]
# Vahekihid töötlevad päringuid loendi järjekorras ja vastuseid vastupidises järjekorras.
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
ROOT_URLCONF = "koolikompass.urls"
# Mallimootor leiab HTML-failid; kontekstitöötlejad lisavad request, user ja messages muutujad.
TEMPLATES = [{
    "BACKEND": "django.template.backends.django.DjangoTemplates",
    "DIRS": [BASE_DIR / "templates"], "APP_DIRS": True,
    "OPTIONS": {"context_processors": [
        "django.template.context_processors.request",
        "django.contrib.auth.context_processors.auth",
        "django.contrib.messages.context_processors.messages",
    ]},
}]
WSGI_APPLICATION = "koolikompass.wsgi.application"
# POSTGRES_DB olemasolu valib PostgreSQL-i; vaikimisi kasutatakse kohalikku SQLite-faili.
if os.getenv("POSTGRES_DB"):
    DATABASES = {"default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ["POSTGRES_DB"], "USER": os.environ["POSTGRES_USER"],
        "PASSWORD": os.environ["POSTGRES_PASSWORD"],
        "HOST": os.getenv("POSTGRES_HOST", "localhost"),
        "PORT": os.getenv("POSTGRES_PORT", "5432"),
    }}
else:
    DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": BASE_DIR / "db.sqlite3"}}
# Sisseehitatud kontrollid keelavad liiga lihtsad või kasutajanimega sarnased paroolid.
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]
# Kasutajaliidese keel on eesti; ajavööndiga ajad kuvatakse Tallinna ajas.
LANGUAGE_CODE = "et"
TIME_ZONE = "Europe/Tallinn"
USE_I18N = True
USE_TZ = True
# Arenduse lähtefailid asuvad static-kaustas; collectstatic kogub need STATIC_ROOT kausta.
STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
# Nimelised URL-id määravad autentimise suunamised.
LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "dashboard"
LOGOUT_REDIRECT_URL = "login"
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = "Lax"
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"
# Tootmisrežiimis nõutakse HTTPS-i ja turvalisi küpsiseid.
if not DEBUG:
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = True
