# Projekti kavand ja teostus

## Eesmärk ja ulatus

KooliKompass aitab õpilasel hoida enda koolitöid ja tähtaegu ühes kohas. Õpilane loob konto, lisab ained ja ülesanded ning märgib tööd tehtuks. Õpetaja rolli ja kooli infosüsteemiga ühendust pole. Edukuse siht on, et kolm proovikasutajat lisavad ülesande, leiavad lähima tähtaja ja märgivad töö tehtuks, iga tegevus alla minuti. Seda proovikasutust pole veel tehtud.

## Arendusprotsess

| Etapp | Eesmärk ja tegevus |
| --- | --- |
| Vajaduste uurimine | Täpsustada õpilaste probleemi ja esimese versiooni ulatust |
| Nõuded | Kirjutada kasutajalood, prioriteedid ja kontrollitavad kriteeriumid |
| Kavandamine | Valida tehnoloogiad ning kirjeldada komponendid ja andmeseosed |
| Teostus | Arendada väikeste terviklike töövoogudena |
| Testimine | Kontrollida töövoogu, sisendit, andmete eraldatust ja kasutajaliidest |
| Kasutuselevõtt | Proovikeskkond, tagasiside, varundus ja avaldamine |
| Hooldus | Vigade parandamine, sõltuvuste uuendamine ja taastamise kontroll |

Valitud on **iteratiivne ja inkrementaalne arendus**: esmalt konto → aine → ülesanne, seejärel nimekiri, muutmine ja lisavaated. Iga osa läbib kontrolli. **Koskmudel** läbib etappe peamiselt järjest ning sobib stabiilsete nõuetega tööle; selle risk on hiline tagasiside. Iteratiivne mudel lubab vaadet proovikasutuse järel täpsustada, kuid nõuab ulatuse kontrollimist.

Uue nõude puhul täpsustan vajaduse, lisan loo ja kriteeriumid, hindan mõju sõltuvustele, skeemidele, testidele ja ajale ning uuendan plaani. Sama tähtaja korral tuleb vähem oluline töö edasi lükata. Andmete lekkimise vea lahendan enne mugavusfunktsioone.

## Kanban ja kasutajalood

Ühe arendaja töövoog on **Backlog → Ready → In progress → In review → Done**. Töös ja kontrollimisel võib olla kummaski üks kaart. Iga töökorra järel uuendan olekut, kord nädalas prioriteete ja hinnanguid. Kanban ei nõua Scrumi rolle ega sprinte; kahe nädala plaan on prognoos.

Alustamisvalmis lool on selge vajadus, prioriteet, kriteeriumid ja täidetud sõltuvused. Valmis lugu vastab kriteeriumidele, läbib vajalikud kontrollid ning on salvestatud Git-i koos vajaliku dokumentatsiooniga.

P1 = vajalik, P2 = mugavus, P3 = hilisem täiendus. Allpool on algsed hinnangud koos kontrollidega; kõik kaheksa funktsiooni on praeguses rakenduses teostatud.

| ID | Õpilase soov | Prioriteet | Tundi | Sõltub | Vastuvõtukriteeriumid |
| --- | --- | --- | ---: | --- | --- |
| US-01 | Luua konto ning sisse ja välja logida | P1 | 6 | — | Korduv nimi ja vale parool annavad vea; väljalogitud kasutaja ei pääse töölauale; võõrad andmed on kaitstud |
| US-02 | Lisada õppeaine | P1 | 3 | US-01 | Nimi on kohustuslik ja ühe omaniku piires unikaalne; teisel kasutajal võib olla sama nimi |
| US-03 | Lisada tähtajaga ülesanne | P1 | 5 | US-02 | Pealkiri, enda aine ja kehtiv tähtaeg on kohustuslikud; töö säilib värskendamisel; mineviku tähtaeg on lubatud |
| US-04 | Näha tegemata töid tähtaja järjekorras | P1 | 4 | US-03 | Ainult enda tööd, järjestus tähtaja ja ID järgi; hilinemine ja tühi nimekiri on selgitatud |
| US-05 | Märkida töö tehtuks ja taastada | P1 | 2 | US-04 | Töö liigub vastavasse olekuvaatesse ning olek säilib värskendamisel |
| US-06 | Muuta ja kustutada enda tööd | P1 | 3 | US-03 | Muudatus salvestub; kustutamine vajab kinnitust; tühistamine säilitab töö; võõra töö muutmine on keelatud |
| US-07 | Filtreerida aine ja oleku järgi | P2 | 3 | US-04, US-05 | Filtrid töötavad eraldi ja koos; neid saab eemaldada; tulemusteta otsingul on selgitus |
| US-08 | Vaadata nädala tähtaegu | P3 | 5 | US-04 | Seitse päeva, nädala vahetamine ja enda tööd õigel päeval Eesti ajas |

[Tegelik GitHub Projects tahvel](https://github.com/users/Ken-Janek/projects/1) sisaldab kaartidel kriteeriume ja sõltuvusi ning Priority ja Estimate välju. Periood on kirjelduses. Kohalik [backlog.json](../planning/backlog.json) hoiab lugude andmeid; see ei impordi tahvlit automaatselt. Oleku Done kirje ei asenda funktsiooni kontrollimist.

## Esialgne ajakava ja riskid

Eeldus: üks arendaja, kuus nädalat, 10 tundi nädalas. Nädal 1: nõuded ja kavand; nädalad 2–3: konto, ained ja lisamine; nädal 4: nimekiri, olek ja muutmine; nädal 5: proovikasutus ja parandused; nädal 6: kasutuselevõtt ja varundus.

Esimese kahe nädala 20 tunni plaan: keskkond 2 h, US-01 6 h, US-02 3 h, US-03 5 h, ühine demo 1 h ja puhver 3 h. Kui töö ei mahu, uuendan prognoosi ega märgi poolikut lugu valmis. Riskid on ulatuse kasv, ebatäpsed hinnangud ja andmekadu; abinõud on prioriteedid, puhver, varundus ja taastamise proovimine.

## Arhitektuur ja andmemudel

Kohanduv Django veebirakendus on **kihiline monoliit**: vaated, vormide ärireeglid, mudelid ja HTML-mallid on loogiliselt eraldatud, kuid server avaldatakse ühe tervikuna. Monoliiti on ühel arendajal lihtne hallata ja andmetehingud on lihtsad. Puudus on kogu rakenduse koos skaleerimine ja ühine rikete mõju. Mikroteenused võimaldaksid osade sõltumatut avaldamist, kuid lisaksid võrguühendused, liidesed ja halduskoormuse.

Andmevoog: brauser → HTTP-päring → Django sessiooni-, CSRF- ja vormikontroll → ORM → andmebaas → suunamine nimekirjale → HTML-vastus. Tootmises kasutatakse HTTPS-i; kohalik arendusserver kasutab HTTP-d. Serveri kihtide vahel on funktsioonikutsed. Brauser andmebaasiga otse ei suhtle.

| Mudel | Andmed ja reeglid |
| --- | --- |
| Kasutaja | Django konto, kasutajanimi ja parooli räsi |
| Õppeaine | Omanik, nimi ja värv; nimi unikaalne omaniku piires |
| Ülesanne | Aine, pealkiri, kirjeldus, tähtaeg, tehtud-olek ja loomisaeg |

Kasutajal on mitu ainet ning ainel mitu tööd. Töö omanik leitakse aine kaudu. Ülesannetega aine kustutamist takistab PROTECT; kontode kustutamise töövoogu kasutajaliideses pole. Hilinemine arvutatakse tähtajast ja olekust. Ajavöönd on kogu rakenduses `Europe/Tallinn`; kasutaja muudetavat ajavööndiprofiili pole.

Vaikimisi kasutatakse SQLite'i. PostgreSQL-i ühendus on seadistatav, kuid selle vastu pole siinses keskkonnas teste käivitatud. [Käivitamine ja majutuse seadistus](../app/README.md).

Muudetavad algfailid: [arhitektuur](../diagrams/arhitektuur.drawio) ja [andmemudel](../diagrams/andmemudel.drawio). Need kujutavad kavandit; kohaliku teostuse andmebaasi ja ajavööndi täpsustused on ülal.

## CASE-vahendid

**diagrams.net** toetab komponentide ja seoste modelleerimist; **GitHub Projects** tööde planeerimist ja jälgimist. Git hoiab mõlema kõrval failide ajalugu. Skeem ei asenda tahvlit ja kumbki ei tõenda automaatselt programmi õigsust.

| diagrams.net | PlantUML |
| --- | --- |
| Visuaalselt liigutatavad kujundid ja ühendused | Tekstikirjeldusest renderdatav diagramm |
| Kaitsmisel mugav otse muuta | Git-is tavaliselt lihtsam muudatusi võrrelda |
| XML-i muudatus võib olla pikk | Paigutuse arvutab peamiselt renderdaja |

Valitud on diagrams.net, sest kaitsmisel saab komponente kiiresti lisada ja ümber paigutada. Avamine: File → Open From → Device, vali `.drawio`; muuda topeltklõpsuga teksti, lisa kast ja ühendus ning salvesta. Harjutuse salvesta eraldi koopiana.

## Git ja versioonid

[Repositoorium](https://github.com/Ken-Janek/koolikompass) · [commit'ide ajalugu](https://github.com/Ken-Janek/koolikompass/commits/main/).

Commit salvestab kohaliku seisu, push saadab selle kaugserverisse ja tag nimetab täpse ajaloo punkti. Suurema muudatuse jaoks sobib eraldi `feature/...` haru; enne liitmist kontrollin muudatust. `git status`, `git diff`, `git log --oneline` ja `git show <commit>` aitavad tulemust näidata. Saladused, kohalik andmebaas ja päris kasutajaandmed Git-i ei kuulu.

SemVer on MAJOR.MINOR.PATCH. Lähtudes igal juhul versioonist 2.4.1: tagasiühilduv veaparandus → 2.4.2; uus tagasiühilduv funktsioon → 2.5.0; avalikku lepingut lõhkuv muudatus → 3.0.0. Sisemine ümberkirjutus või migratsioon ei nõua iseenesest MAJOR-i.

Algne plaan: 0.1.0 kavand, 0.2.0 konto ja lisamine, 0.3.0 ülesannete haldus, 1.0.0-rc.1 proovikasutus ja 1.0.0 kontrollitud kasutuselevõtt. Praegune 0.3.0 sisaldab juba filtreid ja nädalavaadet, mis olid algselt plaanitud 1.1.0-sse. Väljalaske märgistan näiteks `v1.0.0` tag'iga; avaldatud versiooni parandamiseks teen uue numbri.

## Teostus ja kontrolltõendid

Rakendus asub [app-kaustas](../app/). Varasemal kontrollimisel läbisid 13 Django testi SQLite'i testandmebaasis, Django `check` ei leidnud vigu ning migratsioonide kontroll ei leidnud mudelimuudatusi. Testid katavad töövoo, autentimise, andmete eraldatuse, võõra aine tagasilükkamise, CSRF-i, filtrid, nädalapiirid, leheküljed ja HTML-i ohutu kuvamise.

Varasem brauserikontroll hõlmas sisselogimist, lisamist, tehtuks märkimist ja kalendrit ning 360 px telefoni nimekirja ja nädalavaadet. Need ei asenda kolme õpilase proovikasutust; tootmiskeskkonda avaldamist pole tehtud.

| Tõend | Sisu |
| --- | --- |
| [Algne tahvel](../evidence/kanban.jpg) | 7 backlog'i ja 1 alustamisvalmis kaart |
| [Valminud tahvel](../evidence/kanban-valmis.jpg) | Kaheksa lugu Done-veergu viidud |
| [Skeem redaktoris](../evidence/arhitektuur.jpg) | Muudetav arhitektuur diagrams.net-is |
| [Rakendus](../evidence/rakendus.jpg) | Nimekiri demoandmetega |
| [Telefonivaade](../evidence/rakendus-telefon.jpg) | 360 px laiune nimekiri |

Tootmise eel on vaja HTTPS-i, saladuste seadistust, staatiliste failide teenindamist, varundust, taastamise proovimist ja sisselogimiskatsete piiramist. Varunduse kavand: igapäevane koopia, seitse viimast alles ning taastamise proov enne pilooti ja kord kuus.

Allikad: [Django](https://docs.djangoproject.com/en/5.2/), [GitHub Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/creating-projects/creating-a-project), [diagrams.net](https://www.drawio.com/docs/manual/open-diagram-file/), [SemVer](https://semver.org/).
