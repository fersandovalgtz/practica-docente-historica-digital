# PDHD periodization protocol

## Purpose

PDHD uses periodization as an **analytical stratification device**, not as a claim that pedagogical change occurred synchronically across Mexico. The initial README used overlapping reference ranges to describe broad historical problems. Those ranges remain useful narratively, but they are not suitable as mutually exclusive sampling strata.

For quantitative summaries, cohort balancing and annotation sampling, PDHD therefore adopts the following non-overlapping `era_code` system.

| era_code | Range | Working label | Main analytical problem |
|---|---|---|---|
| E1 | 1870–1910 | Liberal and Porfirian professionalization | consolidation of pedagogical press, normalism, objective teaching, inspection, professional identity and regional educational networks |
| E2 | 1911–1920 | Revolutionary transition | institutional disruption, continuity of late-Porfirian pedagogies, revolutionary redefinition of schooling and teacher authority |
| E3 | 1921–1934 | SEP reconstruction and rural expansion | national cultural project, rural schooling, missions, teacher formation, community action and expansion of state pedagogical guidance |
| E4 | 1935–1940 | Socialist education and Cardenista reconfiguration | socialist schooling, rural and indigenous education, collective work, political formation and intensified state direction |
| E5 | 1941–1970 | National consolidation and mass expansion | institutional stabilization, expansion of schooling, professional normalization and postwar curricular-pedagogical consolidation |
| E6 | 1971–2000 | Planning, modernization and evaluation | technification, planning, learning objectives, evaluation, teacher updating and administrative modernization |
| E7 | 2001–2026 | Inclusion, accountability and digital transformation | inclusion, competencies, standardized evaluation, digital mediation, professional learning and the Nueva Escuela Mexicana |

## Rules

1. Every analysis-ready document should eventually receive exactly one `era_code`.
2. A date interval that crosses an era boundary is not silently forced into one era. Volume-level objects should be split into issue-level objects when possible; otherwise the record must declare `cross_era=true` in a future normalization pass.
3. Era assignment is based on the publication date of the documentary object, not the historical period discussed inside the text.
4. Era codes are sampling metadata. They do not replace finer historical interpretation.
5. Regional chronologies may diverge from national institutional chronologies. Comparative work must therefore preserve `place`, publisher/institution and documentary type alongside `era_code`.
6. Changes to boundaries require a versioned methodological decision and a migration note; previously released datasets must not be silently relabeled.

## Immediate migration policy

The original `period` column in `data/catalog/documents.csv` is retained for backward compatibility. New balancing shards should include `era_code`. Before the first analysis release, a migration script will assign `era_code` to all object-level records and report unresolved dates rather than guessing them.

## Epistemic constraint

`era_code != causal_period`

A concentration of a pedagogical term within an era is a descriptive pattern. Historical explanation requires source criticism, institutional context, regional comparison and validation of the underlying fragments.
