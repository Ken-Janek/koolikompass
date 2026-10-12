# 2. Arendusmetoodika ja tööde nimekiri

## Valik: Kanban

Arendan esialgu üksinda. Kanban võimaldab võtta järgmise kõige olulisema valmis töö ilma Scrumi rollide ja kindlate sprintide korralduseta. Iteratiivne mudel kirjeldab arenduse elutsüklit; Kanban kirjeldab igapäevase töö planeerimist ja liikumist. Need täiendavad teineteist.

GitHub Projects tahvli veerud on **Backlog**, **Valmis alustamiseks**, **Töös**, **Kontrollimisel**, **Valmis**. Töös võib olla korraga üks lugu ja kontrollimisel üks lugu. Kui kontrollimisel tekib takistus, lahendan selle enne järgmise loo alustamist. Need piirangud aitavad lõpetada alustatud töö.

Kord nädalas vaatan üle prioriteedid, takistused ja lõpetatud tööde arvu. Iga tööpäeva lõpus uuendan tahvlit. Mõõdan loo alustamisest lõpetamiseni kulunud aega ning selle põhjal parandan hinnanguid. Kahe nädala plaan on prognoos, mitte Kanbani kohustuslik sprint.

**Alustamisvalmis:** vajadus, prioriteet ja kontrollitavad kriteeriumid on selged; sõltuvused on täidetud ning lugu mahub mõne töökorra sisse.

**Valmis:** kõik vastuvõtukriteeriumid on kontrollitud, asjakohased testid läbivad, muudatus on Git-is, dokumentatsioon on uuendatud ja proovikeskkonnas kontrollitud. Planeerimisdokumendi valmimine ei tähenda kasutajaloo arenduse valmimist.

## Prioriteedid ja backlog

P1 = esimese versiooni jaoks vajalik; P2 = oluline mugavus; P3 = hilisem täiendus. Sama prioriteedi puhul järgin tabeli järjekorda ja sõltuvusi. Tunnid on esialgsed arendushinnangud koos kontrollimisega.

| ID | Kasutajalugu | Prioriteet | Tundi | Sõltub |
|---|---|---|---:|---|
| US-01 | Õpilasena soovin luua konto ning sisse ja välja logida, et minu ülesanded oleksid isiklikud. | P1 | 6 | — |
| US-02 | Õpilasena soovin lisada õppeaine, et saaksin ülesandeid aine järgi korraldada. | P1 | 3 | US-01 |
| US-03 | Õpilasena soovin lisada pealkirja, õppeaine ja tähtajaga ülesande, et töö ei ununeks. | P1 | 5 | US-02 |
| US-04 | Õpilasena soovin näha tegemata ülesandeid tähtaja järjekorras, et teaksin, millega alustada. | P1 | 4 | US-03 |
| US-05 | Õpilasena soovin märkida ülesande tehtuks ja vajaduse korral uuesti tegemata, et minu ülevaade oleks õige. | P1 | 2 | US-04 |
| US-06 | Õpilasena soovin muuta ja kustutada enda ülesannet, et saaksin parandada ekslikku sisestust. | P1 | 3 | US-03 |
| US-07 | Õpilasena soovin filtreerida ülesandeid õppeaine ja oleku järgi, et leiaksin vajaliku töö kiiremini. | P2 | 3 | US-04, US-05 |
| US-08 | Õpilasena soovin vaadata valitud nädala tähtaegu kalendris, et saaksin oma nädalat planeerida. | P3 | 5 | US-04 |

## Vastuvõtukriteeriumid

- **US-01:** korrektsete andmetega konto saab luua; korduv kasutajanimi annab veateate; õige parooliga saab sisse; vale parooliga ei saa; väljalogimise järel on isiklik vaade kaitstud. Kasutaja A ei saa näha kasutaja B ülesandeid ka otse URL-iga.
- **US-02:** mittetühja nimega aine salvestub sisselogitud kasutajale; sama kasutaja ei saa luua sama nimega ainet; teise kasutaja samanimeline aine on lubatud.
- **US-03:** pealkiri, enda õppeaine ja kehtiv tähtaeg on kohustuslikud; vigane sisestus annab veateate; ülesanne jääb alles pärast lehe värskendamist. Mineviku tähtaeg on lubatud ja ülesanne kuvatakse hilinenuna.
- **US-04:** nimekiri sisaldab ainult enda tegemata ülesandeid ja järjestub tähtaja järgi kasvavalt; võrdse tähtajaga tööd järjestuvad ID järgi; möödunud tähtaeg on tähistatud tekstiga „Hilinenud“; tühi nimekiri näitab selgitust.
- **US-05:** tehtuks märgitud töö kaob tegemata tööde vaatest ja on tehtud tööde vaates; taastamine toob töö tagasi; mõlemad olekud säilivad lehe värskendamisel.
- **US-06:** muudatus salvestub ja ilmub nimekirja; kustutamine nõuab kinnitust; tühistamine jätab töö alles; võõra ülesande muutmine ja kustutamine on keelatud.
- **US-07:** aine- ja olekufilter töötavad eraldi ning koos; filtrite eemaldamine taastab vastava täieliku nimekirja; tulemusteta otsing kuvab selgituse.
- **US-08:** vaade näitab valitud nädala enda ülesandeid õigel päeval; nädala vahetamine muudab kuvatavaid ülesandeid; kuupäev arvutatakse kasutaja ajavööndis.

## Esimene arendusperiood: kaks nädalat, 20 tundi

Eesmärk on võimaldada õpilasel konto luua, lisada aine ja salvestada ülesanne. Täielik esimene versioon vajab veel järgmise perioodi töid US-04–US-06.

| Tegevus | Maht | Tulemus |
|---|---:|---|
| Keskkond, Django projekt, PostgreSQL ja esmane migratsioon | 2 h | Kohalik käivitus ja andmebaasiühendus |
| US-01 | 6 h | Konto ja andmete eraldatus |
| US-02 | 3 h | Õppeaine lisamine |
| US-03 | 5 h | Ülesande sisestamine ja salvestamine |
| Ühine töövoo demonstratsioon ning tagasiside | 1 h | Konto → aine → ülesanne läbitud |
| Puhver vigadele ja hinnangu täpsustamisele | 3 h | Vajaduse korral parandused |

Lugude hinnangud sisaldavad nende funktsioonide teste; ühine demonstratsioon kontrollib terviklikku töövoogu. Kui aeg saab otsa, ei märgi pooleli olevat lugu valmis. Uuendan prognoosi ning jätan US-03 järgmisse perioodi, kui US-01 ja US-02 lõpetamine seda nõuab.

Esialgses kavandis oli US-01 veerus „Valmis alustamiseks“ ning US-02–US-08 backlog'is. Pärast Django rakenduse teostamist ja kontrollimist on kõik kaheksa kaarti Done-veergu viidud. Teostuse kontrollid ja piirangud on dokumendis `10-rakenduse-teostus.md`; algne prioriteetide ja perioodide plaan säilib ülal võrdluseks.
