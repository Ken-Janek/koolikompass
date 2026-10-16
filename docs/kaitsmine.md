# Kaitsmise meelespea

## Kava: 15–20 minutit

- **5 min:** põhjenda projekti valikuid ja näita tõendeid.
- **10 min:** tee õpetaja antud muudatus skeemil või tahvlil.
- **5 min:** vasta teadmiste küsimustele oma projekti näidetega.

Hindamine: kavand 25%, põhjendused 25%, muudatus 35%, teadmised 15%. Kõik õpiväljundid tuleb tõendada. Vastuse skeem: **vajadus → valik → alternatiiv → puudus või kontroll**.

## Ava enne kaitsmist

- [Projekti ülevaade](projekt.md) ja [tööde tahvel](https://github.com/users/Ken-Janek/projects/1): lood, sõltuvused, hinnangud ja poolelioleva töö piir 1.
- [Arhitektuur](../diagrams/arhitektuur.drawio) ja [andmemudel](../diagrams/andmemudel.drawio) diagrams.net-is: File → Open From → Device.
- [Git-ajalugu](https://github.com/Ken-Janek/koolikompass/commits/main/): näita vähemalt viit sisulist commit'i ja ühe muudatust.
- Rakendus: `kaivita.cmd` → [localhost:8000](http://127.0.0.1:8000). Näita aine ja töö lisamist, tähtaega ning tehtuks märkimist.

## Praktilise muudatuse töövõte

Täpsusta eesmärk → leia mõjutatud osad → muuda skeemi või tahvlit → selgita mõju ajale ja ulatusele → kontrolli ning salvesta. Harjutus salvesta eraldi koopiana; ajutised tahvlimuudatused taasta pärast harjutust.

| Harjutus | Muudatus ja põhjendus | Näidis |
| --- | --- | --- |
| Eraldi mobiilirakendus | Täpsusta, kas veebist piisab. Paigaldatavale kliendile lisa autentimisega JSON-API; taaskasuta ärireegleid ja andmebaasi. Tahvlile API, autentimine, mobiilivaated ja testid. | [Mobiil](../diagrams/arhitektuur-mobiil.drawio) |
| Tähtaeg poole lühem | Alguses 3 × 10 h = 30 h: US-01–US-05 20 h + keskkond 2 h + demo 1 h + puhver 3 h + proovikasutus ja avaldamine 4 h. US-06 P2, US-07–US-08 P3. Kontrollid säilivad. | [Tähtaeg](../diagrams/arhitektuur-tahtaeg.drawio) |
| Kasutajaid 100 korda rohkem | Mõõda samaaegset koormust ja päringuid. Vajadusel lisa koormusjaotur ning kaks Django koopiat ühise PostgreSQL-i ja sessioonihoidlaga. Andmebaas võib jääda pudelikaelaks. Tahvlile mõõtmised ja vajalikud parandused. | [Koormus](../diagrams/arhitektuur-koormus.drawio) |

Need on kavandamise harjutused. Edasi lükatud töö ei ole valmis; serverikoopiad ei tõenda koormustaluvust.

## Kiirvastused

| Küsimus | Vastuse tuum |
| --- | --- |
| Miks iteratiivne arendus? | Töötavat osa saab tagasiside järgi täiendada; koskmudel sobib stabiilsetele nõuetele |
| Miks Kanban? | Üks arendaja, pidev töövoog ja poolelioleva töö piir |
| Miks monoliit? | Väikest tervikut on lihtne hallata; mikroteenused lisaksid keerukust |
| Kuidas kaitsed andmeid? | Iga päring kontrollib sessiooni kasutajat ja aine omanikku |
| Commit, push, tag? | Kohalik seis, saatmine kaugserverisse, väljalaske märgis |
| SemVer algversioonist 2.4.1? | Parandus 2.4.2; tagasiühilduv lisandus 2.5.0; lõhkuv muudatus 3.0.0 |
| Mida pole kontrollitud? | PostgreSQL, tootmiskoormus ja kolme õpilase proovikasutus |

Harjuta taimeriga: põhjenda oma sõnadega ja tee muudatus enne näidise lugemist.
