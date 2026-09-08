# PDHD-U1 — pre-validation state 0.1

Reference cut: 2026-09-07.

PDHD-U1 has completed the documentary freeze gate at 96/96 fragments. Human semantic validation has not started and remains at 0 coded fragments.

The pre-validation state is intentionally split into three frozen layers:

- the 96-fragment documentary pilot;
- the 12-fragment calibration selection (`PDHD-CAL-0.1-20260907`);
- the complementary 84-fragment reliability reserve (`PDHD-RR-0.1-20260907`).

The 84-fragment reserve is not a formal reliability package. It fixes sample identity only. A formal coder-facing reliability round may be generated only after real human calibration has occurred and an independent-round codebook has been versioned and frozen.

The pre-label analytical commitments are recorded in `docs/ANALYSIS_PLAN_0_1.md`. They distinguish descriptive corpus analysis from population inference, preserve document-level dependence, forbid semantic imputation of inaccessible cases and require exploratory questions discovered after labeling to be identified as exploratory.

No automated or model-produced annotation may be reclassified as human validation. No reliability coefficient or gold label exists at this stage.
