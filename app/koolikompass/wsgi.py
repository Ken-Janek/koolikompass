"""WSGI sisenemispunkt: majutusserver laadib siit Django application-objekti."""
import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "koolikompass.settings")
application = get_wsgi_application()
