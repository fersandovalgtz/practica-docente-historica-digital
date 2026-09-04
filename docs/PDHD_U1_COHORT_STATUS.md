# PDHD-U1 cohort status

Reference cut: **2026-09-03**

## Current thresholds

| Layer | Count | Status |
|---|---:|---|
| Registered discovery candidates | 25 | threshold reached |
| Object-level documents | 62 | stabilization in progress |
| Issue-level leads awaiting primary resolution | 17 | active balancing queue |
| Sources with explicit rights policy | 10 / 10 | complete at source-policy level |
| Registered chronology conflicts | 2 | explicitly preserved |
| Human-validated pedagogical fragments | 0 | not started |

The original 50-document threshold established that PDHD-U1 could sustain object identity, provenance, rights and annotation workflows. The first balancing wave has now increased the object union to **62 records** without treating raw count as representativeness.

## Composition of the 62-document union

PDHD currently treats `data/catalog/documents.csv` and `data/catalog/documents_balancing_w1.csv` as two validated shards of one object catalog. The separation is temporary and makes the balancing intervention auditable.

### By evidence source

| Source | Documents | Share |
|---|---:|---:|
| BVM-CERVANTES | 40 | 64.5% |
| UNAM-RI | 8 | 12.9% |
| HNDM | 7 | 11.3% |
| INTERNET-ARCHIVE | 7 | 11.3% |

The earlier 80% dependence on BVM-CERVANTES has fallen to 64.5%. This remains too concentrated for longitudinal inference, but the direction of correction is explicit and measurable.

### By publication

| Publication | Documents |
|---|---:|
| La Enseñanza Normal | 20 |
| La Enseñanza Moderna | 20 |
| El Maestro | 7 |
| La Escuela moderna | 5 |
| Revista de la Instrucción Pública Mexicana | 4 |
| La Enseñanza primaria | 3 |
| La Enseñanza Objetiva | 1 |
| El Escolar Mexicano | 1 |
| Revista Mexicana de Educación | 1 |

## What balancing wave 1 changed

The first balancing wave deliberately added two missing historical poles.

First, **five object-level records from _La Escuela moderna_** provide additional pre-1900 pedagogical press, with direct UNAM repository identifiers for 1889–1891.

Second, **seven records from _El Maestro. Revista de Cultura Nacional_** introduce the early-SEP and postrevolutionary cultural-educational project. Exact day-level chronology is not fabricated: where only year or month is supported, the date remains at that precision.

A separate `issue_leads.csv` now records unresolved but bibliographically supported issues of _La Escuela moderna_, _El Maestro Rural_ and _Revista de Educación_. These leads do not count as object-level documents until a sufficiently stable primary locator is found.

## Chronology integrity

Two source disagreements are now formally registered in `data/catalog/chronology_conflicts.csv`:

- the start chronology of _La Enseñanza Normal_;
- the day-level date of _El Maestro_, tomo I, núm. 1.

The rule is conservative: **precision is reduced rather than disagreement being silently normalized**.

## Canonical analytical eras

The repository now distinguishes narrative historical ranges from quantitative sampling strata. `docs/PERIODIZATION_PROTOCOL.md` defines seven non-overlapping `era_code` values from E1 (1870–1910) through E7 (2001–2026). New balancing records include `era_code`; the legacy core catalog will be migrated before an analysis release.

## Epistemic status

The current set remains a **stabilizing cohort**, not an analytical sample.

`object_count_threshold_reached != historical_representativeness`

`catalog_ready != annotation_ready`

`digitized_series_density != historical_importance`

`bibliographic_issue_reference != primary_object_resolved`

The two 1904–1907 pedagogical series still account for 40 of 62 objects. Any historical model trained or summarized directly on the present union would therefore inherit a major availability bias.

## Remaining stabilization requirements

The next balancing pass should prioritize three gaps.

1. **Rural and postrevolutionary primary objects.** Resolve primary digital localizers for _El Maestro Rural_ and _Revista de Educación_. Peer-reviewed scholarship already supplies issue/date leads, but these remain leads until primary resolution.
2. **Regional pre-1900 press.** Resolve more objects from Veracruz, Guanajuato, Jalisco and Aguascalientes, particularly _México Intelectual_ and Lancasterian or teacher-facing publications.
3. **Documentary-type diversity.** Add manuals, inspection/supervision material, teacher-training documents and official guidance so periodical density does not define the object of study by convenience.

## Gate for the first human annotation pilot

The 24-document human pilot should begin only when the sample can include at minimum:

- E1 pre-1911 professional/pedagogical press;
- E3 early SEP/postrevolutionary publications;
- E3/E4 rural-teacher material with primary localizers;
- at least three geographic origins outside Mexico City;
- at least three documentary types;
- no single publication contributing more than 25% of the pilot.

The pilot will test `pedagogical_act`, `dimension`, `normativity`, `actor`, `target`, evidence localization and inter-annotator agreement before any automated classifier is treated as more than candidate generation.

## Decision

PDHD-U1 has advanced from the **50-object infrastructure seed** to a **62-object stabilization union** plus a 17-lead balancing queue. Issue #1 should remain open. The next meaningful threshold is not 100 objects by accumulation; it is a sufficiently diversified object union that can support a defensible 24-document human-validation pilot.
