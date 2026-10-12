# Kaitsmise kava ja nõuete kontroll

## Umbes 7-minutiline esitlus

1. **Idee, 45 sekundit.** „KooliKompass aitab mul koondada eri ainete ülesanded ja tähtajad ühte kohta.“ Lisa oma tegelik näide. Ütle, et rakendus on kavandatud, mitte programmeeritud.
2. **Protsess, 1 minut.** Selgita etappe ja võrdle koskmudelit iteratiivse mudeliga. Too nädalakalendri lisamise näide nõuete muutumisest.
3. **Kanban, 1,5 minutit.** Ava tegelik GitHub Projects tahvel, näita kaheksat lugu, prioriteete, US-03 sõltuvust ning esimese perioodi 20 tunni plaani. Selgita poolelioleva töö piirangut.
4. **CASE, 1 minut.** Ava `.drawio` fail diagrams.net-is ja muuda ühe komponendi nime. Võrdle visuaalset redaktorit PlantUML-i tekstikirjeldusega.
5. **Arhitektuur, 1,5 minutit.** Jälgi skeemil ülesande lisamise teekonda brauserist andmebaasi ja tagasi. Põhjenda monoliiti võrreldes mikroteenustega. Näita andmemudeli seoseid.
6. **Git, 1 minut.** Ava GitHubi commit'ide ajalugu ja üks sisuline muudatus. Too PATCH-, MINOR- ja MAJOR-näide. Ütle, et tag märgistab täpse väljalaske commit'i.

## Nõuete vastavus

| Õpetaja nõue | Materjal või tõend |
|---|---|
| Arendusetapid ja eesmärgid | `01-arendusprotsess.md`, etappide tabel |
| Kahe mudeli võrdlus, valik ja nõuete muutus | `01-arendusprotsess.md` |
| Metoodika põhjendus ja jälgimine | `02-metoodika-ja-backlog.md`, Kanbani reeglid |
| Vähemalt kuus kasutajalugu ja prioriteedid | Kaheksa lugu US-01–US-08 |
| Esimene arendusperiood | Kahe nädala ja 20 tunni plaan |
| Tööd projektihaldusvahendis | Tegelik GitHub Projects tahvel; ainult kohalik nimekiri ei täida seda nõuet |
| Vähemalt kaks vahendit ja nende kasutus | diagrams.net skeemid ning GitHub Projects tahvel |
| CASE-vahendite võrdlus | `03-case-vahendid.md`: diagrams.net ja PlantUML |
| Kaitsmisel muudetav skeem | `diagrams/arhitektuur.drawio` ja `diagrams/andmemudel.drawio` |
| Rakenduse tüüp, arhitektuur, andmevoog ja alternatiiv | `04-arhitektuur.md` |
| GitHubi repositoorium ja vähemalt viis sisulist commit'i | Repositooriumi tegelik commit'ide ajalugu |
| SemVer-i plaan ja näited | `05-git-ja-versioonid.md` |

## Võimalikud küsimused

**Miks pole õpetaja rolli?** Esimese versiooni eesmärk on minu isiklik planeerimine. Õpetaja töövoog suurendaks ulatust ning pole põhivajaduse jaoks vajalik.

**Miks Kanban, mitte Scrum?** Ühe arendaja pidevat töövoogu saab jälgida lihtsa tahvli ja tööpiiranguga. Scrum sobiks kindla koostöörütmiga meeskonnale, kuid vajaks rollide ja sündmuste korraldust.

**Mis siis, kui soovitakse teavitusi?** Lisan loo, täpsustan kanali ja ajastuse ning hindan mõju. Meiliteavitused nõuaksid täiendavat ajastajat ja teenust; need ei ole praeguse esimese versiooni osa.

**Kuidas hoiad andmed isiklikuna?** Kõik päringud piiratakse sessioonis oleva kasutaja ainetega; ka otse URL-iga saadetud lugemis- ja muutmispäringud kontrollivad omanikku.

**Mida tõendavad commit'id?** Need näitavad kavandi sisulist kujunemist. Need ei tõenda veel, et kavandatud rakendus on arendatud.

## Enne esitamist

- Lisa README-sse enda tegelik näide ja veendu, et oskad kõiki valikuid oma sõnadega seletada.
- Kontrolli repositooriumi ja projektitahvli ligipääsu õpetajale.
- Harjuta `.drawio` skeemi avamist, muutmist ja salvestamist.
- Näita vähemalt viie commit'i sisu, mitte ainult nende arvu.
