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
- [Muudetav arhitektuuriskeem](diagrams/arhitektuur.drawio)
- [Muudetav andmemudel](diagrams/andmemudel.drawio)
- [Projektitahvli ettevalmistus](planning/github-projects.md)
- [Kasutajalugude andmed](planning/backlog.json)

## Valitud lahendus

Veebirakendus, kihiline monoliit, iteratiivne ja inkrementaalne arendus ning Kanban. Kavandatav tehnoloogia on Django koos serveris renderdatavate HTML-mallide, CSS-i ja PostgreSQL-iga. Tegemist on kavandiga, mitte valmis rakendusega.

## Hetkeseis

Kohalikud dokumendid, skeemid ja Git-ajalugu on kavandamise tõendid. GitHubi repositooriumi ning GitHub Projects tahvli olemasolu tuleb kinnitada nende tegelike linkidega; juhend või JSON-fail ei asenda töötavat projektitahvlit.
