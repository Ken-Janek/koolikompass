import getpass
from datetime import datetime, time, timedelta
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.utils import timezone
from planner.models import Subject, Task


class Command(BaseCommand):
    help = "Loo eraldi demo kasutaja sünteetiliste õppeainete ja ülesannetega."

    def add_arguments(self, parser):
        parser.add_argument("--username", default="demo")
        parser.add_argument("--password-stdin", action="store_true")

    @transaction.atomic
    def handle(self, *args, **options):
        username = options["username"]
        if User.objects.filter(username=username).exists():
            raise CommandError("Selle nimega kasutaja on juba olemas; vali teine nimi. Olemasolevaid andmeid ei muudeta.")
        if options["password_stdin"]:
            import sys
            password = sys.stdin.readline().rstrip("\r\n")
        else:
            password = getpass.getpass("Demo konto parool: ")
        from django.contrib.auth.password_validation import validate_password
        validate_password(password, User(username=username))
        user = User.objects.create_user(username, password=password)
        names = [("Tarkvaraarendus", "#8b82f6"), ("Matemaatika", "#d49a4c"), ("Inglise keel", "#5d9ac9"), ("Andmebaasid", "#4a9b82")]
        subjects = [Subject.objects.create(owner=user, name=name, color=color) for name, color in names]
        sample = [
            ("Lõpeta projekti arenduskavand", 0, 0, "Vaata üle kasutajalood ja skeemide seosed."),
            ("Lahenda võrrandite ülesanded", 1, 1, "Harjutused 12–18, lisa lahenduskäik."),
            ("Valmista ette inglise keele esitlus", 2, 3, "Teema: minu tulevikuplaanid."),
            ("Koosta andmebaasi ER-diagramm", 3, 4, "Määra tabelite võtmed ja seosed."),
            ("Korda funktsioonide graafikuid", 1, -1, "Kontrolli eelmise tunni märkmeid."),
            ("Kirjuta kasutajalugude vastuvõtukriteeriumid", 0, 5, "Iga lugu peab olema kontrollitav."),
        ]
        today = timezone.localdate()
        for title, subject, offset, description in sample:
            due = timezone.make_aware(datetime.combine(today + timedelta(days=offset), time(20, 0)))
            Task.objects.create(subject=subjects[subject], title=title, due_at=due, description=description)
        Task.objects.create(subject=subjects[0], title="Vali projekti arendusmudel", due_at=timezone.now()-timedelta(days=2), completed=True)
        self.stdout.write(self.style.SUCCESS(f"Demo konto '{username}' on loodud. Parooli ei salvestata lähtekoodi ega logisse."))
