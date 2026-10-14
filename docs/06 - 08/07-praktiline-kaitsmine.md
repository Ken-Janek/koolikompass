# Individuaalse praktilise kaitsmise harjutused

Need on võimalikud lahenduskäigud, mitte ette teada õpetaja vastused. Harjutus ei muuda projekti praegust ulatust ega tegeliku tahvli kaheksat lugu. Kaitsmisel lähtu õpetaja antud tingimustest ja tee muudatus ise.

## A. Kuidas oma valikut põhjendada

Kasuta vastamisel nelja sammu: **vajadus → valik → alternatiiv → puudus või kontroll**.

| Küsimus | KooliKompassi põhjendus |
|---|---|
| Miks iteratiivne arendus? | Nimekirja kasutusmugavus selgub proovikasutusel. Teen esmalt väikese töötava osa ja täpsustan järgmisi osi tagasisidega. Koskmudel sobiks stabiilsete nõuete korral; iteratiivne töö vajab ulatuse pidevat kontrolli. |
| Miks Kanban? | Üks arendaja saab võtta järgmise olulisima valmis töö. Piir üks töös olev kaart aitab lõpetada alustatu. Scrum korraldaks töö sprintide, rollide ja kindlate sündmustega; Kanbanis pean ise regulaarselt prioriteete ja takistusi üle vaatama. |
| Miks kihiline monoliit? | Kontod, ained ja ülesanded moodustavad väikese seotud terviku. Ühe serverirakenduse avaldamine ja tehingud on lihtsad. Mikroteenused annaksid eraldi skaleerimise võimaluse, kuid lisaksid võrguühendused ja mitme teenuse haldamise. |
| Milleks CASE-vahendid? | diagrams.net teeb komponendid ja seosed nähtavaks ning muudetavaks. GitHub Projects näitab tööde järjekorda ja olekut. Skeem aitab avastada puuduva ühenduse, tahvel täitmata sõltuvuse; kumbki ei tõenda automaatselt programmi õigsust. |
| Kuidas andmed liiguvad? | Vorm → HTTPS-päring → sessiooni ja sisestuse kontroll → äriloogika → ORM → PostgreSQL. Nimekirjapäring loeb enda andmed, mall teeb HTML-i ja brauser kuvab tulemuse. Serveri kihtide vahel on funktsioonikutsed. |
| Mis juhtub uue nõudega? | Täpsustan vajaduse, kirjutan loo ja kriteeriumid, hindan sõltuvusi ning mõju ajale. Uuendan prioriteete ja lepin ulatuse kokku. Pooleli töö ei muutu valmis tööks pelgalt sellepärast, et plaan muutus. |

## B. Üldine 10 minuti töövõte

| Minutid | Tegevus |
|---|---|
| 0–1 | Täpsusta üks-kaks otsustavat tingimust; korda uut eesmärki oma sõnadega. |
| 1–2 | Leia mõjutatud komponendid, lood ja sõltuvused. Sõnasta oma eeldus, kui mõni detail pole antud. |
| 2–6 | Muuda vajalikku skeemi või tegelikku projektitahvlit. Näita nii muudatust kui ka selle põhjendust. |
| 6–8 | Selgita taaskasutust, uut tööd, prioriteete ja mõju ajakavale. |
| 8–10 | Kontrolli seoseid ja kriteeriume, salvesta skeem, näita tulemust ning võimalusel salvesta sisuline Git-muudatus. |

Enne harjutust ava [tahvel](https://github.com/users/Ken-Janek/projects/1) ja arhitektuuriskeem diagrams.net-is. Kohaliku faili puhul kasuta File → Open From → Device. Harjutusskeem salvesta eraldi nimega, näiteks `arhitektuur-mobiil-harjutus.drawio`. Kui harjutad päris tahvlil, märgista ajutised kaardid „HARJUTUS“ ja taasta pärast harjutust algsed prioriteedid.

### Olukord 1: lisaks veebile soovitakse mobiilirakendust

**Täpsustus:** kas klient vajab telefonis toimivat veebivaadet või eraldi paigaldatavat rakendust? Praegune kohanduv veebivaade töötab juba telefonis. Kui nõutakse eraldi rakendust, ei piisa ainult selle nimetamisest mobiilivaateks. Allolev näide eeldab eraldi Androidi/iOS-i klienti ja internetiühendust.

**Skeemimuudatus diagrams.net-is:**

1. Lisa brauseri kõrvale komponent „Mobiilirakendus“.
2. Lisa olemasoleva Django serveri piirjoone sisse „API päringukiht: JSON“. See on monoliidi osa, mitte uus mikroteenus.
3. Ühenda mobiiliklient API-kihiga: „HTTPS, JSON, autentimine“. Ühenda API-kiht olemasoleva äriloogikaga: „Funktsioonikutsed / tulemus“.
4. Säilita brauseri senine HTML-päringute tee ning ühine ORM ja andmebaas. Mobiiliklient ei ühendu otse andmebaasiga.

**Taaskasutus:** kontoandmed, õppeainete ja ülesannete ärireeglid, ORM, andmebaas ning migratsioonid. Uus klient saab eraldi kasutajaliidese; serveri HTML-malle ei saa automaatselt kasutada mobiilikliendi ekraanidena. Näiteks Django REST Framework võib toetada API loomist; mobiilikliendi jaoks võiks kaaluda Flutterit. Tehnoloogia valik sõltub arendaja oskusest ja nõutud platvormidest.

**Näidiskaardid, mille õpetaja nõude korral tahvlile lisada:**

| ID | Uus töö | Prioriteet | Sõltuvus ja vastuvõtt |
|---|---|---|---|
| US-09 | Õpilasena soovin mobiilis turvaliselt sisse logida, et pääseda ligi enda töödele. | P1 uue mobiiliulatuse sees | Sõltub US-01-st. Vale autentimine ei anna ligipääsu; väljalogimine tühistab mobiilikliendi ligipääsu. |
| US-10 | Mobiilikliendi kasutajana soovin lugeda ja lisada enda ülesandeid API kaudu. | P1 uue mobiiliulatuse sees | Sõltub US-02, US-03 ja US-09-st. JSON-päring salvestub; vigane sisestus annab vea; teise kasutaja tööle ligipääs on keelatud. |
| US-11 | Õpilasena soovin mobiilis ülesannete nimekirja ja lisamise ekraani. | P1 uue mobiiliulatuse sees | Sõltub US-10-st ja nimekirja loogikast US-04-s. Lisatud ülesanne on nähtav nii veebis kui ka mobiilis. |
| T-12 | Kontrollida veebi ja mobiili ühist töövoogu ning võõraste andmete kaitset. | P1 | Tehniline kontrolltöö. Mõlemad kliendid järgivad samu ärireegleid ja näitavad salvestatud muudatusi. |

Kirjelduses lisa platvorm, kriteeriumid ja sõltuvused; maht hinda pärast täpsustamist, mitte suvalise arvu põhjal. API ja mobiili autentimine vajavad täiendavat kavandamist: tokenite kasutamisel on vaja turvalist hoiukohta, aegumist ja tühistamist. Veebi sessiooni- ja CSRF-kaitse jääb alles.

**Mõju protsessile:** uus nõue lisab tööd API, mobiilivaadete ja kontrollidega. Planeerin esmalt ühe tervikliku töövoo „mobiilis lisa → veebis näe“. Kui tähtaeg ei muutu, tuleb mõni teine funktsioon edasi lükata või muuta mobiili esimese väljalaske ulatust. Põhifunktsioonide testimine ja õiguste kontroll jäävad kohustuslikuks.

**Enesekontroll:** oskad näidata, milline kast on uus, millised jäävad samaks ja miks server võib endiselt olla monoliit?

### Olukord 2: tähtaeg lüheneb poole võrra

**Eeldus:** muudatus tuleb arenduse alguses. Kuus nädalat muutub kolmeks ja 10 tundi nädalas tähendab 30 tundi. Kui osa aega on juba kulunud, arvuta allesjäänud võimekus eraldi ning arvesta tegelikult valmis töid.

**Uus minimaalne versioon:** konto, õppeained, ülesande lisamine, tähtaja järgi nimekiri ja tehtuks märkimine. Need moodustavad kasutatava põhiteekonna.

| Lugu | Uus prioriteet | Otsus |
|---|---|---|
| US-01–US-05 | P1 | Esimesse versiooni; sõltuvuste järjekord säilib |
| US-06 | P2 | Muutmine ja kustutamine järgmisse väljalaskesse; kasutajale tuleb piirang selgitada |
| US-07 | P3 | Filtrid hiljem |
| US-08 | P3 | Kalendrivaade hiljem |

Lugude US-01–US-05 maht on 6 + 3 + 5 + 4 + 2 = **20 h**, sealhulgas lugude enda kontrollid. Lisaks kavandan keskkonna 2 h, ühise demonstratsiooni 1 h, puhvri 3 h ja proovikasutuse/kasutuselevõtu 4 h: kokku **30 h**. Viimane 4 h on selle harjutuse uus esialgne hinnang. See on prognoos, mitte garantii; kui uus hinnang ei mahu, tuleb veel ulatust või tähtaega läbi rääkida.

**Praktiline muudatus tahvlil:** ava US-06 ja muuda Priority väärtuseks P2; US-07 puhul P3; US-08 jääb P3. Uuenda nende pealkirjades ja kirjeldustes samuti prioriteet ning väljalaskeplaan, et need ei läheks väljaga vastuollu. Ära vii edasi lükatud lugusid Done-veergu. Märgi esimese väljalaske sisu tahvli kirjelduses ja dokumentides.

**Kanbani abi:** valin järgmise kõige olulisema töö, piiran pooleliolevat tööd ja vaatan prognoosi lõpetatud lugude põhjal üle. Kanban ei tee töid iseenesest kaks korda kiiremaks. Konto turvalisust, andmete eraldatust ja põhiteekonna kontrolli ei jäeta ajasurve tõttu ära.

**Enesekontroll:** kas muudetud esimene versioon täidab ikka ülesannete planeerimise põhieesmärki ning ajakavas on lisaks funktsioonidele aega avaldamiseks?

### Olukord 3: kasutajaid tuleb sada korda rohkem

**Täpsustus:** sada korda rohkem registreeritud kasutajaid ei tähenda tingimata sada korda rohkem samaaegseid päringuid. Küsi tipptunni aktiivsete kasutajate, päringusageduse ja andmemahu kohta. Ilma mõõtmiseta ei saa öelda, milline komponent esimesena piirab.

| Võimalik pudelikael | Mida kontrollida | Võimalik muudatus |
|---|---|---|
| Django server | CPU, mälu, töötajate arv, vastuseaeg ja vead | Optimeeri töötlust; vajadusel mitu sama monoliidi eksemplari |
| PostgreSQL | Aeglased päringud, lukud, ühenduste arv ja päringuplaan | Piira tagastatavat andmemahtu, paranda päringuid ja lisa mõõdetud vajadusega indekseid |
| Kasvav ülesannete nimekiri | Kas iga vaade loeb kõik tööd? | Lehekülgede kaupa laadimine ja vajalikud filtrid |
| Staatilised failid | Kas CSS-i ja muid faile teenindab rakenduse server? | Eraldi staatiliste failide teenindamine ja vahemälu |

**Üks võimalik skeemimuudatus:** lisa klientide ja Django vahele „Koormusjaotur“. Näita selle taga „Django eksemplar A“ ja „Django eksemplar B“, mõlemad sama kihilise monoliidi koopiad. Mõlemad ühenduvad ühise PostgreSQL-iga. Kui serverid peavad olema vahetatavad, hoia sessioonid ühises andmebaasis või selleks sobivas ühises hoidlas. Kohaliku mälu sessioon ei saa olla ainus sessiooni allikas. Staatiliste failide teenindaja võib olla eraldi.

**Piirang:** kaks serverikoopiat ei kõrvalda andmebaasi pudelikaela. Näiteks võib uurida ülesannete päringu jaoks indeksit `(õppeaine_id, olek, tähtaeg, id)`, kuid selle kasu tuleb kontrollida päringuplaaniga; üle mitme õppeaine järjestamisel võib endiselt olla vaja sortimist. Ühenduste arvu tuleb piirata. Isiklike vaadete vahemälu puhul peab võti sisaldama kasutajat, et andmeid mitte segada.

**Miks mitte kohe mikroteenused?** Kasutajate arvu kasv ei tõenda vajadust jagada süsteem eraldi teenusteks. Sama monoliidi mitme eksemplari kasutamine võib olla lihtsam. Mikroteenuseid kaalun mõõdetud kitsaskoha ja iseseisva vastutuse korral.

**Kontrollplaan:** kasuta sünteetilisi andmeid ja sihtkoormust, mõõda enne/pärast näiteks p95 vastuseaega, veaprotsenti ning andmebaasi koormust. Sihtväärtused lepi kokku; ära väida ilma testita, et lahendus teenindab kindlasti uut kasutajate hulka. Lisa koormustest ja valitud muudatused backlog'i.

**Enesekontroll:** oskad selgitada, miks kaks Django kasti ei tähenda mikroteenuseid ja mis juhtub, kui andmebaas jääb aeglaseks?

## C. Teadmiste kontroll

Proovi esmalt vastata ilma allolevat veergu lugemata. Lisa igale vastusele üks KooliKompassi näide.

| Küsimus | Vastuse kontrollpunkt |
|---|---|
| Koskmudel ja iteratiivne mudel? | Koskmudel liigub peamiselt järjestikuste etappidena; iteratiivses mudelis täpsustatakse lahendust korduvates arendusosades. KooliKompassis aitab varajane nimekirjavaate tagasiside järgmisi osi muuta. |
| Scrum ja Kanban? | Scrum kasutab kuni ühekuulisi sprinte, määratletud vastutusi ja sündmusi; Kanban keskendub nähtavale töövoole, tööpiirangutele ja voo parandamisele. Kanban ei keela perioodilist planeerimist ning Scrum ei välista töövoo piiranguid. |
| Milleks CASE? | Nõuete, disaini ja arendustegevuste toetamiseks; siin aitab skeem seoseid muuta ja tahvel sõltuvusi jälgida. Töövahend ei tee arhitektuurivalikut arendaja eest. |
| Monoliit ja mikroteenused? | Monoliit avaldatakse ühe tervikuna; mikroteenuste teenuseid saab iseseisvalt avaldada, kuid nende suhtlus ja haldus on keerukamad. Kihilisus kirjeldab vastutuste eraldamist ja võib esineda mõlemas. |
| Miks Git-harud? | Muudatust saab teha eraldi main-haru stabiilsest seisust, üle vaadata ja seejärel liita. Haru ei taga ise testide läbimist ega kõrvalda liitmiskonflikte. |
| Mis on commit, push ja tag? | Commit salvestab kohaliku muudatuse; push saadab commit'id kaugserverisse; tag nimetab konkreetse ajaloo punkti, näiteks väljalaske. |
| Versioon 2.4.1: veaparandus? | **2.4.2**, kui avalik liides jääb tagasiühilduvaks. |
| Versioon 2.4.1: uus tagasiühilduv funktsioon? | **2.5.0**; PATCH lähtestub. |
| Versioon 2.4.1: avalikku API-t lõhkuv muudatus? | **3.0.0**; MINOR ja PATCH lähtestuvad. Need kolm vastust lähtuvad igaüks algversioonist 2.4.1. |

## Iseseisev proovikaitsmine

1. Pane taimer 20 minutiks. Vali juhuslikult üks B-olukord ja ära loe lahendust enne muutmist.
2. Selgita viie minutiga õpetaja rollis küsitud otsuseid. Näita iga vastuse juures päris faili või töövahendit.
3. Tee kümne minutiga muudatus. Kontrolli, et skeem, tööde prioriteedid ja selgitus ei oleks omavahel vastuolus.
4. Vasta viie minutiga kuuele C-küsimusele, sealhulgas ühele versiooniküsimusele.
5. Kui vajad vastuse jaoks ettevalmistatud teksti, korda seda osa uue variandiga: näiteks mobiilikliendile nõutakse võrguühenduseta kasutust või ülesandeid hakatakse sõpradega jagama. Too välja uus mõju, mida algses näites polnud.

Lõplik kontroll: kas leiad materjalid, põhjendad otsuseid, muudad lahendust ja rakendad mõisteid iseseisvalt? Iga osa on vajalik; kõrge üldpunktisumma ei asenda puuduvat õpiväljundit.

## Täpsustuste allikad

Scrumi sprintide, vastutuste ja sündmuste kirjeldus lähtub [Scrum Guide'ist](https://scrumguides.org/scrum-guide.html). API-vahendi võimalusi saab kontrollida [Django REST Frameworki dokumentatsioonist](https://www.django-rest-framework.org/). Ühise sessioonihoidla valikuid kirjeldab [Django sessioonide juhend](https://docs.djangoproject.com/en/5.2/topics/http/sessions/); serveri kohalik mälu ei sobi ühise sessiooniallika rolli. Versiooninumbrite reeglid on [SemVer 2.0.0 spetsifikatsioonis](https://semver.org/).

Harjutuste ulatuse vähendamine, tööde järjestus ja skaleerimisvariant on selle projekti kavandamise näited; allikad ei kinnita nende ajahinnanguid ega koormustaluvust.
