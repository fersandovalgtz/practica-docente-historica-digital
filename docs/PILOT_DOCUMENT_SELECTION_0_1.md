# PDHD pilot document selection 0.1

Reference cut: **2026-09-03**

## Decision

PDHD now freezes a first **24-document stratified selection** for the human-validation pilot. This is a sampling decision for testing the annotation system; it is not a claim that the selected documents represent all Mexican teaching practice.

The selection is stored in `data/samples/pilot_document_selection_0_1.csv` and targets four fixed fragments per document, for a total of **96 reliability fragments**, plus the separate 12-fragment calibration set defined in `ANNOTATION_PILOT_PROTOCOL.md`.

## Why the gate can now open

The previous blocking condition was the absence of primary-localized rural-teacher material. That condition is now resolved by several direct source objects, especially:

- `PDHD-D000067` — *El papel social del maestro rural* (SEP, 1925), cataloged by HathiTrust with full view;
- `PDHD-D000068` — *El sistema de escuelas rurales en México* (SEP, 1927), full-view HathiTrust object;
- `PDHD-D000069` — *Las misiones culturales en 1927: Las escuelas normales rurales* (SEP, 1928), full-view HathiTrust object;
- `PDHD-D000071` — *Las misiones culturales, 1932-1933* (SEP, 1933), stable Google Books object with searchable internal passages;
- `PDHD-D000072` and `PDHD-D000073` — SEP institutional memories with direct sections on missions, rural schools, normal education and inspection;
- `PDHD-D000074` and `PDHD-D000075` — Cardenista SEP memories with rural, regional-normal and supervision material.

These are primary documentary objects with stable digital identities. They do not depend on treating later historiography as if it were the historical source itself.

## Stratification

The 24-document selection contains:

| Era | Documents | Role |
|---|---:|---|
| E1 — 1870–1910 | 10 | pedagogical press, normalism, objective teaching, professional and regional educational cultures |
| E3 — 1921–1934 | 12 | early SEP, rural schooling, missions, teacher role, institutional reporting and policy design |
| E4 — 1935–1940 | 2 | Cardenista rural-normal administration and supervision |

The pilot deliberately does **not** attempt proportional national representation. E2 is omitted from this first reliability batch because the immediate methodological contrast is between the mature late-nineteenth/early-twentieth pedagogical press and postrevolutionary state/rural documentary regimes. E2 should enter a later substantive sample once the annotation scheme is stable.

## Geographic condition

At object level, the selection includes at least three clearly identified origins outside Mexico City:

- Campeche — *El Periquito*;
- Aguascalientes — *El Instructor*;
- Xalapa, Veracruz — *México intelectual*.

These regional objects are not treated as sufficient evidence of national geographic representativeness. They satisfy the pilot requirement that the reliability exercise not be built exclusively from Mexico City materials.

## Documentary-type condition

The selection contains more than the minimum three documentary types:

- periodical issues;
- hemerographic objects;
- official reports;
- teacher guidance;
- institutional monographs;
- policy proposals.

This matters because annotation categories should survive changes in documentary regime. A coding scheme that works only on pedagogical journals would be too narrow for PDHD's historical objective.

## Publication concentration rule

No publication contributes more than six of the 24 selected documents. *El Maestro* contributes four. Every other selected publication contributes one document except the SEP memory series, which is represented by multiple distinct annual/volume objects rather than one serial run dominating the pilot.

## Access and rights condition

Selection for annotation does not override source rights. Before fragment freezing, every selected document receives an access-mode decision:

- public source text may be transcribed only when the reuse basis permits it;
- otherwise the pilot stores short research excerpts only when legally defensible, or stores coder-local text with public metadata/localizers;
- HNDM remains `metadata_only` in the public repository unless a stronger object-level permission basis is documented;
- HathiTrust and Google Books full-view availability is treated as research access, not as an automatic license to republish scans or OCR.

## Fragment-freeze protocol

The next step is not coding. It is **fragment freezing**.

For each of the 24 documents, the preparation pass must identify four fixed fragments under the following design:

1. one passage with an explicit pedagogical action or instructional prescription;
2. one passage bearing on professional identity, authority, supervision, evaluation or organization;
3. one historically salient passage selected through source criticism rather than keyword expectation;
4. one control passage capable of receiving `none` or `unclear` for at least one target field.

The four fragments must be stored with page/localizer, transcription status, access basis, selection rationale and an immutable `fragment_id`. The preparation pass may use search and model assistance to find candidates, but proposed labels must not be visible to the human coders.

## Pilot start condition

The **document-selection gate is passed**. Human coding begins only after all 96 fixed fragments are frozen and checked for source location, readability and rights-compatible handling.

`document_selection_ready != annotation_started`

`primary_source_resolved != source_text_republishable`

`pilot_reliability != historical_representativeness`
