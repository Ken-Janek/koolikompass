# Lühike õppetekst ja kaitsmise lingid

## 1. Projekti idee

**Ava:** [README](https://github.com/Ken-Janek/koolikompass).

> KooliKompass on õppeülesande jaoks koostatud kooliülesannete ja tähtaegade planeerija kavand. Rakenduses saaks luua konto, lisada aineid ja ülesandeid, vaadata tähtaegu ning märkida töid tehtuks.

## 2. Arendusprotsess

**Ava:** [arendusprotsess](https://github.com/Ken-Janek/koolikompass/blob/main/docs/01-arendusprotsess.md). Näita mudelite võrdlust.

> Etapid on vajaduste uurimine, nõuded, kavandamine, arendamine, testimine, kasutuselevõtt ja hooldus. Valisin iteratiivse mudeli: rakendus valmib väikeste osadena ning tagasiside põhjal saab teha muudatusi. Koskmudel liigub peamiselt järjest ja sobib stabiilsete nõuetega projektile. Uue nõude korral hindaksin mõju ja uuendaksin tööde plaani.

## 3. Kanban

**Ava:** [tööde tahvel](https://github.com/users/Ken-Janek/projects/1/views/1). Näita veerge ja ava US-03 kaart.

> Valisin Kanbani, sest projekt on kavandatud ühele arendajale. Tahvel näitab tööde olekut. Korraga võib töös olla üks lugu ja kontrollimisel üks. Kaheksal kasutajalool on prioriteedid: P1 vajalik, P2 oluline mugavus, P3 hilisem täiendus. Ülesande lisamine sõltub õppeainest ja kontost. Esimese kahe nädala plaan on 20 tundi: konto, aine ja ülesande lisamine koos seadistuse, kontrollimise ja puhvriga.

## 4. CASE-vahendid

**Ava:** [arhitektuuriskeem redaktoris](https://app.diagrams.net/#Uhttps%3A%2F%2Fraw.githubusercontent.com%2FKen-Janek%2Fkoolikompass%2Fmain%2Fdiagrams%2Farhitektuur.drawio).

> Kasutasin diagrams.net-i skeemide jaoks ja GitHub Projectsi tööde planeerimiseks. Diagrams.net-is muudan kujundeid ja ühendusi visuaalselt. PlantUML kirjeldab skeemi tekstina, mida on Git-is lihtsam võrrelda. Valisin diagrams.net-i, sest skeemi on mugav redaktoris muuta.

## 5. Arhitektuur

**Näita skeemil:** brauser → päringukiht → äriloogika → ORM → PostgreSQL.

> Rakendus oleks veebirakendus Django serveri ja PostgreSQL-i andmebaasiga. Valisin kihilise monoliidi: server avaldatakse ühe tervikuna, aga vastutused on eraldatud. Seda on väikese projekti puhul lihtne arendada ja hallata. Puudus on see, et serveri rike võib mõjutada kõiki funktsioone. Mikroteenuseid saab eraldi avaldada ja skaleerida, kuid nende haldamine on keerukam.
>
> Brauser saadab ülesande andmed serverile. Server kontrollib sisselogimist, sisestust ja aine omanikku. ORM salvestab ülesande andmebaasi. Seejärel koostab server nimekirjast HTML-vaate. Brauser andmebaasiga otse ei suhtle.

**Ava:** [andmemudel](https://app.diagrams.net/#Uhttps%3A%2F%2Fraw.githubusercontent.com%2FKen-Janek%2Fkoolikompass%2Fmain%2Fdiagrams%2Fandmemudel.drawio).

> Ühel kasutajal võib olla mitu õppeainet ja ühel ainel mitu ülesannet. Ülesande omanik leitakse õppeaine kaudu. Kasutaja pääseb ligi ainult enda andmetele.

## 6. Git ja versioonid

**Ava:** [commit'ide ajalugu](https://github.com/Ken-Janek/koolikompass/commits/main/). Ava üks commit ja näita muudatusi.

> Dokumendid ja skeemid on salvestatud sisuliste commit'idena. Commit salvestab kohaliku muudatuse, push saadab selle GitHubi ja haru võimaldab muudatust eraldi teha. Kasutan SemVer-i: MAJOR.MINOR.PATCH. Versioonist 2.4.1 saaks tagasiühilduva veaparandusega 2.4.2, uue tagasiühilduva funktsiooniga 2.5.0 ja avalikku API-t lõhkuva muudatusega 3.0.0. Väljalaske commit'i märgiksin tag'iga.

## Praktiline muudatus

Valmis näidiskoopiaid saab avada [siit](09-skeemide-koopiad.md). Seal on ka lühikesed juhised skeemi ja tahvli muutmiseks.

| Ülesanne | Ava | Tee ja selgita |
|---|---|---|
| Mobiilirakendus | Arhitektuuriskeem ja tahvel | Lisa mobiiliklient ja serveri sisse API-kiht. Ühenda API äriloogikaga. Ärireeglid ja andmebaas jäävad ühised. Lisa API, autentimise, mobiilivaadete ja kontrollimise tööd ning hinda mõju ajale. |
| Tähtaeg poole lühem | Tahvel | Arvuta allesjäänud aeg. Jäta põhiversiooni US-01–US-05. Muuda US-06 P2-ks ja US-07 P3-ks; US-08 jääb P3. Uuenda ka kaartide pealkirju ja kirjeldusi. Kontrollimine jääb plaani. |
| Sada korda rohkem kasutajaid | Arhitektuuriskeem ja tahvel | Mõõda koormust. Vajadusel lisa koormusjaotur ja kaks sama Django serveri koopiat ühise andmebaasiga. Kontrolli ka aeglaseid andmebaasipäringuid. Serverikoopiad ei ole mikroteenused. |

Tahvli muutmiseks logi sisse Ken-Janek kontoga. Muudetud skeem salvesta `.drawio` failina projektikausta; redaktor ei kirjuta GitHubi faili automaatselt üle.

## Teadmiste kontroll

- **Scrum ja Kanban:** Scrum kasutab sprinte, kindlaid vastutusi ja sündmusi; Kanban nähtavat töövoogu ja poolelioleva töö piiramist.
- **CASE:** tarkvaraarendust toetav töövahend, näiteks skeemiredaktor.
- **Monoliit ja mikroteenused:** üks avaldatav tervik või iseseisvalt avaldatavad teenused.
- **Git-haru:** muudatuse tegemine ja kontrollimine main-harust eraldi.
- **Valmis töö:** vastuvõtukriteeriumid ja vajalikud kontrollid on täidetud, muudatus Git-is salvestatud.
- **2.4.1 veaparandus:** 2.4.2; **uus tagasiühilduv funktsioon:** 2.5.0; **API-d lõhkuv muudatus:** 3.0.0.

Pikemad harjutused: [praktilise kaitsmise juhend](https://github.com/Ken-Janek/koolikompass/blob/main/docs/07-praktiline-kaitsmine.md).
