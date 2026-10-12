# 4. Tarkvaraarhitektuur

## Rakenduse tüüp ja tehnoloogiad

Valin veebirakenduse, mida saab kasutada telefoni ja arvuti brauseris. Eraldi mobiilirakendust ei pea paigaldama ning ühe paranduse avaldamine jõuab kõigi kasutajateni.

Valin kihilise monoliidi: kasutajaliides, päringute käsitlemine, ärireeglid ja andmetele ligipääs on loogiliselt eraldatud, kuid serverirakendus avaldatakse ühe tervikuna. PostgreSQL on eraldi andmebaas, mitte eraldi äriloogika mikroteenus.

| Vahend | Kavandatud roll ja põhjendus |
|---|---|
| Python ja Django | Konto, sessioonid, vormid, serveri loogika ning andmebaasi migratsioonid ühes raamistikus |
| Django HTML-mallid ja CSS | Lihtne kohanduv kasutajaliides; eraldi JavaScripti rakendust pole esimese versiooni jaoks vaja |
| PostgreSQL | Kasutajate, õppeainete ja ülesannete seoste ning piirangute hoidmine |
| Git ja GitHub | Kavandi ning hiljem lähtekoodi ajalugu ja tööde jälgimine |

Enne päris arendust valin sel hetkel toetatud stabiilsed versioonid ja fikseerin sõltuvused. See kavand ei väida, et keskkond või sõltuvused on juba paigaldatud.

## Komponendid ja andmeliikumine

Muudetav skeem: [`arhitektuur.drawio`](../diagrams/arhitektuur.drawio).

1. Õpilane täidab brauseris ülesande vormi. Brauser saadab serverile HTTPS POST-päringu koos vormiandmete, sessiooniküpsise ja CSRF-tõendiga.
2. Django päringukiht kontrollib sessiooni ja vormingut. Äriloogika kontrollib, et pealkiri ja tähtaeg on olemas ning valitud aine kuulub sellele kasutajale.
3. ORM-i kaudu salvestatakse ülesanne PostgreSQL-i. Omanik määratakse sessioonist; brauseri saadetud kasutaja ID-d ei usaldata.
4. Server suunab brauseri ülesannete nimekirja GET-päringule. Päring tagastab ainult sisselogitud kasutaja andmed ning järjestab need tähtaja järgi.
5. Mallikiht koostab HTML-i, mille brauser kuvab. Andmebaasiga brauser otse ei suhtle.

Skeemi nooled näitavad nii päringut kui ka vastust. Serveri sees ei toimu kihtide vahel HTTP-suhtlust: need on ühe protsessi funktsioonikutsed.

## Andmemudel

Muudetav skeem: [`andmemudel.drawio`](../diagrams/andmemudel.drawio).

- **Kasutaja:** ID, kasutajanimi, parooli räsi, ajavöönd. Esmalt kasutatakse Django kontomudelit ja ajavööndit profiili väljana. Parooli ei salvestata loetaval kujul.
- **Õppeaine:** ID, kasutaja ID, nimi. Nime unikaalsus kehtib ühe kasutaja piires.
- **Ülesanne:** ID, õppeaine ID, pealkiri, kirjeldus, tähtaeg, olek ja loomise aeg. Olek on `tegemata` või `tehtud`.

Ühel kasutajal on 0 kuni mitu õppeainet; igal ainel üks omanik. Ühel ainel on 0 kuni mitu ülesannet; igal ülesandel üks aine. Ülesande omanik leitakse aine kaudu, vältides vastuolulist topeltomanikku. Ülesandega aine kustutamine on esialgu keelatud; kasutaja konto kustutamise korral eemaldatakse tema ained ja ülesanded koos.

Tähtaeg salvestatakse ajavööndit arvestava ajatemplina ja kuvatakse kasutaja ajavööndis. Hilinemist ei salvestata eraldi olekuna: see arvutatakse, kui tähtaeg on möödunud ja töö tegemata.

## Eelised, puudused ja alternatiiv

| Kriteerium | Kihiline monoliit — valitud | Mikroteenused — alternatiiv |
|---|---|---|
| Arendus ja avaldamine | Üks serverirakendus; ühe arendaja jaoks lihtne | Mitu teenust, liideseid ja avaldamisprotsessi |
| Andmete terviklus | Tehingud ühes andmebaasis on lihtsad | Teenuste vahelise kooskõla korraldamine on keerukam |
| Skaleerimine | Skaleeritakse suuremat tervikut, isegi kui koormus on ühes osas | Üksikuid teenuseid saab eraldi skaleerida |
| Rikete mõju | Serveri rike võib mõjutada kõiki funktsioone | Teenuseid saab eraldada, kuid lisanduvad võrgurikked |
| Sobivus | Väike rakendus ja üks arendaja | Suur süsteem, eraldi meeskonnad ja erinev koormus |

Monoliidi puudus on komponentide võimaliku liigse seotuse kasvamine. Hoian konto-, aine- ja ülesannete vastutused eraldi moodulites. Mikroteenustele liiguksin alles mõõdetud vajaduse korral, näiteks kui üks osa vajab eraldi meeskonda või iseseisvat skaleerimist.

## Kvaliteet, testimine ja kasutuselevõtt

Kavandan kontrollid, mis tõendavad tulevase teostuse õigsust:

- Ühiktestid: tähtaja ja oleku põhjal hilinemise arvutamine ning sisestuse valideerimine.
- Integratsioonitestid: konto → aine → ülesanne salvestub; kasutaja A ei saa kasutaja B objekti lugeda, muuta ega kustutada.
- Kasutajaliidese kontroll: ülesande lisamine ja tehtuks märkimine arvutis ning 360 px laiuses vaates; vormil on sildid ja seda saab kasutada klaviatuuriga.
- Proovikasutus: kolm õpilast läbivad README-s kirjeldatud kolm põhitegevust; puudujäägid lisatakse backlog'i.

Enne väljalaset varundan andmebaasi, käivitan kontrollid ja proovikeskkonna migratsioonid. Tootmises kasutan HTTPS-i, keskkonnamuutujates saladusi, turvalisi sessiooniküpsiseid ja väljalülitatud silumisrežiimi. Teen igapäevase andmebaasivarukoopia, hoian 7 viimast koopiat ja proovin taastamist enne pilooti ning seejärel kord kuus. Rakenduse versiooni saab tagasi pöörata; andmebaasi skeemi muutus võib vajada eraldi taastamisplaani. Jälgin serverivigu ilma paroolide või ülesannete sisu logimata.
