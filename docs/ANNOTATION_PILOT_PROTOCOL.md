# PDHD human annotation pilot protocol

## Purpose

The first PDHD human-validation pilot is designed to test whether the historical-pedagogical categories can be applied reproducibly by people who did not jointly construct every coding decision. It is **not** a substantive historical study and does not convert the current cohort into a representative sample.

The pilot begins only after the cohort gate in `PDHD_U1_COHORT_STATUS.md` is met.

## Sampling design

The target pilot contains **24 documents** selected by stratified purposive sampling. No publication may contribute more than 6 documents. The selection must include E1 and E3, rural/postrevolutionary material, at least three geographic origins outside Mexico City and at least three documentary types.

For the first reliability batch, PDHD will use **96 fixed fragments**: four fragments per document. This is an operational pilot size, not a claim of universal statistical sufficiency.

Fragment sampling should mix:

- candidate-positive fragments located through transparent lexical or metadata cues;
- fragments selected without regard to a target category, to avoid a corpus made only of expected positives;
- historically salient passages identified during source criticism;
- at least one fragment per document that can legitimately receive `none/unclear` for a target field.

The sampling mechanism and random seed, when random selection is used, must be versioned.

## Separation of tasks

PDHD separates **span identification** from **label assignment**.

### Pilot A — fixed-span label reliability

A preparation pass freezes the source location and fragment boundaries. Coders receive the same fragment and independently assign labels. This is the first pilot because it tests the taxonomy without confounding disagreement over where a fragment begins or ends.

### Pilot B — span detection reliability

After the taxonomy is stable, a smaller second task asks coders to identify relevant passages directly from pages. Agreement will be assessed with overlap-based measures rather than forcing a nominal reliability statistic onto a boundary-detection problem.

## Coders

At least **two human coders** independently code the reliability batch. Ideally, at least one coder should not have participated in the construction of the taxonomy. This follows the reproducibility concern noted in content-analysis methodology: coders who built a scheme together can share tacit assumptions that inflate apparent reliability.

A third expert may adjudicate disagreements after the independent reliability calculation.

LLM outputs, search heuristics and automated classifiers may generate candidates, but they **do not count as human coders** and their labels must not be visible to coders during the blind reliability round.

## Calibration

Before the reliability batch, coders complete a **12-fragment calibration set**. They discuss disagreements, revise definitions and add examples to the annotation manual.

Calibration fragments are excluded from the final reliability calculation.

The codebook is then frozen as a versioned pilot release. No category definition may be changed during the independent round without invalidating and rerunning the affected reliability test.

## Core fields

Each fixed fragment receives the following fields.

### `pedagogical_act_primary`

One primary historical teaching act when supported by the passage, for example `explicar`, `preguntar`, `examinar`, `corregir`, `castigar`, `premiar`, `mostrar`, `leer`, `dictar`, `observar`, `organizar`, `clasificar`, `adaptar` or `registrar`. A coder may use `none` or `unclear`.

Secondary acts may be stored separately, but primary-act reliability is calculated on one nominal value.

### `dimension`

Multi-label thematic dimensions such as `teaching_method`, `assessment`, `discipline`, `teacher_authority`, `teacher_training`, `rurality`, `indigenous_education`, `inclusion_difference` and `professional_identity`.

Because this field is multi-label, agreement is calculated per dimension as a binary decision and supplemented with set-overlap measures. PDHD does not collapse the entire multi-label set into a misleading single nominal category.

### `normativity`

Controlled values:

- `prescriptive` — instructs or recommends what should be done;
- `descriptive` — describes a practice or situation without itself prescribing it;
- `testimonial` — reports first-person or attributed practitioner experience;
- `policy_normative` — establishes or communicates an institutional rule;
- `mixed` — more than one mode is inseparable in the fixed fragment;
- `unclear`.

The distinction is central because `prescription != observed_practice`.

### `actor`

Primary actor of the pedagogical action: `teacher`, `student`, `inspector`, `director`, `family`, `community`, `state_authority`, `other`, `unclear`.

### `target`

Primary target or recipient: `student`, `teacher`, `family`, `community`, `institution`, `self`, `other`, `unclear`.

### `evidence_confidence`

Coder confidence is descriptive metadata, not evidence of correctness: `high`, `medium`, `low`.

## Independent coding rules

Coders work independently and do not discuss pilot items until the reliability snapshot is frozen. They receive source citation and enough page context to understand the passage, but they do not receive model predictions or another coder's labels.

Every code must remain linked to `fragment_id`, `document_id`, page/localizer, coder ID, codebook version and timestamp.

Missing access or illegible text is coded as an evidence problem, not guessed.

## Reliability statistics

PDHD uses **Krippendorff's alpha** for nominal single-label fields because it is a chance-corrected reliability measure that can accommodate more than two coders and missing values. Krippendorff's methodological work emphasizes that reliability must be demonstrated before conclusions are trusted; later annotation-quality research also warns that high agreement alone does not guarantee annotation quality and should be paired with manual inspection and adjudication.

Predeclared decision rule:

- `alpha >= 0.80`: field may proceed to the next pilot stage;
- `0.667 <= alpha < 0.80`: provisional; revise definitions and run another independent batch before substantive use;
- `alpha < 0.667`: stop; the field is not reliable enough for analytical use in its current form.

These thresholds are conventions, not laws of nature. PDHD reports the coefficient, sample size, missingness and preferably a bootstrap confidence interval rather than only a pass/fail label.

For `dimension`, each dimension is represented as a binary field and evaluated separately; macro summaries and Jaccard set similarity are secondary diagnostics.

Confusion matrices must be inspected for fields with multiple categories, because an acceptable aggregate coefficient can conceal a systematically confused pair of labels.

## Adjudication and gold labels

Reliability is calculated **before adjudication**. After that snapshot, disagreements are reviewed by an expert adjudicator using the frozen source evidence.

The adjudicated value becomes `gold_label` for the pilot dataset, while original coder responses remain preserved. Adjudication never overwrites independent annotations.

If adjudication reveals a category-definition defect, the codebook receives a new version and the affected reliability batch is rerun; the old batch remains part of provenance.

## Model use after the pilot

An automated classifier may be evaluated only after a stable human gold set exists. Model predictions must be stored separately from human labels.

`model_label != human_validation`

The first valid model evaluation must use held-out human-validated fragments and report class-level performance, not only aggregate accuracy. Model-assisted annotation can be considered later, but model suggestions should not be shown during a reliability test intended to measure independent human application of the codebook.

## References informing the reliability design

- Krippendorff, K. (2004). *Reliability in Content Analysis: Some Common Misconceptions and Recommendations*. Human Communication Research, 30(3), 411–433. DOI: 10.1111/j.1468-2958.2004.tb00738.x
- Hayes, A. F., & Krippendorff, K. (2007). *Answering the Call for a Standard Reliability Measure for Coding Data*. Communication Methods and Measures, 1(1).
- Recent review of annotation quality management: <https://direct.mit.edu/coli/article/50/3/817/120233/Analyzing-Dataset-Annotation-Quality-Management-in>

## Gate

The pilot is successful only if the categories are both **reliably applicable** and **historically interpretable after source criticism**. A numerical agreement threshold cannot substitute for the latter.
