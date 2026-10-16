# Faili eesmärk: käivitada Django halduskäsud, näiteks server, migratsioonid ja testid.

import os
import sys

# See plokk käivitub faili otse käivitamisel, mitte mooduli importimisel.
if __name__ == "__main__":
    # Vali Django seadistusmoodul; setdefault säilitab juba määratud keskkonnaväärtuse.
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "koolikompass.settings")
    from django.core.management import execute_from_command_line
    # sys.argv sisaldab käsurea argumente, näiteks migrate või runserver.
    execute_from_command_line(sys.argv)
