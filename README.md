# KooliKompass

Kooliülesannete ja tähtaegade planeerija — tarkvararakenduse arenduskavand.

## Idee ja isiklik seos

Õpilasena pean jälgima eri õppeainete ülesandeid ja tähtaegu. KooliKompass koondaks need ühte vaatesse, et saaksin otsustada, mida järgmisena teha. See on projekti lähte-eeldus: enne esitamist lisan oma tegeliku näite olukorrast, kus ülesannete jälgimine oli keeruline.

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
- [Muudetav arhitektuuriskeem](diagrams/arhitektuur.drawio)
- [Muudetav andmemudel](diagrams/andmemudel.drawio)
- [Projektitahvli ettevalmistus](planning/github-projects.md)
- [Kasutajalugude andmed](planning/backlog.json)

## Valitud lahendus

Veebirakendus, kihiline monoliit, iteratiivne ja inkrementaalne arendus ning Kanban. Kavandatav tehnoloogia on Django koos serveris renderdatavate HTML-mallide, CSS-i ja PostgreSQL-iga. Tegemist on kavandiga, mitte valmis rakendusega.

## Hetkeseis ja tegelikud tõendid

- [Avalik GitHubi repositoorium](https://github.com/Ken-Janek/koolikompass)
- [Avalik GitHub Projects Kanbani tahvel](https://github.com/users/Ken-Janek/projects/1)
- [Sisuliste commit'ide ajalugu](https://github.com/Ken-Janek/koolikompass/commits/main/)
- [Arhitektuuriskeem diagrams.net-is](https://app.diagrams.net/#Uhttps%3A%2F%2Fraw.githubusercontent.com%2FKen-Janek%2Fkoolikompass%2Fmain%2Fdiagrams%2Farhitektuur.drawio)
- [Andmemudel diagrams.net-is](https://app.diagrams.net/#Uhttps%3A%2F%2Fraw.githubusercontent.com%2FKen-Janek%2Fkoolikompass%2Fmain%2Fdiagrams%2Fandmemudel.drawio)

Tahvlil on kaheksa kirjeldatud kasutajalugu koos prioriteetide, hinnangute, sõltuvuste ja vastuvõtukriteeriumidega. US-01 on Ready ning teised Backlog. In progress ja In review piir on üks kaart. Arhitektuuriskeem on avatud ja visuaalselt kontrollitud diagrams.net-is; mõlema XML-faili struktuur ning viited on kontrollitud.

Rakendust pole programmeeritud. Kavandamise commit'id ja tööde planeerimine on valmis; rakenduse arenduslood ootavad teostust. Avaldamiseks mõeldud commit'ides kasutatakse GitHubi noreply aadressi.
