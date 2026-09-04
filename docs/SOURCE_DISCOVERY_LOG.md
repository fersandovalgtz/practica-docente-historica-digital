# Source discovery log

## 2026-09-03 — initial PDHD-U1 sweep

The first documentary sweep tested whether HNDM can support a historically meaningful corpus centered on teaching practice rather than only on general educational discourse. Four high-priority candidates were verified and entered in `data/catalog/source_candidates.csv`.

### La Voz de la instrucción

HNDM describes **La Voz de la instrucción** as *O sea el libro primero del maestro*, a weekly publication devoted to the progress of teaching and to the material and moral interests of the Mexican teaching profession. The descriptor records a first volume of 24 numbers in 1871. This is a core PDHD candidate because its declared audience and purpose place the teaching profession itself at the center of the documentary object.

Source descriptor: <https://hndm.iib.unam.mx/consulta/publicacion/verDescripcionDescarga/558ff9427d1e325230861576.pdf>

### La Enseñanza

HNDM records **La Enseñanza** for 1870–1876. The descriptor notes pedagogical content and characterizes the publication as an encyclopedic pedagogical resource intended to assist teachers in their work. It is therefore suitable for tracing method, pedagogical language, materials and the relationship between scientific knowledge and classroom instruction.

Source descriptor: <https://hndm.iib.unam.mx/consulta/publicacion/verDescripcionDescarga/558ff9307d1e32523086143b.pdf>

### La Educación

HNDM describes **La Educación** as the newspaper of the Sociedad de Enseñanza Popular, published in León between 1871 and 1873. The bibliographic description also documents the society's maintenance of adult night schools. The source is potentially useful for linking pedagogical discourse with popular education, examinations, institutional organization and community schooling.

Source descriptor: <https://hndm.iib.unam.mx/consulta/publicacion/verDescripcionDescarga/558ff92f7d1e325230861436.pdf>

### La Enseñanza Objetiva — 12 December 1891

A digitized issue dated 12 December 1891 identifies **La Enseñanza Objetiva** as a newspaper dedicated to the propagation and advancement of that system and to the civil and moral education of youth. The issue contains a model lesson of explained reading. This makes it especially valuable for the `pedagogical_act` layer because it preserves concrete sequences of questioning, defining and guiding pupil responses rather than only abstract educational commentary.

Digitized issue: <https://hndm.iib.unam.mx/consulta/publicacion/pdf/558a33397d1ed64f16922c93.pdf?palabras=>

## Rights decision

All four candidates remain `metadata_only` in the public repository until object-level reuse conditions are affirmatively resolved. HNDM's published conditions require conservative treatment of digital images and incorporation into systems. Candidate status therefore does not authorize facsimile or full-OCR redistribution.

## Next documentary target

The next sweep should expand from four candidates to at least **25 serial titles or high-value documentary objects**, then resolve individual issues/documents for the first stable 50–100-object PDHD-U1 cohort. Priority search axes are teacher profession, normal schools, inspection, objective teaching, examinations, discipline, rural teaching and pedagogical methods.

## 2026-09-03 — expansion to 25 candidates and object-level seed

The second sweep reached the first discovery threshold: **25 candidate serial titles or high-value documentary objects** are now registered in `data/catalog/source_candidates.csv`. The expansion deliberately combines primary institutional catalogs with a small number of high-quality secondary discovery records whose primary serial source still has to be resolved. Records with unresolved primary provenance are explicitly marked `secondary_verified_source_pending`; they are not silently promoted to primary-source status.

### Documentary clusters now represented

The candidate set now covers several historically meaningful clusters rather than one undifferentiated list of educational periodicals:

- **Lancasterian and popular instruction, 1870s:** *El Porvenir de la niñez*, *El Protector de la infancia*, *La Educación*, *El Sábado* and related child/teacher press.
- **Professional and pedagogical press, 1880s–1890s:** *El Escolar Mexicano*, *La Enseñanza Objetiva*, *La Escuela moderna*, *Revista de la Instrucción Pública Mexicana* and *México Intelectual*.
- **Normalismo and teacher professionalization, 1900s:** *La Enseñanza primaria*, *La Enseñanza Moderna*, *La Enseñanza Normal* and *El Magisterio Nacional*.
- **Postrevolutionary and rural-teacher culture, 1919–1930s:** *Revista Mexicana de Educación*, *El Maestro*, *El Maestro Rural* and *Revista de Educación*.

This structure makes it possible to compare not only vocabulary but documentary regimes: publications directed to children, organs of teaching societies, professional teacher journals, normal-school publications and state educational magazines.

### New evidence sources

The source registry was expanded beyond HNDM, UNAM-RI and SEP to include the Biblioteca Virtual Miguel de Cervantes, Universidad Veracruzana's hemerographic reference work, SIHENA, El Colegio de México, UAM Signos Históricos and TESIUNAM. These sources have different legal and epistemic roles. A primary digital catalog can support object resolution; an academic article or thesis can support discovery but does not substitute for the primary serial record.

### First object-level cohort

`data/catalog/documents.csv` now contains **15 concrete issue-level records**. The seed includes:

- *La Enseñanza Objetiva*, 12 December 1891;
- *El Escolar Mexicano*, 2 September 1888;
- three object-level records of *La Enseñanza primaria*;
- four issue localizers for *Revista de la Instrucción Pública Mexicana*;
- one issue of *Revista Mexicana de Educación*;
- five issues of *La Enseñanza Normal* from 1904–1905.

The record for *La Enseñanza Normal* preserves an important catalog inconsistency rather than normalizing it away: the Cervantes collection-level description states a different beginning date, while its parts listing explicitly identifies Año I, núm. 1 as 15 September 1904 and núm. 2 as 22 October 1904. PDHD uses the issue-level parts listing for the seed records and records the inconsistency in `notes`.

### Rights and reproducibility decision

No expansion of the discovery universe changes the public-content policy. HNDM objects remain `metadata_only`; newly added repositories are `review_required` until object-level terms are resolved. The repository therefore stores bibliographic identity, localizers, rights state and analytical metadata, not an unlicensed mirror of source PDFs or page images.

### Next documentary target

The next threshold is **50 concrete documents**. Priority should go to resolving issue-level objects for the strongest comparative series: *La Enseñanza Objetiva*, *El Escolar Mexicano*, *México Intelectual*, *La Escuela moderna*, *La Enseñanza primaria*, *La Enseñanza Normal* and *El Maestro Rural*. A stratified sample can then enter `pedagogical_fragment` annotation so that method, authority, assessment, discipline and teacher action are compared across periods without treating prescriptions as observed classroom practice.

## 2026-09-03 — stabilization sweep, regional balancing and unresolved rural sources

After reaching the 50-object infrastructure seed, the project shifted from accumulation to **cohort stabilization**. The working object union now contains 65 records, split temporarily between `documents.csv` and `documents_balancing_w1.csv` so that the balancing intervention remains auditable.

### Resolved balancing objects

The sweep added seven object records from *El Maestro. Revista de Cultura Nacional* to create an early-SEP/postrevolutionary pole. Where bibliographic sources disagree about the exact day of an issue, PDHD deliberately reduces date precision instead of selecting a date without sufficient evidence. The disagreement over tomo I, núm. 1 is registered in `chronology_conflicts.csv`.

Five direct object-level records of *La Escuela moderna* were resolved in the UNAM repository for 1889–1891. Three additional direct UNAM objects increase regional breadth: *México intelectual* from Xalapa, Veracruz; *El Instructor* from Aguascalientes; and *El Periquito* from Campeche. Their digital-resource licenses are recorded conservatively at object level and are not generalized into a blanket source-reuse permission.

### Lead queue and negative discovery result

The rural/postrevolutionary series remain the main methodological bottleneck. Peer-reviewed scholarship gives strong issue-level evidence for *El Maestro Rural*: it identifies the magazine as the organ of the SEP's Departamento de Misiones Culturales and cites individual issues including núm. 1 (1 March 1932), núm. 8 (15 June 1932) and núm. 11 (1 August 1932). Scholarship likewise identifies *Revista de Educación* as a SEP publication from 1937 and 1939. These citations are sufficient to create **discovery leads**, but not to promote the issues to object-level PDHD documents without a stable primary digital locator.

A targeted public-web sweep checked HNDM-facing queries, institutional repositories and Internet Archive discovery for stable issue objects. It recovered additional scholarly references and physical/hemerographic evidence, but **did not resolve a stable primary digital issue endpoint for _El Maestro Rural_ or _Revista de Educación_**. PDHD therefore preserves these records as `pending_primary_locator` rather than fabricating object URLs or treating secondary citations as source objects.

This negative result is itself part of project provenance. Repeating the same generic search should not be treated as new progress; the next attempt should use a new access route, such as an HNDM internal issue identifier, a catalog-to-image bridge, an institutional scan supplied by a library, or documented permission/access from the holding institution.

### Regional nineteenth-century leads

The same sweep strengthened the pre-1900 queue with HNDM primary descriptors. *El Protector de la infancia* is supported at serial level for Guadalajara, with surviving chronology from tomo I, núm. 1 (31 August 1871) through núm. 10 (31 August 1872). *La Educación* is supported for León, including tomo I, núm. 4 (16 July 1871) and tomo II, núm. 18 (1 May 1873). These remain leads until issue-level localizers are resolved.

### Methodological consequence

The corpus now satisfies the future pilot's minimum **geographic diversity** condition at object level, but it does not yet satisfy the stronger requirement for rural-teacher primary objects and documentary-type diversity. Accordingly, the human reliability protocol has been built and tested technically, but actual blind coding remains gated.

The decision is deliberate: **a smaller, traceable and heterogeneous pilot is preferable to an apparently larger corpus whose rural evidence rests only on citations to inaccessible primary issues.**

## 2026-09-03 — rural primary-source bottleneck resolved

A new search strategy abandoned the attempt to solve the rural gap only through *El Maestro Rural* issue discovery and instead targeted **contemporary SEP monographs, memorias, guidance pamphlets and mission reports** with stable primary digital records. This produced a materially stronger result.

### HathiTrust primary objects

Four direct HathiTrust catalog records were added:

- *El papel social del maestro rural* (SEP, 1925), an 8-page pamphlet with full-view access;
- *El sistema de escuelas rurales en México* (SEP, 1927), xxvi + 358 pages, full view;
- *Las misiones culturales en 1927: Las escuelas normales rurales* (SEP, 1928), xii + 470 pages, full view;
- José Gálvez, *Proyecto para la organización de las misiones federales de educación* (1923), 26 pages, full view.

These sources are contemporary institutional objects. They directly document rural teacher roles, mission organization, professional improvement, rural-normal education and planned educational intervention.

HathiTrust's catalog and full-view status resolve **object identity and research access**, but automated retrieval of the Babel page-image endpoint returned HTTP 403 in the current research environment. PDHD therefore records the stable catalog object and does not pretend that machine-accessible page text has already been obtained. Fragment freezing for these objects may require manual browser consultation or another permitted local access route.

### Google Books primary objects

Five additional SEP objects were resolved through stable Google Books identifiers:

- *Las misiones culturales, 1932-1933* (1933), 357 pages;
- *Memoria relativa al estado que guarda el ramo de educación pública*, vol. 1 (1932);
- the corresponding vol. 2 record published in 1934;
- *Memoria de la Secretaría de Educación Pública*, vol. 2 (1937);
- *Memoria de la Secretaría de Educación Pública*, vols. 1-2 (1938).

Google Books exposes searchable internal metadata and, in several records, full-view or free-ebook access. The records include direct evidence of rural schools, missions, teacher preparation, inspectors, Escuelas Regionales Campesinas, supervision and institutional organization. PDHD uses these objects as **primary digital localizers**, while preserving a separate rights decision for any public transcription or image reuse.

### Consequence for the pilot

The hard pilot condition is now satisfied: PDHD has rural/postrevolutionary **primary objects with stable digital identities**, not merely citations to inaccessible issues. The project therefore froze a first 24-document pilot selection spanning E1, E3 and E4, multiple regions and six documentary types.

Human coding still has not started. The new bottleneck is narrower and more operational: freeze 96 page-localized fragments in a rights-compatible way and then run the predeclared calibration and independent reliability protocol.
