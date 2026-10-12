# Arhitektuuriskeemi kolm koopiat

Algne `diagrams/arhitektuur.drawio` säilib. Need koopiad on kaitsmise harjutusvariandid; algse projekti ulatus ja tööde tahvel pole nende tõttu muudetud.

| Variant | Ava muudetav skeem | Lisatud muudatus |
|---|---|---|
| Mobiilirakendus | [Ava diagrams.net-is](https://app.diagrams.net/#Uhttps%3A%2F%2Fraw.githubusercontent.com%2FKen-Janek%2Fkoolikompass%2Fmain%2Fdiagrams%2Farhitektuur-mobiil.drawio) | Mobiiliklient ja API-kiht; mõlemad kliendid kasutavad sama äriloogikat ja andmebaasi |
| Suurem koormus | [Ava diagrams.net-is](https://app.diagrams.net/#Uhttps%3A%2F%2Fraw.githubusercontent.com%2FKen-Janek%2Fkoolikompass%2Fmain%2Fdiagrams%2Farhitektuur-koormus.drawio) | Koormusjaotur, kaks Django eksemplari ning ühine andmete ja sessioonide hoidmine |
| Lühem tähtaeg | [Ava diagrams.net-is](https://app.diagrams.net/#Uhttps%3A%2F%2Fraw.githubusercontent.com%2FKen-Janek%2Fkoolikompass%2Fmain%2Fdiagrams%2Farhitektuur-tahtaeg.drawio) | Esimese versiooni funktsioonid ja 30 tunni näidisplaan; tehniline arhitektuur säilib |

## Kuidas skeemi ise muuta?

1. Ava tabelist soovitud link.
2. Kujundi teksti muutmiseks tee sellel topeltklõps.
3. Uue kasti lisamiseks lohista ristkülik vasakult skeemile ja kirjuta nimi.
4. Ühendamiseks lohista kujundi ühenduspunkt teise kujundini. Noole tekst lisa topeltklõpsuga.
5. Salvesta Fail → Salvesta kui kaudu `.drawio` failina oma projektikausta. Redaktori muudatus ei uuenda GitHubi faili automaatselt.

## Mida lisaks tahvlil teha?

Ava [GitHub Projects](https://github.com/users/Ken-Janek/projects/1/views/1) Ken-Janek kontoga.

- **Mobiil:** lisa Backlog-veergu API, mobiili autentimise, mobiilivaadete ja ühise töövoo kontrollimise kaardid. Uuel kaardil kasuta mustandi loomiseks Ctrl+Enter. Ava kaart, lisa kirjeldus ja vastuvõtukriteeriumid ning määra Priority. Näited on [harjutuste dokumendis](07-praktiline-kaitsmine.md).
- **Lühem tähtaeg:** ava US-06 → Priority → P2; US-07 → Priority → P3. Muuda samad prioriteedid ka pealkirjades ja kirjeldustes. US-01–US-05 jäävad esimesse versiooni. Ära märgi edasi lükatud töid valmis.
- **Suurem koormus:** lisa koormustesti, päringute uurimise ja vajaduse korral koormusjaoturi seadistamise kaardid. Serverikoopiad ei tõenda veel, et vajalik koormus on saavutatud.

Praegust tahvlit pole harjutusnõuete järgi ümber tehtud. Kaitsmisel tee õpetaja antud nõude põhjal vajalik muudatus.
