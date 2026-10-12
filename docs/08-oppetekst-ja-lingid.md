# KooliKompassi õppetekst ja kaitsmisel avatavad lingid

Õpi mõtete järjekord ja põhjused, mitte ainult sõnastus. Allolev põhitekst on umbes viie minuti jaoks, kui räägid rahulikult ja näitad vahepeal materjale. Õpetaja küsimuse korral vasta sellele otse; kogu teksti ei pea järjest ette kandma.

## Ava enne kaitsmist need viis vahelehte

| Järjekord | Link | Milleks seda kasutan? |
|---|---|---|
| 1 | [Repositoorium ja README](https://github.com/Ken-Janek/koolikompass) | Projekti idee, materjalide asukohad ja õpetajale esitatav link |
| 2 | [GitHub Projects tööde tahvel](https://github.com/users/Ken-Janek/projects/1/views/1) | Kasutajalood, prioriteedid, hinnangud ja olekute muutmine |
| 3 | [Arhitektuuriskeem diagrams.net redaktoris](https://app.diagrams.net/#Uhttps%3A%2F%2Fraw.githubusercontent.com%2FKen-Janek%2Fkoolikompass%2Fmain%2Fdiagrams%2Farhitektuur.drawio) | Komponendid, andmete liikumine ja praktiline arhitektuurimuudatus |
| 4 | [Andmemudel diagrams.net redaktoris](https://app.diagrams.net/#Uhttps%3A%2F%2Fraw.githubusercontent.com%2FKen-Janek%2Fkoolikompass%2Fmain%2Fdiagrams%2Fandmemudel.drawio) | Kasutaja, õppeaine ja ülesande seosed |
| 5 | [Commit'ide ajalugu](https://github.com/Ken-Janek/koolikompass/commits/main/) | Sisuliste Git-muudatuste tõendamine |

Skeemide lingid avavad muudetava diagrammi, mitte ainult pildi. Veendu enne kaitsmist, et saad kuju valida ja teksti muuta. GitHubi toorfailist avatud diagrammi muutmine ei kirjuta seda automaatselt tagasi GitHubi: salvesta muudetud `.drawio` kohalikku projektikausta ja tee Git-muudatus. Kui küsitakse salvestuskohta, vali Device / Seade. Kohaliku algfaili saab avada ka File / Fail → Open From / Ava → Device / Seade kaudu.

Tahvli muutmiseks peab olema sisse logitud **Ken-Janek** kontoga. Avalikku tahvlit saab vaadata ka ilma muutmisõiguseta, kuid sellest praktiliseks kaitsmiseks ei piisa.

## 1. Projekti idee — umbes 30 sekundit

**Ava:** repositooriumi README. **Näita:** „Idee ja isiklik seos“ ning esimese versiooni eesmärk.

> Minu projekti nimi on KooliKompass. See on kooliülesannete ja tähtaegade planeerija. Valisin selle teema, sest õpilasena pean jälgima eri ainete ülesandeid ja nende tähtaegu. Rakenduse eesmärk on koondada need ühte kohta, et oleks lihtsam otsustada, mida järgmisena teha.
>
> Esimeses versioonis saaks kasutaja luua konto, lisada aineid ja ülesandeid, vaadata tööde tähtaegu ning märkida ülesandeid tehtuks. Ülesanded sisestab õpilane ise. Praegu olen koostanud arenduskavandi, mitte valmis rakenduse.

Kui tahad lisada isikliku näite, räägi ainult olukorrast, mis on sinuga päriselt juhtunud. Kavand ei tõenda veel, et rakendus oleks kasutajatega testitud.

## 2. Arendusprotsess — umbes 45 sekundit

**Ava vajaduse korral:** [arendusprotsessi kirjeldus](https://github.com/Ken-Janek/koolikompass/blob/main/docs/01-arendusprotsess.md). **Näita:** etappide ja mudelite võrdluse tabelit.

> Arendus algaks probleemi ja kasutajate vajaduste uurimisest. Seejärel määraksin nõuded, kavandaksin süsteemi, arendaksin funktsioonid ja kontrolliksin nende toimimist. Pärast proovikasutust tuleks rakenduse kasutuselevõtt ja hooldus.
>
> Valisin iteratiivse ja inkrementaalse arendusmudeli. See tähendab, et teeksin rakendust väikeste osadena ja parandaksin lahendust tagasiside põhjal. Näiteks saaks kõigepealt proovida ülesannete lisamist ja hiljem täiendada nimekirjavaadet.
>
> Koskmudelis liiguvad etapid peamiselt järjest ning see sobib paremini selgete ja stabiilsete nõuetega projektile. Minu projektis võivad kasutajate soovid proovimise käigus täpsustuda. Uue nõude korral hindaksin selle mõju ning muudaksin tööde plaani, selle asemel et lisada kõik sama tähtaja sisse.

## 3. Kanban ja tööde planeerimine — umbes 1 minut

**Ava:** tööde tahvel. **Näita:** US-01 kaarti Ready-veergu ning US-03 kaardi kirjeldust. Kaardi avamiseks klõpsa selle pealkirjal.

> Arendusmetoodikaks valisin Kanbani, sest kavandatud projekti arendaksin esialgu üksinda. Tahvlil on näha, millised tööd ootavad, millised on alustamiseks valmis, millised on töös, kontrollimisel või lõpetatud.
>
> Korraga võib töös olla üks kasutajalugu ja kontrollimisel üks. See aitab mul lõpetada alustatud töö enne järgmise võtmist. Kahe nädala plaan on tööprognoos, mitte Scrumi sprint.
>
> Mul on kaheksa kasutajalugu. P1 tähendab esimese versiooni jaoks vajalikku tööd, P2 olulist mugavust ja P3 hilisemat täiendust. Näiteks ülesande lisamine sõltub õppeaine lisamisest, mis omakorda sõltub kasutajakontost.
>
> Esimese kahe nädala eesmärk oleks konto, aine ja ülesande lisamine. Selleks olen planeerinud kokku 20 tundi koos keskkonna seadistuse, demonstratsiooni ja puhvriga. Töö saab valmis oleku alles siis, kui selle kriteeriumid ja vajalikud kontrollid on täidetud. Praegu ootavad rakenduse arenduslood teostust.

## 4. CASE-vahendid — umbes 30 sekundit

**Ava:** arhitektuuriskeem redaktoris. **Näita:** kujundeid ja ühendusi. Võrdluse lisalink: [CASE-vahendite kirjeldus](https://github.com/Ken-Janek/koolikompass/blob/main/docs/03-case-vahendid.md).

> Kavandamisel kasutasin diagrams.net-i ja GitHub Projectsi. Diagrams.net-is saan näidata süsteemi komponente ning muuta nende seoseid. GitHub Projectsis saan korraldada tööde järjekorda ja jälgida nende olekut.
>
> Võrdlesin diagrams.net-i ka PlantUML-iga. Diagrams.net-is muudan skeemi visuaalselt. PlantUML-is kirjutatakse diagrammi kirjeldus tekstina, mida on Git-is lihtsam võrrelda. Valisin diagrams.net-i, sest kaitsmisel on mul mugav komponente hiirega muuta ja ühendada.

## 5. Arhitektuur ja andmete liikumine — umbes 1,5 minutit

**Ava:** arhitektuuriskeem. **Näita rääkimise ajal:** brauser → Django päringukiht → äriloogika → ORM → PostgreSQL. **Seejärel ava:** andmemudel.

> KooliKompass oleks veebirakendus, mida saab kasutada arvuti ja telefoni brauseris. Serveri jaoks valisin Django ning andmebaasiks PostgreSQL-i. Veebivaade kasutaks HTML-malle ja CSS-i.
>
> Arhitektuur on kihiline monoliit. Server avaldatakse ühe tervikuna, kuid selle sees on erinevad vastutused eraldatud. Päringukiht võtab päringu vastu, äriloogika rakendab reegleid ja andmekiht suhtleb andmebaasiga.
>
> Kui õpilane lisab ülesande, saadab brauser vormiandmed HTTPS-päringuga serverisse. Server kontrollib sisselogimist, sisestatud andmeid ja seda, kas valitud aine kuulub kasutajale. Seejärel salvestab ORM ülesande PostgreSQL-i. ORM tähendab siin vahendit, millega programm saab andmebaasi lugeda ja kirjutada.
>
> Pärast salvestamist avatakse ülesannete nimekiri uuesti. Server loeb kasutaja ülesanded ja koostab neist HTML-vaate. Brauser ei suhtle andmebaasiga otse ning serveri sisemiste kihtide vahel pole HTTP-päringuid, vaid funktsioonikutsed.
>
> Andmemudelis võib ühel kasutajal olla mitu õppeainet ja ühel ainel mitu ülesannet. Ülesande omanik leitakse õppeaine kaudu. Nii kontrollin ka seda, et kasutaja ei pääseks ligi teiste töödele.
>
> Monoliit sobib väikesele projektile, sest seda on lihtsam arendada ja avaldada. Puudus on see, et serveri rike võib mõjutada kõiki funktsioone. Mikroteenustega saaks osi eraldi avaldada ja skaleerida, kuid lisanduks mitme teenuse haldamine. Praegune ulatus seda keerukust ei vaja.

## 6. Git ja versioonid — umbes 45 sekundit

**Ava:** commit'ide ajalugu. **Näita:** vähemalt viit eri sisuga commit'i; klõpsa näiteks skeemide lisamise commit'il ja näita muudetud faile. Lisalink: [versiooniplaan](https://github.com/Ken-Janek/koolikompass/blob/main/docs/05-git-ja-versioonid.md).

> Dokumendid ja muudetavad skeemid on GitHubi repositooriumis. Muudatused olen salvestanud eraldi sisuliste commit'idena. Git näitab, mis muutus, ning võimaldab varasemat seisu vaadata. Commit salvestab muudatuse kohalikku ajalukku ja push saadab selle GitHubi.
>
> Versiooniplaan järgib SemVer-i ehk MAJOR.MINOR.PATCH põhimõtet. Tagasiühilduv veaparandus tõstab viimast numbrit, uus tagasiühilduv funktsioon keskmist numbrit ja avalikku liidest lõhkuv muudatus esimest numbrit.
>
> Näiteks versioonist 2.4.1 saaks veaparandusega 2.4.2, uue tagasiühilduva funktsiooniga 2.5.0 või API-d lõhkuva muudatusega 3.0.0. Väljalaske täpse commit'i märgiksin Git-tag'iga ning GitHub Release'is kirjeldaksin muudatusi.

## Praktilise ülesande ajal: milline link avada?

| Õpetaja ülesanne | Ava | Tee ise | Mida selgita? |
|---|---|---|---|
| Lisada mobiilirakendus | Arhitektuuriskeem ja tööde tahvel | Lisa mobiiliklient ja serveri sisse API päringukiht; ühenda need äriloogikaga. Lisa uued API, autentimise, mobiilivaadete ja kontrollimise tööd. | Ühine äriloogika ja andmebaas jäävad kasutusse; mobiil saab oma vaated. Selgita mõju ajale ja ulatusele. |
| Tähtaeg poole lühem | Tööde tahvel ja backlog'i dokument | Muuda US-06 prioriteet P2-ks ja US-07 P3-ks; uuenda ka kaardi pealkirja ja kirjeldust. Esimesse versiooni jäta US-01–US-05. | Harjutuse eeldusel on 30 h: lood 20 h, muud tegevused ja puhver 10 h. Tegelik plaan sõltub juba tehtud tööst. |
| Sada korda rohkem kasutajaid | Arhitektuuriskeem ja tööde tahvel | Lisa koormusjaotur ja sama Django serveri kaks koopiat ühise andmebaasi ees; lisa koormuse mõõtmise töö. | Mõõda esmalt samaaegset koormust. Serveri koopiad ei kõrvalda automaatselt andmebaasi pudelikaela ega muuda süsteemi mikroteenusteks. |

Üksikasjalikud kriteeriumid ja harjutuskäigud: [praktilise kaitsmise harjutused](https://github.com/Ken-Janek/koolikompass/blob/main/docs/07-praktiline-kaitsmine.md).

**Kui mõte läheb kinni, alusta nii:** „Kõigepealt täpsustan uut nõuet. Seejärel vaatan, milliseid komponente ja töid see mõjutab. Teen muudatuse skeemis või tahvlil ning selgitan mõju ajakavale ja kontrollimisele.“

### Lühike õppetekst mobiilirakenduse olukorraks

> Kõigepealt küsin, kas vaja on telefonis toimivat veebivaadet või eraldi paigaldatavat rakendust. Eraldi mobiilirakenduse jaoks lisaksin serverile API-kihi. API on liides, mille kaudu mobiilirakendus saab serveriga andmeid vahetada. Mobiiliklient saadaks HTTPS-i kaudu JSON-andmeid. Olemasolev äriloogika ja andmebaas jääksid ühised, aga mobiili kasutajaliides tuleb eraldi teha. Tahvlile lisaksin autentimise, API, mobiilivaadete ja testimise tööd ning hindaksin, mida tuleb tähtaja hoidmiseks edasi lükata.

### Lühike õppetekst lühema tähtaja olukorraks

> Tähtaja lühenemisel arvutan kõigepealt allesjäänud tööaja. Kõiki funktsioone ei saa lihtsalt kaks korda kiiremini valmis teha. Jätan esimesse versiooni konto, ained, ülesande lisamise, nimekirja ja tehtuks märkimise. Muutmine, kustutamine, filtrid ja kalender lähevad hilisemaks. Muudan tahvlil prioriteete ning uuendan kirjeldusi. Kanban aitab valida järgmise olulisima töö ja piirata pooleliolevat tööd, kuid vajalik kontrollimine jääb alles.

### Lühike õppetekst suurema koormuse olukorraks

> Sada korda rohkem kasutajaid ei ütle veel, kui palju päringuid tuleb korraga. Mõõdaksin serveri ja andmebaasi koormust ning aeglaseid päringuid. Kui rakenduse server on pudelikael, võiks koormusjaoturi taga töötada sama monoliidi mitu koopiat. Neil oleks ühine andmebaas ja ühine sessioonide hoidmine. Kui aeglane on andmebaas, tuleb parandada päringuid ja kontrollida indeksite vajadust. Ma ei läheks ainult kasutajate arvu tõttu kohe mikroteenustele üle.

## Teadmiste kontrolli lühivastused

Teadmiste kontrollis selgita ise; eraldi veebilehte ei pea avama, kui õpetaja seda ei küsi.

- **Koskmudel või iteratiivne arendus?** Koskmudel läbib etapid peamiselt järjest. Iteratiivses arenduses korratakse tegevusi ja täpsustatakse lahendust väikeste osadena.
- **Arendusmudel või metoodika?** Mudel kirjeldab arenduse üldist kulgu; metoodika aitab korraldada igapäevast tööd. Minul on iteratiivne mudel ja Kanban.
- **Scrum või Kanban?** Scrum korraldab töö sprintides määratletud vastutuste ja sündmustega. Kanban keskendub nähtavale töövoole ning poolelioleva töö piiramisele.
- **CASE-vahend?** Tarkvaraarendust toetav töövahend. Minu skeemiredaktor aitab süsteemi kavandada ja projektitahvel töid planeerida.
- **Monoliit või mikroteenused?** Monoliit avaldatakse ühe tervikuna. Mikroteenuste teenuseid saab iseseisvalt avaldada, kuid nende suhtlus ja haldus on keerukamad.
- **Miks Git-haru?** Saan muudatuse teha eraldi main-harust, seda kontrollida ja seejärel liita.
- **Miks testimine?** Kontrollin, kas funktsioon vastab kriteeriumidele ja kas muudatus rikkus midagi. Näiteks testiksin, et üks kasutaja ei saa teise ülesannet muuta.
- **2.4.1 + veaparandus?** 2.4.2.
- **2.4.1 + tagasiühilduv uus funktsioon?** 2.5.0.
- **2.4.1 + API-d lõhkuv muudatus?** 3.0.0.

## Viimane harjutus enne kaitsmist

Loe põhitekst üks kord läbi, seejärel sulge see. Ava viis töövahelehte ja räägi ainult nende põhjal. Vali üks praktiline olukord ning tee muudatus kümne minutiga. Salvesta harjutusskeem eraldi failina. Kui harjutad päris tahvlil, taasta pärast algsed prioriteedid ja eemalda või arhiveeri selgelt märgistatud harjutuskaardid.

AI kasutamise kohta võid öelda: „Kasutasin AI-d kavandi, selgituste ja skeemide koostamisel. Kaitsmisel näitan, et mõistan valikuid ja oskan neid ise muuta.“ Seda viimast osa saad tõendada oma tegevusega.
