# Faili eesmärk: anda majutusserverile Django rakendus, mis võtab vastu veebipäringuid.

import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "koolikompass.settings")
application = get_wsgi_application()
