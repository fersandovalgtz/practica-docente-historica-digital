# Práctica Docente Histórica Digital (PDHD): a provenance-first corpus for reproducible research on Mexican teaching-practice history

**Article type:** Data paper — pre-submission draft 0.1  
**Author:** Fernando Sandoval Gutiérrez  
**ORCID:** https://orcid.org/0000-0002-3168-6725  
**Project:** Práctica Docente Histórica Digital (PDHD)  
**Repository:** https://github.com/fersandovalgtz/practica-docente-historica-digital  
**Dataset DOI:** *to be added after archival deposit of the cited pre-validation snapshot*  
**Scientific state described:** `PDHD-U1-PREVALIDATION-0.1-20260907`

## Abstract

Práctica Docente Histórica Digital (PDHD) is an open research infrastructure for constructing reproducible evidence about the history of teaching practice in Mexico from heterogeneous educational print sources. We describe the first controlled documentary pilot, PDHD-U1, and the provenance-first workflow used to transform repository records into stable research units without conflating digital availability, republication rights, documentary identity, fixed evidence boundaries, or semantic interpretation. The current pilot contains 24 selected documents and 96 fixed fragments. All 96 fragments are localized and frozen, while human semantic coding remains deliberately at zero. The repository preserves rights policies, unsuccessful retrieval attempts, chronology conflicts, source substitutions, deterministic calibration selection, and a pre-registered reliability reserve. PDHD-U1 therefore provides a reusable corpus-construction method and a reproducible pre-validation dataset rather than a completed benchmark of historical teaching practices.

**Keywords:** history of education; digital humanities; historical corpus; teaching practice; provenance; reproducibility

## 1. Background and research context

Historical research increasingly depends on digital repositories whose interfaces, metadata models, access conditions, and image-delivery mechanisms differ substantially. This heterogeneity creates a methodological problem before interpretation begins. A digitized object may be discoverable but not directly inspectable. A page may be visible but not legally redistributable. A search result may identify a relevant passage without providing a stable primary locator. A repository may also change its interface while the historical object remains extant. Treating these states as equivalent weakens source criticism and makes later computational analysis difficult to reproduce.

PDHD addresses this problem by separating documentary discovery from semantic interpretation. We build a traceable chain from source family to documentary identity, rights status, retrieval evidence, page-level localization, fixed fragment boundary, and only then future human annotation. This design follows the broader logic of FAIR data stewardship, in which reuse depends on findability, accessibility, interoperability, and explicit conditions of reuse (Wilkinson et al., 2016). It also reflects the importance of provenance for evaluating trust and derivation in digital objects, as formalized by the W3C PROV family (Moreau & Missier, 2013). In computational terms, PDHD adopts the principle that each result should remain connected to the procedure and version that produced it (Sandve et al., 2013).

The project focuses on a substantive historical question: how the act of teaching changes in Mexico and what documentary traces remain of instructional methods, evaluation, discipline, professional authority, materials, supervision, rural schooling, inclusion, and representations of teachers and pupils. The present data paper does not answer those semantic questions. It documents the infrastructure required to answer them without allowing retrieval convenience or automated classification to become historical evidence by default.

## 2. Documentary universe and pilot design

The wider repository currently records 25 documentary candidates and 78 documentary objects with identity and locators. Thirteen source families have an explicit operational rights policy. PDHD-U1 draws a controlled pilot of 24 documents from this larger stabilization cohort. The selected objects range from regional pedagogical periodicals to institutional monographs and official reports. They include material accessed through the Hemeroteca Nacional Digital de México, Biblioteca Virtual Miguel de Cervantes, Internet Archive, Google Books, and related discovery or crosswalk services.

Each selected document contributes four deterministic fragment slots, producing a target of 96 research units. The current selection contains 12 issues, two hemerographic objects, five official reports, three institutional monographs, one teacher-guidance volume, and one policy proposal. The pilot is intentionally non-probabilistic. It tests documentary diversity, temporal coverage, retrieval robustness, rights handling, fragment freezing, and future annotation procedures. Frequencies within PDHD-U1 therefore describe the corpus and must not be interpreted as national prevalence estimates for Mexican teaching practice.

| Documentary type | Selected documents |
|---|---:|
| Periodical issue | 12 |
| Hemerographic object | 2 |
| Official report | 5 |
| Institutional monograph | 3 |
| Teacher guidance | 1 |
| Policy proposal | 1 |
| **Total** | **24** |

The 24 selected documents are represented through 96 fixed fragment identities. At the pre-validation snapshot, all 96 are localized and all 96 are frozen. No fragment is human-coded. Twelve fragments form a deterministic calibration cohort, while the remaining 84 constitute a pre-registered reserve for a future formal reliability round. The 12/84 split is fixed before observing human semantic labels.

## 3. Provenance-first source recovery

PDHD treats retrieval as a research process rather than an invisible technical precondition. Structured retrieval records preserve the target object, source family, requested fragment or slot, result status, blocker, next route, and date of inspection. Failed routes are retained because they explain why a later source, edition, or interface path was used. They also make it possible to distinguish a temporary server failure from the nonexistence of a historical source.

This distinction is especially important in large digitization platforms. A URL that returns an error today does not establish that the underlying issue, volume, or archival object has disappeared. PDHD therefore models link health separately from documentary existence. A scheduled non-blocking audit classifies reachable resources, redirects, access restrictions, rate limits, server errors, timeouts, DNS errors, and other network states without allowing those observations to rewrite the historical catalog automatically.

Four document substitutions occur in the present pilot. Each substitution is versioned and records the outgoing object, replacement object, reason, effects on era, geography, document type, publication concentration, and the primary evidence supporting the decision. The substitutions preserve the sampling function of the original position rather than lowering the evidence threshold to retain an inaccessible object. This makes substitution itself part of the provenance record.

## 4. Rights-aware openness

PDHD distinguishes consultation from republication. The rights registry currently contains operational policies for 13 source families. For example, HNDM is handled under a conservative metadata-only public-commit policy, while several aggregators and repositories remain under object-level review requirements. Public availability of a PDF, page image, OCR derivative, or viewer endpoint is not treated as an automatic license to mirror that material in the corpus.

The public repository therefore prioritizes identifiers, bibliographic metadata, stable source URLs, page locators, fixed boundaries, retrieval provenance, derived research metadata, schemas, and validation code. When rights are unresolved or restrictive, PDHD does not commit facsimiles, full historical transcriptions, or source OCR merely because those materials can be technically retrieved. This approach interprets FAIR as a framework for responsible reuse rather than as a requirement to republish every underlying historical file. Comparable debates in archaeology show that FAIR practice must remain connected to disciplinary ethics, stewardship, and the conditions under which legacy data can be reused (Nicholson et al., 2023).

## 5. From locator to frozen fragment

The core methodological sequence is:

`locator -> directly inspected primary surface -> fixed boundary -> future human annotation`

A locator identifies a page, leaf, image, or equivalent primary surface. A frozen fragment then gives that evidence unit a stable fragment identifier and a fixed boundary. Freezing does not mean that a pedagogical interpretation has been validated. It means that future coders can be shown the same documentary unit instead of coding shifting search snippets or differently cropped passages.

The architecture also separates structural fragment records from semantic annotations. The fragment schema contains source-critical and boundary information. Human annotation has its own schema. Experimental model output is stored in a quarantined `machine_candidate` layer that cannot satisfy human-validation gates or create gold labels. This separation prevents a common form of benchmark contamination in which model suggestions become visible to human coders or are later mistaken for adjudicated labels.

## 6. Human-validation architecture

The project pre-registers the future human workflow even though no human semantic labels exist yet. A deterministic 12-item calibration package is selected from the frozen 96. It is intended for at least two independent human coders. Calibration responses will be used to diagnose ambiguity and revise the codebook. The calibration set is excluded from the subsequent formal reliability round.

The remaining 84 fragments are fixed as the reliability reserve. The repository refuses to generate the formal reliability package until exactly one codebook is registered as frozen for independent reliability and its Git blob hashes match the registered version. Phase 5 semantic analysis is gated even more strongly: it will not run without a human-adjudicated gold manifest that confirms formal reliability and excludes machine candidates. At the state described here, human-coded fragments equal zero, formal reliability has not started, and gold labels equal zero.

## 7. Data records, reproducibility, and technical validation

PDHD uses open text formats, primarily CSV, JSON, Markdown, and Python. A field-level data dictionary documents public data surfaces without requiring a user to reverse-engineer scripts. JSON schemas separate documents, structural fragments, human annotations, machine candidates, and future adjudicated gold annotations. Versioned scripts reconstruct deterministic selections and validate foreign keys, fragment identities, status counts, rights references, calibration blinding, codebook provenance, machine-output quarantine, and phase-gate conditions.

The scientific pre-validation snapshot `PDHD-U1-PREVALIDATION-0.1-20260907` pins a signed Git commit and tree together with a successful continuous-integration run. The snapshot records 24 selected documents, 96 target fragments, 96 localized fragments, 96 frozen fragments, 12 calibration fragments, 84 reliability-reserve fragments, zero human-coded fragments, and zero gold labels. Subsequent repository hardening does not retroactively change that scientific state.

## 8. Reuse potential

The current dataset supports several forms of reuse before semantic validation. Researchers can examine source-recovery strategies across historical repositories, compare the persistence of digital localizers, audit rights-aware corpus construction, study patterns of documentary availability, reproduce the 24-document pilot selection, inspect versioned substitutions, or build compatible tools against the published schemas. The repository can also serve as a testbed for methods that distinguish source identity from interface availability.

After human validation, the same fixed 96-fragment architecture can support historically cautious analyses of pedagogical acts and discourse. Because each fragment remains linked to its document, future analyses can account for within-document dependence rather than treating 96 fragments as 96 independent historical sources. A pre-written phase-5 pipeline already enforces this distinction through document-cluster resampling, but it remains closed until a legitimate gold set exists.

## 9. Limitations

PDHD-U1 is constrained by digitization history. Surviving and digitized educational print favors some institutions, regions, genres, and periods over others. Repository interfaces also introduce access asymmetries that are not properties of the historical record itself. The pilot does not solve these biases. It makes them more observable by preserving negative retrieval evidence, substitutions, rights constraints, and chronology conflicts.

The dataset is also deliberately incomplete at the semantic level. No claim about the prevalence, transformation, or accuracy of identified pedagogical practices is warranted from the current pre-validation state. Prescriptive discourse is not equivalent to observed classroom practice. Reported practice is not equivalent to direct observation. These distinctions remain explicit requirements for future coding and interpretation.

## 10. Data and code availability

The development repository is publicly available at https://github.com/fersandovalgtz/practica-docente-historica-digital. The canonical project citation is maintained in `CITATION.cff`. The exact pre-validation scientific state is recorded in `data/snapshots/prevalidation_snapshot_0_1.json`.

Before journal submission, the cited data snapshot should be deposited in a trusted archival repository and assigned a persistent identifier. That DOI should replace the placeholder in this manuscript. The archival deposit should preserve the distinction between PDHD-created metadata and third-party historical source materials that PDHD is not licensed to redistribute.

## Ethics and rights statement

The dataset described here is built from historical documentary sources and does not contain a human-subject intervention. Rights to third-party historical objects remain with their respective rights holders or institutions. PDHD publishes only those source-derived materials and metadata permitted by its documented rights policy and does not infer republication permission from technical accessibility.

## Author contribution

Fernando Sandoval Gutiérrez: Conceptualization; Methodology; Investigation; Data curation; Software; Project administration; Visualization; Writing — original draft; Writing — review and editing.

## References

Moreau, L., & Missier, P. (Eds.). (2013). *PROV-DM: The PROV Data Model*. W3C Recommendation. https://www.w3.org/TR/prov-dm/

Nicholson, C., Kansa, S., Gupta, N., & Fernandez, R. (2023). Will It Ever Be FAIR? Making Archaeological Data Findable, Accessible, Interoperable, and Reusable. *Advances in Archaeological Practice, 11*(1), 63–75. https://doi.org/10.1017/aap.2022.40

Sandve, G. K., Nekrutenko, A., Taylor, J., & Hovig, E. (2013). Ten Simple Rules for Reproducible Computational Research. *PLOS Computational Biology, 9*(10), e1003285. https://doi.org/10.1371/journal.pcbi.1003285

Wilkinson, M. D., Dumontier, M., Aalbersberg, I. J., et al. (2016). The FAIR Guiding Principles for scientific data management and stewardship. *Scientific Data, 3*, 160018. https://doi.org/10.1038/sdata.2016.18
