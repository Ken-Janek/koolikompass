# Projekti ülevaade

KooliKompass on õpilase isiklik koolitööde ja tähtaegade planeerija. Konto, õppeained, ülesannete haldus, otsing, filtrid ja nädalakalender on teostatud. Õpetaja rolli ega kooli infosüsteemi ühendust pole.

## Arendus ja töökorraldus

Etapid: vajaduste uurimine → nõuded → kavand → teostus → testimine → kasutuselevõtt → hooldus. Valitud on **iteratiivne ja inkrementaalne arendus**, sest väikest töötavat osa saab tagasiside järgi täiendada. Koskmudel sobib stabiilsete nõuetega projektile, kuid tagasiside võib saabuda hilja.

Ühe arendaja **Kanban**: Backlog → Ready → In progress → In review → Done. Töös ja kontrollimisel võib kummaski olla üks kaart. Alustamiseks peavad nõuded ja sõltuvused olema selged; lõpetamiseks kriteeriumid kontrollitud ning muudatus Git-is. Uus nõue tähendab mõju hindamist ja prioriteetide uuendamist.

## Kasutajalood

Õpilasena soovin järgmisi võimalusi. P1 = vajalik, P2 = mugavus, P3 = hilisem täiendus. Hinnangud on algsest kavandist; kõik kaheksa funktsiooni on teostatud.

| ID | Soov ja vastuvõtt | Prioriteet | Tundi | Sõltub |
| --- | --- | --- | ---: | --- |
| US-01 | Konto ja sisselogimine; vale parool keelatud, võõrad andmed kaitstud | P1 | 6 | — |
| US-02 | Aine lisamine; nimi kohustuslik ja omaniku piires unikaalne | P1 | 3 | US-01 |
| US-03 | Töö lisamine; pealkiri, enda aine ja tähtaeg kohustuslikud, andmed säilivad | P1 | 5 | US-02 |
| US-04 | Enda tegemata tööd tähtaja ja ID järjekorras; hilinemine tähistatud | P1 | 4 | US-03 |
| US-05 | Tehtuks märkimine ja taastamine; olek säilib | P1 | 2 | US-04 |
| US-06 | Enda töö muutmine ja kustutamine; kustutamine vajab kinnitust | P1 | 3 | US-03 |
| US-07 | Aine- ja olekufilter töötavad eraldi ning koos | P2 | 3 | US-04, US-05 |
| US-08 | Nädala vahetamine ja enda tähtajad õigel päeval | P3 | 5 | US-04 |

[Tööde tahvel](https://github.com/users/Ken-Janek/projects/1) · [Backlog'i andmed](../planning/backlog.json).

Esialgne ajakava: kuus nädalat × 10 h. Esimene periood: keskkond 2 h + US-01–US-03 14 h + demo 1 h + puhver 3 h = **20 h**. Edasi nimekiri ja haldus, proovikasutus ning avaldamine. Ulatuskasvu ja ajariski vähendavad prioriteedid ja puhver; andmekadu varundus ja taastamise kontroll.

## Tehniline lahendus

**Django kihiline monoliit**: vaated töötlevad päringuid, vormid kontrollivad sisendit, mudelid haldavad andmeid ja mallid kuvavad HTML-i. Üks tervik on lihtne hallata; puudus on ühine rikete mõju ja koos skaleerimine. Mikroteenused annaksid sõltumatu skaleerimise, kuid lisaksid halduskoormust.

Andmevoog: brauser → sessiooni-, CSRF- ja vormikontroll → ORM → andmebaas → HTML-vastus. Omanik tuleb sessioonist. Kasutajal on mitu ainet, ainel mitu ülesannet; töö omanik leitakse aine kaudu. Hilinemine arvutatakse tähtajast ja olekust.

Kohalik andmebaas on SQLite; PostgreSQL on seadistatav. Ajavöönd on `Europe/Tallinn`. [Arhitektuuriskeem](../diagrams/arhitektuur.drawio) · [Andmemudel](../diagrams/andmemudel.drawio) · [Käivitamisjuhend](../app/README.md).

## Vahendid ja versioonid

**diagrams.net** võimaldab skeeme visuaalselt muuta; alternatiiv PlantUML kirjeldab skeemi tekstina ja on Git-is lihtsam võrrelda. **GitHub Projects** näitab tööde järjekorda ja olekut. Git säilitab failide ajaloo.

Commit salvestab kohaliku muudatuse, push saadab selle GitHubi, haru eraldab arendust ja tag märgistab väljalaske. SemVer näited versioonist 2.4.1: veaparandus **2.4.2**, uus tagasiühilduv funktsioon **2.5.0**, lõhkuv muudatus **3.0.0**.

Praegune versioon on **0.3.0**; järgmised sihid on proovikasutus ja stabiilne 1.0.0. [Commit'ide ajalugu](https://github.com/Ken-Janek/koolikompass/commits/main/).

## Kontrollid ja piirangud

Varasemal kontrollil läbisid 13 Django testi SQLite'is, seadistuskontroll ja migratsioonide kontroll. Testid katavad töövoo, andmete kaitse, vormid, filtrid, kalendri ja HTML-i ohutu kuvamise. Brauseris kontrolliti ka 360 px telefonivaadet; [tõendipildid](../evidence/) on säilitatud.

PostgreSQL-i teste, kolme õpilase proovikasutust ja tootmises avaldamist pole tehtud. Proovikasutuse siht: ülesande lisamine, lähima tähtaja leidmine ja tehtuks märkimine, iga tegevus alla minuti. Enne avaldamist on vaja HTTPS-i, saladuste seadistust, varundust ja taastamise proovimist.
