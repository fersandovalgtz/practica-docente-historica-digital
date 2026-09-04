# PDHD-U1 cohort status

Reference cut: **2026-09-03**

## Current thresholds

| Layer | Count | Status |
|---|---:|---|
| Registered discovery candidates | 25 | threshold reached |
| Object-level documents | 50 | seed threshold reached |
| Sources with explicit rights policy | 9 / 9 | complete at source-policy level |
| Human-validated pedagogical fragments | 0 | not started |

The 50-document threshold means that PDHD-U1 now has enough object-level material to test catalog, provenance, rights and annotation workflows. It **does not** mean that the current 50 objects constitute a balanced historical sample.

## Composition of the 50-document seed

### By evidence source

| Source | Documents | Share |
|---|---:|---:|
| BVM-CERVANTES | 40 | 80% |
| HNDM | 7 | 14% |
| UNAM-RI | 3 | 6% |

### By publication

| Publication | Documents |
|---|---:|
| La Enseñanza Normal | 20 |
| La Enseñanza Moderna | 20 |
| Revista de la Instrucción Pública Mexicana | 4 |
| La Enseñanza primaria | 3 |
| La Enseñanza Objetiva | 1 |
| El Escolar Mexicano | 1 |
| Revista Mexicana de Educación | 1 |

## Epistemic status

The current set is a **seed cohort**, not an analytical sample.

`object_count_threshold_reached != historical_representativeness`

`catalog_ready != annotation_ready`

`digitized_series_density != historical_importance`

The concentration in two pedagogical series from 1904–1907 is useful for testing serial continuity and annotation mechanics, but it would bias any longitudinal claim if treated as representative of Mexican teaching practice.

## Stabilization requirements before comparative analysis

Before PDHD-U1 is described as an analysis-ready historical cohort, the next expansion should reduce the present temporal, institutional and geographic concentration. Priority additions are:

1. **Pre-1900 teaching practice:** more issue-level objects from *La Enseñanza Objetiva*, *El Escolar Mexicano*, *México Intelectual*, *La Escuela moderna*, Lancasterian publications and regional pedagogical press.
2. **Postrevolutionary and rural teaching:** primary issue-level objects from *El Maestro*, *El Maestro Rural*, *Revista Mexicana de Educación* and *Revista de Educación*.
3. **Regional diversity:** objects from Veracruz, Guanajuato, Jalisco, Aguascalientes and other states rather than allowing Mexico City publications to define the corpus by availability.
4. **Documentary-type diversity:** professional journals, official publications, teacher-training press, school-facing periodicals and manuals should remain analytically distinguishable.
5. **Rights resolution:** object-level reuse conditions must be preserved separately from source discovery and must never be inferred from mere digital availability.

## Proposed first annotation pilot

A first human-validation pilot should be selected only after the next balancing pass. The recommended design is a **24-document stratified pilot**, with documents chosen across time, documentary type and region. The pilot should test the stability of `pedagogical_act`, `dimension`, `normativity`, `actor`, `target` and `validation_status` before any automated classifier is promoted beyond candidate generation.

## Decision

PDHD-U1 has reached **50 object-level records**, so the infrastructure test has moved from discovery into cohort stabilization. Issue #1 should remain open until the seed is sufficiently diversified to support the first stratified human-annotation pilot.
