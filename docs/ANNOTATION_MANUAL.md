# Annotation manual 0.2

## Unit of annotation

Annotate the smallest fragment that retains enough context to identify a pedagogically meaningful act, norm, representation or institutional relation. Do not reduce the fragment so far that the historical meaning depends on omitted clauses.

The source location is part of the annotation. Every fragment must remain traceable to `document_id`, page or equivalent locator, and the evidence surface used by the coder.

## General rule

**Code what the source supports, not what the historian expects to find.** A pedagogical genre does not by itself prove that an act occurred, that a prescription was followed or that an institutional policy reached classroom practice.

`prescription != observed_practice`

`model_label != human_validation`

`search_hit != historical_claim`

## Pedagogical dimensions

Version 0.2 treats dimensions as **multi-label** because a single historically meaningful fragment may simultaneously concern, for example, method, discipline and teacher authority.

Use the controlled codes in `data/taxonomy/pedagogical_dimensions.csv`. For each dimension, record `1` only when the fragment provides affirmative evidence for that dimension. Record `0` when it does not. Do not force a primary dimension merely for convenience.

The current dimension set is:

- `teaching_method`
- `teacher_authority`
- `discipline`
- `assessment`
- `materials`
- `lesson_organization`
- `teacher_training`
- `inspection_supervision`
- `rurality`
- `indigenous_education`
- `inclusion_difference`
- `gender`
- `student_conception`
- `professional_identity`
- `school_community`
- `pedagogical_change`

## Pedagogical act

Use the `act_code` values in `data/taxonomy/pedagogical_acts.csv`, not free-text synonyms.

Assign `pedagogical_act_primary` only when an action is explicit or strongly recoverable from the wording. Do not infer an act merely because a document belongs to a pedagogical genre.

If more than one act is genuinely present, select the act that structures the fragment as `pedagogical_act_primary` and record additional acts in the secondary field. Use `none` when no pedagogical act is present and `unclear` when an act may be present but the evidence does not support a defensible choice.

Examples of controlled codes include `explain`, `ask`, `examine`, `correct`, `punish`, `reward`, `demonstrate`, `read`, `dictate`, `observe`, `organize`, `classify`, `adapt`, `record`, `repeat`, `memorize`, `practice` and `guide`.

## Normativity / evidentiary mode

`normativity` records **what kind of claim about pedagogical action the fragment makes**. It is not a truth score.

Use one of these values:

- `prescriptive`: recommends, advises or instructs what a teacher or other actor should do, without itself constituting a formal institutional rule.
- `policy_normative`: states, transmits or enforces an official rule, regulation, programmatic obligation or institutional requirement.
- `descriptive`: describes a method, arrangement, role or pedagogical situation without clearly asserting that a concrete practice occurred and without directing that it should occur.
- `reported_practice`: states that a practice occurred, but the fragment is a report rather than a direct contemporaneous observation record.
- `observed_practice`: records a practice from an evidentiary setting that explicitly supports contemporaneous observation. Use sparingly; ordinary narrative description is not enough.
- `testimonial`: first-person or explicitly attributed practitioner testimony about what the actor did, experienced or encountered.
- `analytical`: interprets, theorizes or argues about practice rather than prescribing or reporting a concrete act.
- `mixed`: two or more modes are inseparable within the fixed fragment and reducing the span would destroy the historical meaning.
- `unclear`: the evidentiary mode cannot be defended from the available text.

### Boundary rule: `prescriptive` vs `policy_normative`

Use `policy_normative` only when the fragment is tied to an institutional authority, formal instruction, regulation, official program or explicit requirement. General pedagogical advice remains `prescriptive` even if written by an influential educator.

### Boundary rule: `reported_practice` vs `testimonial`

Use `testimonial` when the speaker or attributed practitioner reports their own experience. Use `reported_practice` when the source reports that another actor or group carried out a practice.

### Boundary rule: `reported_practice` vs `observed_practice`

`observed_practice` requires explicit evidence that the statement derives from contemporaneous observation, inspection or equivalent direct recording. Do not upgrade a confident narrative to observation merely because it is detailed.

## Actor

Code the primary actor responsible for the pedagogical act or normative expectation:

`teacher`, `student`, `inspector`, `director`, `family`, `community`, `state_authority`, `other`, `unclear`.

If a rule is issued by the state but directs teachers, `actor` refers to the actor expected to perform the pedagogical action; institutional authorship can be retained in document metadata.

## Target

Code the primary recipient or object of the action:

`student`, `teacher`, `family`, `community`, `institution`, `self`, `other`, `unclear`.

Do not assume `student` as the target merely because the source is educational.

## Evidence confidence

`evidence_confidence` records the coder's confidence in applying the code to the available evidence: `high`, `medium`, `low`.

Confidence is diagnostic metadata and must not be interpreted as historical truth or as a substitute for agreement testing.

## Access and legibility problems

If the source is inaccessible, the scan is illegible or the fragment boundary lacks enough context, record the problem explicitly. Do not fill missing evidence through contextual guessing.

## Validation states

Automated or provisional coding is `unvalidated`.

Independent human coding is stored as coder-specific annotation and must not overwrite another coder's response.

After reliability is calculated, an adjudicator may produce an adjudicated `gold_label`. Original coder responses remain preserved.

A human reviewer may also mark an annotation `rejected` or `needs_review`. Human validation refers to the **coding decision**, not to the historical truth of every statement contained in the source.

## Reliability

The procedures for calibration, blind independent coding, Krippendorff's alpha, multi-label agreement and adjudication are defined in `docs/ANNOTATION_PILOT_PROTOCOL.md`.

No automated classifier is promoted beyond candidate generation until a stable human-validated pilot exists.
