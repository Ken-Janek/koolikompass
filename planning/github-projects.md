# GitHub Projects: tahvli seadistus

Tegelik avalik tahvel: [KooliKompass – arendus](https://github.com/users/Ken-Janek/projects/1). Seal on kaheksa mustandkaarti koos kasutajalugude, kriteeriumide ja sõltuvustega ning Priority ja Estimate väljad. Periood on kaardi kirjelduses, mitte eraldi väljas. Vaikerepositoorium on `Ken-Janek/koolikompass`.

Loodud tahvel kasutab GitHubi ingliskeelseid olekuid: Backlog, Ready, In progress, In review ja Done. Need vastavad alloleva plaani eestikeelsetele olekutele. In progress ja In review veergude nähtav piir on 1; piiri järgib arendaja.

## Soovitud tahvel

Nimi: **KooliKompass – arendus**. Vaade: Board, rühmitatud välja Status järgi.

| Väli | Väärtused |
|---|---|
| Status | Backlog; Valmis alustamiseks; Töös; Kontrollimisel; Valmis |
| Priority | P1; P2; P3 |
| Estimate | Number, tundides |
| Periood | 1; 2; Hiljem |

WIP-piir: Töös ≤ 1 ja Kontrollimisel ≤ 1. Piiri jälgin ise; tavapärane tahvel ei pruugi seda tehniliselt jõustada.

## Seadistamine ja näitamine

1. Ava GitHubi profiil → Projects → New project → Board.
2. Lisa ülaltoodud olekud ja väljad ning seo projekt repositooriumiga.
3. Lisa kaheksa kasutajalugu. Pealkirjaks pane ID ja lühinimi, kirjeldusse kasutajalugu, vastuvõtukriteeriumid ning sõltuvused dokumendist `docs/02-metoodika-ja-backlog.md`.
4. Määra prioriteedid ja tunnid. Periood 1: US-01–US-03; periood 2: US-04–US-06; ülejäänud Hiljem.
5. US-01 on „Valmis alustamiseks“; teised „Backlog“. Kui konto valmib, saab US-02 liikuda alustamisvalmis olekusse.
6. Kaitsmisel näita prioriteete ning liiguta prooviks üks kaart „Töös“ ja seejärel tagasi. Selgita, et see on tahvli demonstratsioon, mitte tõend valmis funktsioonist.

GitHub Projects toetab tööde esitamist tabeli ja tahvlina ning kohandatud väljade kasutamist. Juhend: [GitHubi ametlik dokumentatsioon](https://docs.github.com/en/issues/planning-and-tracking-with-projects/creating-projects/creating-a-project).

`backlog.json` on lugude lähteandmete fail, mitte GitHub Projectsi automaatne import ega valmis projektihaldusvahend.
