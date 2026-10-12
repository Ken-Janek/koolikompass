# 3. CASE-vahendid

## Kasutatavad vahendid

**diagrams.net** toetab süsteemi modelleerimist ja disaini. Projekti komponendid, seosed ning andmemudel on `.drawio` failides. Need on XML-põhised muudetavad diagrammid, mitte ainult pildid.

**GitHub Projects** toetab arendustegevuste planeerimist ja jälgimist. Kaheksa kasutajalugu liiguvad Kanbani tahvlil olekute vahel; prioriteedid ja hinnangud aitavad otsustada järgmise töö. Tegelik tahvli link ja tõendid lisatakse kaitsmise dokumenti.

Git toetab muudatuste ajalugu mõlema vahendi kõrval. Diagrams.net ei asenda projektitahvlit ja projektitahvel ei asenda süsteemiskeemi.

## Modelleerimisvahendite võrdlus

| Omadus | diagrams.net | PlantUML |
|---|---|---|
| Koostamine | Kujundid, tekst ja ühendused visuaalses redaktoris | Diagrammi kirjeldus tekstina |
| Git-is ülevaatamine | XML-i muutus võib olla pikk ja raskem lugeda | Teksti muudatus on tavaliselt hästi võrreldav |
| Paigutus | Kujundite asukohta saab otse valida | Paigutuse arvutab valdavalt renderdaja |
| Kasutamine kaitsmisel | Komponenti saab hiirega kiiresti lisada ja ümber paigutada | Muudan tekstikirjeldust ja renderdan uuesti |
| Valik selles projektis | Kasutan mõlema muudetava skeemi jaoks | Võimalik alternatiiv tekstipõhiste UML-skeemide jaoks |

Valin diagrams.net, sest soovin kaitsmisel nähtavalt muuta komponendi nime, lisada kujundi ja tõmmata ühenduse. PlantUML oleks sobiv, kui eelistaksin skeeme lähtekoodina kirjutada ning automatiseeritult renderdada.

## Skeemi avamine ja kaitsmisel muutmine

1. Ava [diagrams.net](https://app.diagrams.net/) ja vali salvestuskohaks Device, kui küsitakse.
2. Vali **File → Open From → Device** ja ava `diagrams/arhitektuur.drawio`.
3. Topeltklõpsa komponendil ja muuda näiteks „Brauser“ nimeks „Telefoni või arvuti brauser“.
4. Näitlikusta hilisemat muudatust: lisa kast „Kalendrivaade“ ning ühenda see kasutajaliidese kihiga. Selgita, et see jääb monoliidi osaks.
5. Salvesta eraldi koopiana või tee sisuline muudatus algfailis, salvesta ja lisa Git-i uue commit'ina. Pelgalt demonstratsioonimuudatust ei pea projekti püsivalt jätma.

Failide avamine on kirjeldatud [diagrams.net ametlikus juhendis](https://www.drawio.com/docs/manual/open-diagram-file/). Tahvli loomist kirjeldab [GitHubi juhend](https://docs.github.com/en/issues/planning-and-tracking-with-projects/creating-projects/creating-a-project).
