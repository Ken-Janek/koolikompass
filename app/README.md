# KooliKompassi rakendus

Töötav Django veebirakendus. Lähtekood on samas repositooriumis kavandiga.

## Windowsis käivitamine

1. Ava projekti põhikaust ja käivita `kaivita.cmd`.
2. Ava **http://127.0.0.1:8000**.
3. Vajuta „Loo konto“, seejärel lisa õppeained ja ülesanded.

Esimesel seadistusel on vaja [uv-d](https://docs.astral.sh/uv/getting-started/installation/) ja internetiühendust. Käivitusfail valmistab vajaduse korral ette virtuaalkeskkonna ning rakendab andmebaasi migratsioonid. Kui virtuaalkeskkond on juba olemas, saab rakenduse käivitada kohe. Serveri peatamiseks vajuta terminalis Ctrl+C.

Andmed salvestuvad faili `app/db.sqlite3` ja säilivad serveri taaskäivitamisel. See fail ning arenduskeskkonna juhuslik salajane võti ei kuulu Git-i.

## Käsurealt

Käivita käsud repositooriumi põhikaustas:

```sh
uv sync --python 3.13 --frozen
uv run python app/manage.py migrate
uv run python app/manage.py runserver
```

Windowsi olemasoleva virtuaalkeskkonnaga saab `uv run python` asemel kasutada `.venv\Scripts\python.exe`.

## Funktsioonid

- Konto loomine, sisselogimine ja väljalogimine.
- Enda õppeainete lisamine; korduv ainenimi on ühe kasutaja piires keelatud.
- Ülesande lisamine, muutmine, kustutamise kinnitus ning tehtuks või tegemata märkimine.
- Tähtaja järgi järjestatud nimekiri, hilinenud tööd ja tänased tähtajad.
- Õppeaine- ja olekufiltrid, tekstiotsing ning lehekülgede kaupa laadimine.
- Nädalakalender eelmise, järgmise ja käesoleva nädala valikuga.
- Kohanduv eestikeelne kasutajaliides, mis töötab arvutis ja telefonis.

Tähtajad kuvatakse Eesti ajavööndis (`Europe/Tallinn`). Kasutaja ajavööndi muutmine pole selles versioonis lisatud. Registreerimiseks pole vaja e-posti aadressi. Parooli taastamise meilid, kooli infosüsteemide ühendused ja eraldi mobiilirakendus pole lisatud.

## Demoandmed

Soovi korral loo eraldi demo kasutaja sünteetiliste koolitöödega:

```sh
uv run python app/manage.py demo
```

Käsk küsib parooli; parooli pole lähtekoodis. Olemasolevat kasutajat ega tema andmeid ei kirjutata üle. Uue nime jaoks lisa `--username proov`.

## Kontrollimine

```sh
uv run python app/manage.py check
uv run python app/manage.py test planner
uv run python app/manage.py makemigrations --check --dry-run
```

Testid kontrollivad põhiteekonda, andmete eraldatust, võõra aine sisestamise keelamist, CSRF-kaitset, filtreid, nädalapiire, lehekülgi ja HTML-i ohutut kuvamist.

## PostgreSQL

Kohalikuks lihtsaks käivitamiseks kasutatakse SQLite'i. Kavandatud PostgreSQL-i kasutamiseks määra enne migratsioonide käivitamist keskkonnamuutujad:

```text
POSTGRES_DB=koolikompass
POSTGRES_USER=koolikompass
POSTGRES_PASSWORD=<enda parool>
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

Seejärel käivita migratsioonid PostgreSQL-is. SQLite'i olemasolevad andmed ei kandu automaatselt teise andmebaasi; olemasoleva kasutuse korral tuleb nende üleviimine eraldi planeerida. PostgreSQL-i draiver sisaldub sõltuvustes.

## Internetis avaldamine

Praegune käivitusfail kasutab kohalikku arendusserverit. Internetis avaldamiseks vali Django majutus, seadista tootmise server ja staatiliste failide teenindamine ning määra `DJANGO_DEBUG=0`, `DJANGO_SECRET_KEY` ja `DJANGO_ALLOWED_HOSTS`. Vajalikud on HTTPS, varundus, migratsioonid, saladuste turvaline hoiustamine ning sisselogimiskatsete piiramine majutuskeskkonnas või täiendava lahendusega. Tootmiskeskkonnas ei kasutata `runserver`-it. `collectstatic` koondab stiilifailid tootmise staatiliste failide kausta.

Django dokumentatsioon: [kontosüsteem](https://docs.djangoproject.com/en/5.2/topics/auth/default/) ja [kasutuselevõtu juhend](https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/).
