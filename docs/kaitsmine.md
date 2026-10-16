# Kaitsmise meelespea

## Kava: 15–20 minutit

| Osa | Aeg | Näita ja selgita |
| --- | ---: | --- |
| Valikute põhjendamine | 5 min | Probleem, iteratiivne mudel, Kanban, CASE-vahendid, arhitektuur ja Git |
| Ootamatu muudatus | 10 min | Muuda skeemi või tahvlit, selgita mõju ja kontrolli tulemust |
| Teadmiste kontroll | 5 min | Rakenda mõisteid oma projekti näidetega |

Hindamise jaotus: kavand 25%, põhjendused 25%, praktiline muudatus 35%, teadmised 15%. Kõik neli õpiväljundit tuleb eraldi tõendada. Vasta õpetaja küsimusele otse, näita päris faili või töövahendit ja põhjenda: **vajadus → valik → alternatiiv → puudus või kontroll**.

## Ava enne kaitsmist

- [Projekti kavand ja teostus](projekt.md): etapid, mudelite võrdlus, kaheksa kasutajalugu, 20 tunni plaan, arhitektuur, CASE-võrdlus ja SemVer.
- [GitHub Projects](https://github.com/users/Ken-Janek/projects/1): ava US-03, näita sõltuvusi, Priority ja Estimate välju ning poolelioleva töö piiri 1.
- [Git-ajalugu](https://github.com/Ken-Janek/koolikompass/commits/main/): näita vähemalt viit sisulist commit'i ja ühe muudatuse sisu.
- [Arhitektuur](../diagrams/arhitektuur.drawio) ja [andmemudel](../diagrams/andmemudel.drawio): ava diagrams.net-is File → Open From → Device.
- Töötav rakendus: `kaivita.cmd`, seejärel [localhost:8000](http://127.0.0.1:8000). Näita aine ja töö lisamist, lähimat tähtaega ning tehtuks märkimist.

## Ootamatu muudatuse töövõte

1. Täpsusta eesmärk ja eeldused (1 min).
2. Leia mõjutatud komponendid, lood ja sõltuvused (1 min).
3. Muuda ise skeemi või tegelikku tahvlit (4 min).
4. Selgita taaskasutust, uut tööd, prioriteete ja ajakava (2 min).
5. Kontrolli seoseid ja kriteeriume ning salvesta tulemus (2 min).

Harjutusskeemid on näited, mitte praeguse rakenduse uued nõuded. Salvesta katsetus eraldi koopiana. Tahvlil märgista ajutised kaardid HARJUTUS ja taasta hiljem algne seis. Redaktoris salvestamine ei uuenda GitHubi automaatselt.

## Kolm harjutust

### 1. Eraldi mobiilirakendus

Täpsusta, kas piisab telefonis töötavast veebist või on vaja paigaldatavat klienti. Veeb töötab juba telefonis. Eraldi kliendi korral lisa skeemile mobiiliklient ja Django sisse JSON-API kiht. Ühenda klient HTTPS-i ja autentimise kaudu API-ga ning API olemasoleva äriloogikaga; brauseri HTML-tee säilib. Mobiil ei suhtle otse andmebaasiga.

Taaskasuta mudeleid, ORM-i ja ärireegleid. Lisa tahvlile mobiili autentimise, ülesannete API, mobiilivaadete ja ühise töövoo kontrolli lood. Kriteeriumid: vale autentimine keelab ligipääsu, võõrad tööd jäävad kaitstuks ja mobiilis lisatud töö ilmub veebis. Tokenite korral kavanda hoiustamine, aegumine ja tühistamine. Hinda maht pärast platvormi ja vajaduste täpsustamist.

Näidis: [mobiili skeem](../diagrams/arhitektuur-mobiil.drawio). Server jääb monoliidiks; uus nõue lisab tööd ja võib nõuda muude funktsioonide edasilükkamist.

### 2. Tähtaeg lüheneb poole võrra

Kui muudatus tuleb alguses, on kolm nädalat × 10 h = 30 h. Kui aega on juba kulunud, arvuta allesjäänud võimekus uuesti.

| Sisu | Otsus |
| --- | --- |
| US-01–US-05 | P1, esimene kasutatav versioon; lugude maht kokku 20 h |
| US-06 | P2, muutmine ja kustutamine hiljem |
| US-07–US-08 | P3, filtrid ja kalender hiljem |
| Lisatööd | Keskkond 2 h, demo 1 h, puhver 3 h, proovikasutus ja kasutuselevõtt 4 h |

Kokku 30 h on prognoos. Muuda tahvlil prioriteete ka kirjeldustes ja pealkirjades; edasi lükatud töö ei ole Done. Ära kärbi andmete eraldatuse ega põhiteekonna kontrolli. Tehniline arhitektuur säilib, muutub väljalaske ulatus.

Näidis: [lühema tähtaja skeem](../diagrams/arhitektuur-tahtaeg.drawio).

### 3. Kasutajaid tuleb sada korda rohkem

Täpsusta samaaegsete päringute, andmemahu ja tipptunni koormus. Mõõda vastuseaega, CPU-d, mälu, aeglasi päringuid, lukke ja ühenduste arvu. Vajaduse korral paranda päringuid, kasuta lehekülgi ning lisa mõõtmise põhjal indekseid.

Skeemi üks võimalik muudatus on koormusjaotur → Django A ja B → ühine PostgreSQL. Eksemplarid on sama monoliidi koopiad. Sessioonid peavad olema ühises hoidlas, staatilisi faile võib teenindada eraldi. Kaks serverit ei lahenda andmebaasi pudelikaela automaatselt.

Tahvlile lisa koormustest, päringute analüüs ja vajaduse korral serveri seadistustöö. Kontrolli mõõdetud tulemust ja andmete terviklust.

Näidis: [koormuse skeem](../diagrams/arhitektuur-koormus.drawio).

## Kiirküsimused

| Küsimus | Vastuse tuum |
| --- | --- |
| Miks Kanban? | Üks arendaja, pidev töövoog ja poolelioleva töö piir; Scrum lisaks rollid ja sündmused |
| Miks monoliit? | Väike seotud tervik, lihtne avaldada; mikroteenuste haldus ja võrguvead lisaksid keerukust |
| Kuidas kaitsed andmeid? | Omanik sessioonist; iga päring piiratakse kasutaja ainetega, ka otse URL-i kasutades |
| Kus on hilinenud-olek? | Arvutatakse tähtajast ja tegemata-olekust, eraldi ei salvestata |
| Commit, push ja tag? | Kohalik seis, saatmine kaugserverisse, konkreetse ajaloo punkti nimi |
| SemVer versioonist 2.4.1? | Veaparandus 2.4.2; uus tagasiühilduv funktsioon 2.5.0; lõhkuv muudatus 3.0.0 |
| Mida testid ei tõenda? | SQLite'i testid ei kinnita PostgreSQL-i tööd, tootmise koormust ega päris õpilaste kasutusmugavust |

Harjuta taimeriga ja tee muudatus enne näidislahenduse lugemist. Kontrolli, et oskad valikuid oma sõnadega põhjendada, materjale leida ja muudatuse mõju näidata.
