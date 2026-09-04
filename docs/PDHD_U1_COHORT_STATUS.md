# PDHD-U1 cohort status

Reference cut: **2026-09-03**

## Current thresholds

| Layer | Count | Status |
|---|---:|---|
| Registered discovery candidates | 25 | threshold reached |
| Object-level documents | 66 | stabilization in progress |
| Issue-level leads | 21 total / 19 unresolved | active balancing queue |
| Sources with explicit rights policy | 11 / 11 | complete at source-policy level |
| Registered chronology conflicts | 2 | explicitly preserved |
| Human-validated pedagogical fragments | 0 | not started |

The original 50-document threshold established that PDHD-U1 could sustain object identity, provenance, rights and annotation workflows. The balancing work has now increased the validated object union to **66 records** without treating raw count as representativeness.

## Composition of the 66-document union

PDHD currently treats `data/catalog/documents.csv` and `data/catalog/documents_balancing_w1.csv` as two validated shards of one object catalog. The separation is temporary and makes the balancing intervention auditable.

### By evidence source

| Source | Documents | Share |
|---|---:|---:|
| BVM-CERVANTES | 40 | 60.6% |
| UNAM-RI | 11 | 16.7% |
| HNDM | 7 | 10.6% |
| INTERNET-ARCHIVE | 7 | 10.6% |
| BIBMX-FR | 1 | 1.5% |

The original 80% dependence on BVM-CERVANTES has fallen to 60.6%. This remains too concentrated for longitudinal inference, but the correction is explicit and measurable.

### By publication or documentary object

| Publication / object | Documents |
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
| México intelectual | 1 |
| El Instructor | 1 |
| El Periquito | 1 |
| El esfuerzo educativo en México | 1 |

## What the balancing work changed

The first balancing wave deliberately added historical poles that were missing from the initial infrastructure seed.

First, **five object-level records from _La Escuela moderna_** provide additional pre-1900 pedagogical press, with direct UNAM repository identifiers for 1889–1891.

Second, **seven records from _El Maestro. Revista de Cultura Nacional_** introduce the early-SEP and postrevolutionary cultural-educational project. Exact day-level chronology is not fabricated: where only year or month is supported, the date remains at that precision.

Third, direct UNAM object records now add **_México intelectual_**, **_El Instructor_** and **_El Periquito_**, bringing document-level regional evidence from Veracruz, Aguascalientes and Campeche into the stabilized union. This materially improves geographic coverage, although it does not yet solve the rural/postrevolutionary gap.

Fourth, the institutional Fondo Reservado de la Biblioteca México contributes **_El esfuerzo educativo en México_ (1928)**, a two-volume SEP analytical-critical report on federal educational organization and policy during 1924–1928. It is registered as `official_report`, which creates a documentary type distinct from issue-level and hemerographic objects and begins to reduce the project's dependence on periodical press.

A separate `issue_leads.csv` now holds **21 bibliographically supported leads**. Two have already been resolved to object-level records and retain their lead-to-document linkage; 19 remain unresolved. High-priority unresolved leads include _El Maestro Rural_, _Revista de Educación_, _El Protector de la infancia_ and _La Educación_. Leads do not count as documents until a sufficiently stable object locator is found.

## Chronology integrity

Two source disagreements are formally registered in `data/catalog/chronology_conflicts.csv`:

- the start chronology of _La Enseñanza Normal_;
- the day-level date of _El Maestro_, tomo I, núm. 1.

The rule is conservative: **precision is reduced rather than disagreement being silently normalized**.

## Canonical analytical eras

The repository distinguishes narrative historical ranges from quantitative sampling strata. `docs/PERIODIZATION_PROTOCOL.md` defines seven non-overlapping `era_code` values from E1 (1870–1910) through E7 (2001–2026). New balancing records include `era_code`; the legacy core catalog will be migrated before an analysis release.

## Epistemic status

The current set remains a **stabilizing cohort**, not an analytical sample.

`object_count_threshold_reached != historical_representativeness`

`catalog_ready != annotation_ready`

`digitized_series_density != historical_importance`

`bibliographic_issue_reference != primary_object_resolved`

The two 1904–1907 pedagogical series still account for 40 of 66 objects. Any historical model trained or summarized directly on the present union would therefore inherit a major availability bias.

## Human-validation infrastructure

The repository now contains `docs/ANNOTATION_PILOT_PROTOCOL.md`, `docs/ANNOTATION_MANUAL.md` version 0.2, `data/samples/annotation_pilot_template.csv` and `scripts/annotation_agreement.py`.

The planned first reliability study uses 24 stratified documents and 96 fixed fragments, with a separate 12-fragment calibration set. At least two human coders work independently; model outputs are excluded from the blind coding round. Single-label nominal fields use Krippendorff's alpha, multi-label dimensions are evaluated per dimension with additional set-overlap diagnostics, and adjudication occurs only after the independent reliability snapshot is frozen.

The agreement calculator is executed in CI through a self-test, so the reliability workflow itself is versioned and checked alongside catalog integrity.

## Remaining stabilization requirements

The next balancing pass should prioritize three gaps.

1. **Rural and postrevolutionary primary objects.** Resolve primary digital localizers for _El Maestro Rural_ and _Revista de Educación_. Peer-reviewed scholarship already supplies issue/date leads, but these remain leads until primary resolution.
2. **Regional pre-1900 depth.** The corpus now has direct regional objects from Veracruz, Aguascalientes and Campeche, but each is represented thinly. Resolve additional issues from these series and from Guanajuato and Jalisco.
3. **Documentary-type depth.** The formal minimum of three object types can now be met (`issue`, `hemerographic_object`, `official_report`), but the third type is represented by only one object. Manuals, inspection/supervision material, teacher-training documents and additional official guidance should be added before broader comparative claims.

## Gate for the first human annotation pilot

The 24-document human pilot should begin only when the sample can include at minimum:

- E1 pre-1911 professional/pedagogical press;
- E3 early SEP/postrevolutionary publications;
- E3/E4 rural-teacher material with primary localizers;
- at least three geographic origins outside Mexico City;
- at least three documentary types;
- no single publication contributing more than 25% of the pilot.

The geographic and formal documentary-type conditions can now be satisfied at object level. The **hard blocking condition is rural-teacher primary resolution**, while documentary-type depth remains a quality concern rather than a binary gate failure.

## Decision

PDHD-U1 has advanced from the 50-object infrastructure seed to a **66-object stabilization union** plus a 19-item unresolved balancing queue. Issue #1 should remain open. The next meaningful threshold is not 100 objects by accumulation; it is resolution of enough rural/postrevolutionary primary material to support a defensible 24-document human-validation pilot.
