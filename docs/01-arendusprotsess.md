# 1. Tarkvara arendusprotsess

## Etapid ja nende eesmärgid

| Etapp | Tegevus KooliKompassis | Tulemus ja eesmärk |
|---|---|---|
| Idee ja probleemi uurimine | Uurin, kuidas õpilased ülesandeid ja tähtaegu jälgivad, ning küsin kolmelt õpilaselt nende vajaduste kohta. | Selgub, kas ühine ülesannete vaade lahendab tegeliku probleemi. |
| Nõuete analüüs | Koostan kasutajalood, prioriteedid ja vastuvõtukriteeriumid. | Piiritlen esimese versiooni ja saan aru, mida kasutaja vajab. |
| Kavandamine | Valin tehnoloogiad, joonistan arhitektuuri ja andmemudeli ning visandan ülesannete vaate. | Enne programmeerimist on teada komponentide vastutus ja andmete struktuur. |
| Teostus | Arendan väikeste osadena: konto, õppeained, ülesanded, nimekiri ja tehtuks märkimine. | Iga osa annab kontrollitava tulemuse. |
| Testimine | Kontrollin ärireegleid, andmete salvestamist, kasutajate andmete eraldatust ja mobiilivaadet. | Funktsioon töötab vastuvõtukriteeriumide järgi ega riku varem tehtut. |
| Kasutuselevõtt | Paigaldan esmalt proovikeskkonda, kogun tagasisidet ja alles siis avaldan stabiilse versiooni. | Rakendus muutub kasutajatele kättesaadavaks ja selle kasutamine on arusaadav. |
| Hooldus | Jälgin vigu, uuendan sõltuvusi, teen varukoopiaid ning planeerin uusi kasutajalugusid. | Rakendus püsib töökindel ja vastab muutuvatele vajadustele. |

Etapid korduvad iga väikese täiendusena. Testimine toimub iga muudatuse juures, mitte ainult projekti lõpus. Praeguse koolitöö tulemus on kavand; teostus, testimine ja kasutuselevõtt on tulevase arenduse plaan.

## Koskmudel ja iteratiivne mudel

| Omadus | Koskmudel | Iteratiivne ja inkrementaalne mudel |
|---|---|---|
| Töö korraldus | Etapid läbitakse peamiselt järjest; järgmine algab eelmise tulemuse põhjal. | Analüüsi, kavandamist, arendamist ja testimist korratakse väikeste osade kaupa. |
| Nõuded | Sobib hästi, kui need on alguses selged ja stabiilsed. | Võimaldab nõudeid kasutaja tagasiside põhjal täpsustada. |
| Tagasiside | Terviklahenduse tagasiside võib saabuda hilja. | Kasutaja saab varakult proovida piiratud, kuid töötavat osa. |
| Muudatused | Hiline muudatus võib nõuda mitme varasema etapi ümbertegemist. | Muudatuse saab lisada tööde nimekirja ja kavandada järgmisse arendusossa. |
| Risk | Valesti mõistetud vajadus võib ilmneda alles lõpus. | Vajadusi kontrollitakse varakult, kuid terviku kavand ja dokumentatsioon vajavad pidevat tähelepanu. |

Valin iteratiivse ja inkrementaalse mudeli. Ma tean põhiprobleemi, kuid parim ülesannete vaade ja filtrid võivad selguda alles proovikasutamisel. Esmalt valmiks lihtne töövoog „lisa ülesanne → vaata tähtaega → märgi tehtuks“, seejärel lisanduksid filtrid ja kalendrivaade. Koskmudel oleks sobivam näiteks juhul, kui tellija annaks ette muutumatu spetsifikatsiooni ja nõuaks iga etapi ametlikku üleandmist.

## Kui klient muudab nõudeid

Näide: arenduse ajal soovib proovikasutaja ka nädalakalendrit.

1. Täpsustan vajaduse: kas piisab nädala ülesannete nimekirjast või on vaja päris kalendrit?
2. Lisan kasutajaloo US-08 ja määran vastuvõtukriteeriumid.
3. Hindan mõju mahule, skeemidele, testidele ja tähtajale. Olemasolev tähtaeg võib piisata; andmemudelit ei muudeta ilma vajaduseta.
4. Võrdlen muudatust põhifunktsioonide prioriteediga. Esimesel perioodil jäävad konto ja ülesannete lisamine ettepoole.
5. Lepin tellijaga kokku: kalendrivaade tuleb hiljem või mõni vähem tähtis töö liigub järgmisse perioodi. Kõike ei lisata sama tähtaja sisse.
6. Uuendan backlog'i, otsuse põhjendust ja vajaduse korral skeemi. Valmis töid kontrollin uuesti.

Kui muudatus parandab teiste kasutajate andmete nähtavuse vea, peataksin madalama prioriteediga töö ning lahendaksin vea kohe.

## Esialgne ajakava ja riskid

Arenduse planeerimise eeldus on üks arendaja, 10 tundi nädalas ja kuus nädalat. Tegelikku kiirust mõõdan esimesel perioodil.

| Aeg | Eesmärk |
|---|---|
| Nädal 1 | Vajaduste täpsustamine, kavand ja esimeste lugude ettevalmistus |
| Nädalad 2–3 | Konto, õppeained ja ülesannete lisamine |
| Nädal 4 | Nimekiri, tehtuks märkimine ja muutmine |
| Nädal 5 | Proovikasutus, parandused ja väljalaskekandidaat |
| Nädal 6 | Kasutuselevõtt, varunduse kontroll ja kasutusjuhend |

Peamised riskid on liiga suur ulatus, ajahinnangute eksimine ja andmete kadumine. Piiran esimest versiooni, jätan arendusperioodi puhvri ning kavandan andmebaasi igapäevase varunduse ja taastamise proovimise. Enne pilootkasutust kontrollin, et kasutaja näeb ja muudab ainult enda andmeid.
