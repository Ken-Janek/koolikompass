# Kaitsmise kava ja nõuete kontroll

Tegelikud tõendid: [repositoorium](https://github.com/Ken-Janek/koolikompass), [avalik projektitahvel](https://github.com/users/Ken-Janek/projects/1) ja [commit'ide ajalugu](https://github.com/Ken-Janek/koolikompass/commits/main/). Tahvli olekud on inglise keeles: Ready = valmis alustamiseks, In progress = töös, In review = kontrollimisel, Done = valmis.

## Kaitsmise tegelik formaat: 15–20 minutit

Õpetaja valib projekti otsused ja ootamatu muudatuse. See pole ainult ettevalmistatud esitlus: vaja on avada töövahendid, muuta lahendust ja põhjendada mõju. [Praktilised harjutused ja teadmiste kontroll](07-praktiline-kaitsmine.md) aitavad valmistuda.

| Osa | Aeg | Mida näitan |
|---|---:|---|
| A. Projekti selgitamine | 5 min | Õpetaja valitud otsuste põhjendus ja tõend dokumendis, skeemil või tahvlil |
| B. Ootamatu muudatus | 10 min | Muudetud skeem või backlog, mõju ulatusele ja arendusele ning muudatuse kontroll |
| C. Teadmiste kontroll | 5 min | Mõistete rakendamine oma projekti näidetega |

## Projekti selgitamise 5-minutiline harjutus

1. **Idee, 30 sekundit.** „KooliKompass on õppeülesande jaoks koostatud kooliülesannete ja tähtaegade planeerija kavand.“ Näita põhifunktsioone.
2. **Protsess, 45 sekundit.** Selgita etappe ja võrdle koskmudelit iteratiivse mudeliga. Too nädalakalendri lisamise näide nõuete muutumisest.
3. **Kanban, 1 minut.** Ava tegelik GitHub Projects tahvel, näita kaheksat lugu, prioriteete, US-03 sõltuvust ning esimese perioodi 20 tunni plaani. Selgita poolelioleva töö piirangut.
4. **CASE, 30 sekundit.** Näita diagrams.net-is avatud `.drawio` faili. Võrdle visuaalset redaktorit PlantUML-i tekstikirjeldusega; praktilist muudatust harjuta eraldi B-osas.
5. **Arhitektuur, 1,5 minutit.** Jälgi skeemil ülesande lisamise teekonda brauserist andmebaasi ja tagasi. Põhjenda monoliiti võrreldes mikroteenustega. Näita andmemudeli seoseid.
6. **Git, 45 sekundit.** Ava GitHubi commit'ide ajalugu ja üks sisuline muudatus. Too PATCH-, MINOR- ja MAJOR-näide. Ütle, et tag märgistab täpse väljalaske commit'i.

See ajajaotus on harjutamiseks. Kaitsmisel vasta õpetaja küsimusele otse ja näita vastavat osa; kõiki punkte ei pruugi järjest ette kanda.

## Hindamise järgi valmistumine

| Hinnatav osa | Osakaal | Harjutuse tulemus |
|---|---:|---|
| Kavand ja nõuete täitmine | 25% | Leian kõik nõutud materjalid repositooriumist |
| Valikute põhjendamine | 25% | Selgitan valiku põhjust, alternatiivi ja puudust oma projekti näitel |
| Ootamatu praktiline muudatus | 35% | Muudan ise skeemi või tahvlit ja kontrollin lahenduse kooskõla |
| Teadmiste kontroll | 15% | Vastan küsimustele ning toon rakendamise näite |

Kõik neli õpiväljundit tuleb eraldi tõendada. Valmis dokumendid ei asenda iseseisvat muutmist ega arusaamist. Harjutamisel pööra enim aega praktilisele muudatusele, kuid kontrolli iga osa eraldi.

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

**Miks pole õpetaja rolli?** Esimene versioon keskendub õpilase ülesannete planeerimisele. Õpetaja töövoog suurendaks ulatust.

**Miks Kanban, mitte Scrum?** Ühe arendaja pidevat töövoogu saab jälgida lihtsa tahvli ja tööpiiranguga. Scrum sobiks kindla koostöörütmiga meeskonnale, kuid vajaks rollide ja sündmuste korraldust.

**Mis siis, kui soovitakse teavitusi?** Lisan loo, täpsustan kanali ja ajastuse ning hindan mõju. Meiliteavitused nõuaksid täiendavat ajastajat ja teenust; need ei ole praeguse esimese versiooni osa.

**Kuidas hoiad andmed isiklikuna?** Kõik päringud piiratakse sessioonis oleva kasutaja ainetega; ka otse URL-iga saadetud lugemis- ja muutmispäringud kontrollivad omanikku.

**Mida tõendavad commit'id?** Need näitavad kavandi sisulist kujunemist. Need ei tõenda veel, et kavandatud rakendus on arendatud.

## Enne esitamist

- Veendu, et oskad kõiki valikuid oma sõnadega seletada.
- Kontrolli repositooriumi ja projektitahvli ligipääsu õpetajale.
- Harjuta `.drawio` skeemi avamist, muutmist ja salvestamist.
- Näita vähemalt viie commit'i sisu, mitte ainult nende arvu.
