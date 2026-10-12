# KooliKompass

Kooliülesannete ja tähtaegade planeerija — arenduskavand ja töötav Django rakendus.

## Rakenduse käivitamine

Windowsis käivita põhikaustas **`kaivita.cmd`**, seejärel ava **http://127.0.0.1:8000**. Loo konto, lisa õppeained ja sisesta ülesanded. Andmed säilivad kohalikus andmebaasis.

[Käivitamisjuhend ja PostgreSQL-i seadistamine](app/README.md) · [Rakenduse lähtekood](app/) · [Kontrollitulemused](docs/10-rakenduse-teostus.md)

## Projekti idee

KooliKompass on kooliülesannete ja tähtaegade planeerija arenduskavand, mis on koostatud õppeülesande jaoks. Rakendus koondaks ülesanded ja tähtajad ühte vaatesse.

Sihtkasutaja on õpilane. Esimene versioon on isiklik planeerija: õpetaja ei jaga selles ülesandeid ja rakendus ei ühendu kooli infosüsteemiga. Ülesanded sisestab õpilane ise.

## Esimese töötava versiooni eesmärk

Õpilane saab sisse logida, lisada õppeaine ja ülesande koos tähtajaga, näha ülesandeid tähtaja järjekorras ning märkida need tehtuks. Tulemus on edukas, kui kolm proovikasutajat suudavad abita lisada ülesande, leida lähima tähtaja ja märkida ülesande tehtuks. Iga tegevuse siht on alla ühe minuti.

## Materjalid

- [Arendusprotsess](docs/01-arendusprotsess.md)
- [Metoodika, backlog ja esimene arendusperiood](docs/02-metoodika-ja-backlog.md)
- [CASE-vahendid ja kasutusjuhend](docs/03-case-vahendid.md)
- [Arhitektuur ja andmemudel](docs/04-arhitektuur.md)
- [Git ja versiooniplaan](docs/05-git-ja-versioonid.md)
- [Kaitsmise kava ja nõuete kontroll](docs/06-kaitsmine.md)
- [15–20 minuti praktilise kaitsmise harjutused](docs/07-praktiline-kaitsmine.md)
- [Õppetekst ja kaitsmisel avatavad lingid](docs/08-oppetekst-ja-lingid.md)
- [Arhitektuuriskeemi kolm muudetavat harjutuskoopiat](docs/09-skeemide-koopiad.md)
- [Muudetav arhitektuuriskeem](diagrams/arhitektuur.drawio)
- [Muudetav andmemudel](diagrams/andmemudel.drawio)
- [Projektitahvli ettevalmistus](planning/github-projects.md)
- [Kasutajalugude andmed](planning/backlog.json)

## Valitud lahendus

Veebirakendus, kihiline monoliit, iteratiivne ja inkrementaalne arendus ning Kanban. Tehnoloogia on Django koos serveris renderdatavate HTML-mallide ja CSS-iga. Kohalik käivitus kasutab SQLite'i; kavandatud PostgreSQL-i ühenduse saab seadistada keskkonnamuutujatega. Algne arendusplaan säilib kavandamise dokumentides ja töötav teostus asub kaustas `app/`.

## Hetkeseis ja tegelikud tõendid

- [Avalik GitHubi repositoorium](https://github.com/Ken-Janek/koolikompass)
- [Avalik GitHub Projects Kanbani tahvel](https://github.com/users/Ken-Janek/projects/1)
- [Sisuliste commit'ide ajalugu](https://github.com/Ken-Janek/koolikompass/commits/main/)
- [Arhitektuuriskeem diagrams.net-is](https://app.diagrams.net/#Uhttps%3A%2F%2Fraw.githubusercontent.com%2FKen-Janek%2Fkoolikompass%2Fmain%2Fdiagrams%2Farhitektuur.drawio)
- [Andmemudel diagrams.net-is](https://app.diagrams.net/#Uhttps%3A%2F%2Fraw.githubusercontent.com%2FKen-Janek%2Fkoolikompass%2Fmain%2Fdiagrams%2Fandmemudel.drawio)

Tahvlil on kaheksa kirjeldatud kasutajalugu koos prioriteetide, hinnangute, sõltuvuste ja vastuvõtukriteeriumidega. US-01–US-08 on pärast kohaliku teostuse kontrollimist Done-veergu viidud. In progress ja In review piir on üks kaart. Arhitektuuriskeem on avatud ja visuaalselt kontrollitud diagrams.net-is; mõlema XML-faili struktuur ning viited on kontrollitud.

Rakenduse teostuses on kontod, õppeained, ülesannete haldus, filtrid, otsing ja nädalavaade. Projekti tahvel näitab teostatud tööde seisu; varasem `evidence/kanban.jpg` säilitab algse plaani ja `evidence/kanban-valmis.jpg` näitab Done-veergu. Teostuse ja kontrollimise tulemused on [eraldi dokumendis](docs/10-rakenduse-teostus.md). Avaldamiseks mõeldud commit'ides kasutatakse GitHubi noreply aadressi.
