# KooliKompass

Eestikeelne kooliülesannete ja tähtaegade planeerija. Projekt sisaldab töötavat Django veebirakendust ning selle arenduskavandit.

## Käivitamine

Windowsis käivita projekti põhikaustas `kaivita.cmd` ja ava [localhost:8000](http://127.0.0.1:8000). Esimesel käivitamisel on vaja [uv-d](https://docs.astral.sh/uv/getting-started/installation/) ja internetiühendust.

Loo konto, lisa õppeained ning sisesta ülesanded. Andmed säilivad failis `app/db.sqlite3`. Serveri peatamiseks vajuta `Ctrl+C`.

Käsurealt, projekti põhikaustas:

```sh
uv sync --python 3.13 --frozen
uv run python app/manage.py migrate
uv run python app/manage.py runserver
```

## Võimalused

- Konto loomine ning sisse- ja väljalogimine.
- Isiklikud õppeained ja ülesannete lisamine, muutmine ning kustutamine.
- Ülesannete tehtuks märkimine, otsing ja filtrid.
- Tähtaegade järgi järjestatud nimekiri ja nädalakalender.

Õpilane sisestab oma ülesanded ise. Rakendus kasutab Djangot, HTML-i, CSS-i ja JavaScripti. Vaikimisi andmebaas on SQLite; PostgreSQL-i seadistus on [rakenduse juhendis](app/README.md).

## Koodi ülesehitus

| Asukoht | Sisu |
| --- | --- |
| `app/planner/models.py` | Õppeained, ülesanded ja andmebaasireeglid |
| `app/planner/forms.py` | Sisestusvormid ja andmete kontroll |
| `app/planner/views.py` | Päringute töötlemine, filtrid ja kalender |
| `app/planner/urls.py` | Aadresside sidumine vaadetega |
| `app/templates/` | HTML-mallid |
| `app/static/` | Kujundus ja JavaScript |
| `app/koolikompass/` | Django seadistus ja projekti URL-id |
| `app/planner/tests.py` | Automaattestid |

Koodis on eestikeelsed kommentaarid, mis selgitavad funktsioone ja olulisemate ridade tähendust.

## Kontrollimine

```sh
uv run python app/manage.py check
uv run python app/manage.py test planner
uv run python app/manage.py makemigrations --check --dry-run
```

## Projekti materjalid

- [Kavand ja teostus](docs/projekt.md)
- [Kaitsmise meelespea ja harjutused](docs/kaitsmine.md)
- [Rakenduse juhend](app/README.md)
- [Arhitektuuriskeem](diagrams/arhitektuur.drawio) ja [andmemudel](diagrams/andmemudel.drawio)
- [GitHubi repositoorium](https://github.com/Ken-Janek/koolikompass) ja [projektitahvel](https://github.com/users/Ken-Janek/projects/1)
