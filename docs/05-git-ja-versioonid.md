# 5. Git ja versioonimine

## Repositoorium ja muudatuste ajalugu

Avalik repositoorium: [Ken-Janek/koolikompass](https://github.com/Ken-Janek/koolikompass).

Git salvestab dokumendi ja skeemi seisud commit'idena. GitHub hoiab nende kaugkoopiat ning võimaldab kavandit õpetajaga jagada. Kohalik commit ja GitHubi push on erinevad tegevused.

Kavandi ajalugu koosneb sisulistest osadest: idee ja ulatus; protsessimudelite võrdlus; Kanban ja kasutajalood; arhitektuur ning CASE-skeemid; versiooniplaan ja kaitsmise kontroll. Tegeliku ajaloo vaatamiseks kasutan `git log --oneline`, muudatuse sisu vaatamiseks `git show <commit>` ja töökausta kontrolliks `git status`.

Tulevases arenduses teen ühe kasutajaloo jaoks haru, näiteks `feature/us-03-ulesande-lisamine`. Kontrollin muudatust enne main-harusse liitmist. Commit'i sõnum kirjeldab tulemust, näiteks `feat: lisa tahtajaga ulesande salvestamine` või `fix: keela voora ulesande muutmine`.

Näidis töövoost:

```sh
git switch -c feature/us-03-ulesande-lisamine
git add docs/04-arhitektuur.md diagrams/andmemudel.drawio
git commit -m "design: tapsusta ulesande tahtaja salvestamist"
git push -u origin feature/us-03-ulesande-lisamine
```

See näide ei tähenda, et vastav arendus või haru oleks juba tehtud. Paroolid, `.env` ja päris kasutajate ülesanded ei kuulu avalikku repositooriumi.

## SemVer-i leping

Rakenduse versioon on **MAJOR.MINOR.PATCH**. Alates 1.0.0-st on avalik ühilduvusleping dokumenteeritud ülesannete töövoog ning tulevase ekspordi/liidese korral ka selle andmevorming. SemVer keskendub avaliku liidese ühilduvusele; rakenduses tuleb selgelt määratleda, mida see tähendab.

| Muudatus | Näide | Versioon |
|---|---|---|
| PATCH | Parandan tähtaja järjestamist, muutmata töövoogu või andmevormingut. | 1.0.0 → 1.0.1 |
| MINOR | Lisan valikulise nädalakalendri; olemasolev nimekirjavaade töötab edasi. | 1.0.1 → 1.1.0 |
| MAJOR | Muudan dokumenteeritud impordivormingut nii, et vana vorming enam ei tööta; kasutajad peavad andmed teisendama. | 1.1.0 → 2.0.0 |

MINOR-i tõstmisel lähtestan PATCH-i; MAJOR-i tõstmisel lähtestan mõlemad väiksemad numbrid. Suur sisemine ümberkirjutus ei nõua iseenesest MAJOR-i, kui avalik leping jääb ühilduvaks. Andmebaasi migratsioon ei ole automaatselt kasutajale ühilduvust rikkuv muudatus.

## Väljalasete plaan

| Versioon | Kavandatud sisu |
|---|---|
| 0.1.0 | Arenduskavand, backlog ja skeemid; rakendust ei ole veel |
| 0.2.0 | Esimese perioodi tulemus: konto, õppeaine ja ülesande lisamine |
| 0.3.0 | Ülesannete nimekiri, tehtuks märkimine, muutmine ja kustutamine |
| 1.0.0-rc.1 | Esimese stabiilse versiooni proovikasutus |
| 1.0.0 | Kontrollitud põhifunktsioonid ja kasutuselevõtt |
| 1.1.0 | Filtrid ja nädalakalender pärast tagasiside läbivaatamist |

0.x tähistab esialgset arendust, mille avalik leping võib muutuda. Väljalaskekandidaat `1.0.0-rc.1` ei ole veel stabiilne 1.0.0.

Väljalaskmisel kontrollin testid ja migratsioonid, uuendan väljalaskemärkmeid ning märgistan täpse commit'i Git-tag'iga, näiteks `v1.0.0`. GitHub Release sisaldab lisandusi, parandusi, ühilduvuse muutusi ja vajadusel uuendusjuhendit. Avaldatud versiooni sisu ei kirjuta ümber: paranduse jaoks teen uue numbri. Kasutajaliidese jaluses näitan paigaldatud versiooni, et veateatele saaks lisada õige väljalaske.

Allikas: [Semantic Versioning 2.0.0](https://semver.org/).
