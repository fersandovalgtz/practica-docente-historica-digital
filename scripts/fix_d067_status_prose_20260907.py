#!/usr/bin/env python3
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "docs" / "PDHD_U1_COHORT_STATUS.md"
text = path.read_text(encoding="utf-8")
text = text.replace(
    "The current 84 frozen units demonstrate that the pipeline works across HNDM, BVMC, Internet Archive and Google Books primary interfaces and can reconcile independent issue identity with an alternate primary scan.",
    "The current 88 frozen units demonstrate that the pipeline works across HNDM, BVMC, Internet Archive and Google Books primary interfaces and can reconcile independent issue identity with an alternate primary scan.",
)
old = (
    "The project is now at **95/96 localized** and **84/96 frozen**. Recent primary-object recovery has expanded the frozen package while preserving the unlocalized complement at 1. "
    "The next quantitative localization checkpoint is **95/96**, while the stronger scientific priority remains completing document batches without weakening the evidence hierarchy."
)
new = (
    "The project is now at **96/96 localized** and **88/96 frozen**. Recent primary-object recovery has expanded the frozen package while preserving the unlocalized complement at 0. "
    "The localization gate is complete at **96/96**; the stronger scientific priority is converting the remaining eight localized fragments into fixed primary-inspected spans without weakening the evidence hierarchy."
)
assert old in text
path.write_text(text.replace(old, new), encoding="utf-8")
print("Synchronized cohort decision prose to 96/96 localized, 88/96 frozen, 0 gaps.")
