# Töötav rakendus: versioon 0.3.0

Arenduskavandi põhjal on lisatud Django rakendus kausta `app/`. Kavandamise dokumendid ja tahvel säilitavad algse plaani; see dokument kirjeldab praegust teostust.

## Kasutajalood ja teostus

| Lugu | Teostatud funktsioon |
|---|---|
| US-01 | Konto loomine, sisselogimine ja POST-põhine väljalogimine |
| US-02 | Õppeaine lisamine nime ja värviga; nime unikaalsus ühe kasutaja piires |
| US-03 | Pealkirja, õppeaine, tähtaja ja kirjeldusega ülesande salvestamine |
| US-04 | Tähtaja ning ID järgi järjestatud tegemata tööd, tekstiline hilinemise märge ja tühi vaade |
| US-05 | Tehtuks märkimine ja taastamine; korduv sama oleku saatmine ei pööra tulemust tagasi |
| US-06 | Ülesande muutmine ning kustutamine eraldi kinnitusega |
| US-07 | Õppeaine- ja olekufiltrid, tekstiotsing ja tulemusteta vaade |
| US-08 | Seitsme päeva kalender ning eelmise, järgmise ja käesoleva nädala valik |

## Seos arhitektuuriga

Päringud asuvad `planner/views.py` failis, sisestuse kontroll `planner/forms.py` failis ning andmemudel ja ORM `planner/models.py` failis. HTML-mallid on `templates/` ning stiilid ja väike kasutajaliidese skript `static/` kaustas. Rakendus on kihiline monoliit.

SQLite on kohaliku käivitamise lihtsustus. PostgreSQL-i tugi on seadistuses ja draiver on lukustatud sõltuvustes, kuid PostgreSQL-i vastu pole selles keskkonnas teste käivitatud. Ajavöönd on esialgu kogu rakendusel `Europe/Tallinn`; kasutaja muudetav ajavööndiprofiil jääb hilisemaks.

## Kontrollitud tulemused

- Django `check`: seadistusvigu ei leitud.
- `makemigrations --check --dry-run`: mudelid ja salvestatud migratsioon on kooskõlas.
- 13 Django testi läbisid SQLite'i testandmebaasis.
- Testid kontrollivad salvestamist, muutmist, tehtuks märkimist, taastamist, kustutamise kinnitust, kontosüsteemi, võõra kasutaja andmete kaitset, võõra õppeaine sisestamise keelamist, CSRF-i, filtreid, nädalapiire, lehekülgi ja HTML-i ohutut kuvamist.
- Brauseris kontrollitud: demo konto sisselogimine, ülesande lisamine, tehtuks märkimine ja selle kajastumine nädalakalendris.
- 360 px telefoni vaates kontrollitud nimekiri ja nädalavaade: puudub horisontaalne ülevool ning väljalogimine jääb kättesaadavaks.

Kontrollid kasutavad sünteetilisi andmeid. Kolme päris õpilase proovikasutust ega internetis tootmiskeskkonda avaldamist pole tehtud.

## Käivitamine

Kasuta põhikausta `kaivita.cmd` faili. Üksikasjad ja PostgreSQL-i seadistus on [rakenduse juhendis](../app/README.md).

Versioon 0.3.0 on esialgne töötav teostus, mitte stabiilne tootmislubadus. Filtrid ja nädalavaade on realiseeritud varem, kui algses versiooniplaanis ette nähtud.
