# Práctica Docente Histórica Digital (PDHD)

**Infraestructura abierta de investigación para estudiar históricamente la práctica docente en México mediante prensa pedagógica, manuales, revistas profesionales, publicaciones oficiales y otros impresos educativos.**

> Estado: `v0.1.0-dev` · `PDHD-U1` en congelamiento activo del primer piloto de validación humana.

## Qué es PDHD

Práctica Docente Histórica Digital (PDHD) construye un corpus histórico-computacional trazable sobre el acto de enseñar en México. Su objetivo no es acumular documentos, sino transformar fuentes heterogéneas en evidencia reproducible sobre métodos de enseñanza, evaluación, disciplina, autoridad docente, materiales, formación profesional, inspección y supervisión, ruralidad, inclusión, concepciones del alumnado e identidad del magisterio.

PDHD distingue entre **fuente**, **identidad documental**, **derechos**, **procesamiento técnico**, **fragmento pedagógico**, **anotación**, **validación humana** e **interpretación histórica**. Esta separación es parte del método.

## Pregunta general

> ¿Cómo se transforma históricamente el acto de enseñar en México y qué huellas documentales dejan sus métodos, normas, prácticas, materiales, formas de evaluación, concepciones del alumnado y representaciones de la profesión docente?

## Estado científico de PDHD-U1

Corte de referencia: **4 de septiembre de 2026**.

| Capa | Estado |
|---|---:|
| Candidatos documentales registrados | **25** |
| Objetos documentales con identidad y localizador | **75** |
| Fuentes con política de derechos explícita | **13 / 13** |
| Leads hemerográficos activos sin resolver | **19** |
| Conflictos cronológicos preservados | **2** |
| Documentos congelados para el primer piloto | **24** |
| Fragmentos fijos previstos | **96** |
| Slots con localizador candidato/resuelto | **38 / 96** |
| Fragmentos completamente congelados | **4 / 96** |
| Fragmentos pedagógicos validados por humanos | **0** |

Los 75 objetos forman una **cohorte de estabilización y preparación metodológica**, no una muestra nacional representativa. El tablero vigente está en [`docs/PDHD_U1_COHORT_STATUS.md`](docs/PDHD_U1_COHORT_STATUS.md).

## Avance metodológico clave

El principal bloqueo previo era la falta de fuentes rurales/postrevolucionarias primarias con localizador estable. Ese problema ya no depende de localizar primero números digitalizados de *El Maestro Rural*.

PDHD incorporó objetos contemporáneos de la SEP con identidad primaria verificable, entre ellos *El papel social del maestro rural* (1925), *El sistema de escuelas rurales en México* (1927), *Las misiones culturales en 1927: Las escuelas normales rurales* (1928), *Proyecto para la organización de las misiones federales de educación* (1923), *Las misiones culturales, 1932-1933* (1933), *El esfuerzo educativo en México* (1928) y memorias de la Secretaría de Educación Pública de 1932, 1934, 1937 y 1938.

El proyecto también cruzó la primera puerta de **fragment freezing**: `PDHD-F000013`–`PDHD-F000016`, derivados de la página directamente inspeccionada de *El Escolar Mexicano* del 2 de septiembre de 1888, tienen límites estructurales fijos. Como la fuente es HNDM, el repositorio conserva únicamente localizadores y metadatos de preparación; no publica el texto histórico ni la imagen de página.

## Ecosistema de fuentes

La infraestructura registra, entre otras, HNDM y sistemas hemerográficos UNAM, Repositorio Institucional UNAM, Biblioteca Virtual Miguel de Cervantes, Internet Archive, Fondo Reservado de la Biblioteca México, HathiTrust, Google Books/Google Play Books y colecciones históricas de la SEP. Fuentes universitarias secundarias de alta calidad se utilizan para descubrimiento y contextualización cuando todavía falta cotejar una página en el objeto primario.

La inclusión de una fuente **no implica permiso automático para redistribuir facsímiles, imágenes u OCR íntegro**. Los estados de derechos se registran explícitamente en `data/catalog/rights_registry.csv`.

## Arquitectura de evidencia

```text
fuente institucional / catálogo verificable
        ↓
identidad documental + localizador estable
        ↓
registro de derechos y condiciones de uso
        ↓
procesamiento local cuando proceda
        ↓
fragmento pedagógico trazable
        ↓
anotación histórico-pedagógica
        ↓
validación humana independiente
        ↓
adjudicación y gold set
        ↓
análisis longitudinal e interpretación histórica
```

### Contrato epistemológico

PDHD adopta estas reglas:

- `source_found != source_reusable`
- `bibliographic_issue_reference != primary_object_resolved`
- `ocr_available != text_verified`
- `search_hit != historical_claim`
- `model_label != human_validation`
- `prescription != observed_practice`
- `object_count_threshold_reached != historical_representativeness`
- `document_selection_ready != annotation_started`
- `secondary_page_citation != primary_page_inspection`
- `visible_reproduced_facsimile != primary_object_crosscheck`
- `locator_candidate != frozen_fragment`
- `fixed_boundary != public_text_permission`
- `page_locator_resolved != fixed_coder_span`
- `primary_source_resolved != source_text_republishable`
- `absence_of_hit != demonstrated_absence`

Un texto puede prescribir una conducta docente sin demostrar que esa conducta ocurrió. Una publicación abundantemente digitalizada tampoco representa automáticamente una mayor importancia histórica.

## Periodización analítica

Para muestreo y análisis se utilizan estratos no superpuestos documentados en [`docs/PERIODIZATION_PROTOCOL.md`](docs/PERIODIZATION_PROTOCOL.md).

| Código | Periodo | Problema de trabajo |
|---|---|---|
| E1 | 1870–1910 | profesionalización liberal y porfiriana, prensa pedagógica, normalismo, enseñanza objetiva e inspección |
| E2 | 1911–1920 | transición revolucionaria y reconfiguración institucional |
| E3 | 1921–1934 | reconstrucción educativa de la SEP, expansión rural, misiones y formación del maestro |
| E4 | 1935–1940 | educación socialista y reconfiguración cardenista |
| E5 | 1941–1970 | consolidación nacional y expansión masiva |
| E6 | 1971–2000 | planeación, modernización, tecnificación y evaluación |
| E7 | 2001–2026 | inclusión, rendición de cuentas, digitalización y Nueva Escuela Mexicana |

`era_code` es una variable de estratificación; no constituye por sí misma una explicación causal.

## Primer piloto humano

La primera selección de **24 documentos** está congelada en [`data/samples/pilot_document_selection_0_1.csv`](data/samples/pilot_document_selection_0_1.csv) y explicada en [`docs/PILOT_DOCUMENT_SELECTION_0_1.md`](docs/PILOT_DOCUMENT_SELECTION_0_1.md).

| Era | Documentos |
|---|---:|
| E1 | 10 |
| E3 | 12 |
| E4 | 2 |

La selección incluye objetos de Campeche, Aguascalientes y Xalapa además de Ciudad de México; incorpora prensa, objetos hemerográficos, informes oficiales, orientación docente, monografías institucionales y propuestas de política. Ninguna publicación aporta más de seis documentos.

El objetivo del piloto es probar la **reproducibilidad del sistema de anotación**, no estimar frecuencias históricas nacionales.

## Fragmentos fijos

Cada documento aporta cuatro slots metodológicos, para **96 fragmentos**:

- A: acto pedagógico o prescripción explícita;
- B: identidad profesional, autoridad, supervisión, evaluación u organización;
- C: pasaje históricamente significativo seleccionado mediante crítica de fuentes;
- D: control capaz de recibir `none` o `unclear` en al menos un campo.

El protocolo está en [`docs/FRAGMENT_FREEZE_PROTOCOL.md`](docs/FRAGMENT_FREEZE_PROTOCOL.md). El manifiesto vacío se genera determinísticamente con:

```bash
python scripts/build_fragment_manifest.py --output fragment_manifest.csv
```

La cola de trabajo vive en [`data/samples/fragment_locator_progress_0_1.csv`](data/samples/fragment_locator_progress_0_1.csv). En el corte actual hay **38/96** slots con una página o sección candidata o resuelta. Los fragmentos que ya cruzaron el gate completo se registran separadamente en [`data/samples/frozen_fragments_0_1.csv`](data/samples/frozen_fragments_0_1.csv); actualmente son **4/96**.

La fuerza de la evidencia se interpreta conforme a [`docs/LOCATOR_EVIDENCE_POLICY.md`](docs/LOCATOR_EVIDENCE_POLICY.md): un pasaje primario directo, un inicio de sección, un facsímil histórico reproducido dentro de una fuente secundaria y una cita académica con página no tienen el mismo estatus metodológico.

## Taxonomía y confiabilidad

La taxonomía vigente incluye dimensiones como `teaching_method`, `teacher_authority`, `discipline`, `assessment`, `materials`, `lesson_organization`, `teacher_training`, `inspection_supervision`, `rurality`, `indigenous_education`, `inclusion_difference`, `gender`, `student_conception`, `professional_identity`, `school_community` y `pedagogical_change`.

La capa de actos pedagógicos utiliza códigos controlados como `explain`, `ask`, `examine`, `correct`, `punish`, `reward`, `demonstrate`, `read`, `dictate`, `observe`, `organize`, `classify`, `adapt`, `record`, `repeat`, `memorize`, `practice` y `guide`.

El protocolo humano está en [`docs/ANNOTATION_PILOT_PROTOCOL.md`](docs/ANNOTATION_PILOT_PROTOCOL.md). Prevé 12 fragmentos de calibración y 96 fragmentos independientes, al menos dos codificadores humanos, alfa de Krippendorff para campos nominales, diagnóstico multilabel por dimensión y adjudicación solo después de congelar el acuerdo independiente.

El manual vigente está en [`docs/ANNOTATION_MANUAL.md`](docs/ANNOTATION_MANUAL.md) y el cálculo reproducible en [`scripts/annotation_agreement.py`](scripts/annotation_agreement.py).

## Derechos y reutilización

PDHD aplica una política conservadora a objetos digitales de terceros. HNDM se mantiene `metadata_only` salvo autorización adicional. HathiTrust y Google Books/Google Play Books se utilizan como localizadores de investigación; la disponibilidad de vista completa o ebook gratuito no se interpreta como permiso automático para republicar scans u OCR alojados por esas plataformas.

Cuando el texto no deba publicarse, el fragmento puede congelarse mediante página/localizador y utilizar texto de trabajo controlado fuera de GitHub. Consulte [`RIGHTS.md`](RIGHTS.md), [`docs/RIGHTS_AND_REUSE.md`](docs/RIGHTS_AND_REUSE.md) y [`data/catalog/rights_registry.csv`](data/catalog/rights_registry.csv).

## Integridad y reproducibilidad

El repositorio mantiene identificadores estables `PDHD-C`, `PDHD-D`, `PDHD-L`, `PDHD-X` y `PDHD-F`; registra discrepancias cronológicas; valida duplicados, fuentes, derechos y relaciones entre objetos; comprueba la selección de 24 documentos; auto-prueba el calculador de confiabilidad y verifica la generación de 96 slots en GitHub Actions.

El validador también cruza `frozen_fragments_0_1.csv` contra la cola de localizadores y el manifiesto determinista: un fragmento no puede declararse `frozen` sin límites fijos, campos de acceso y manejo público válidos, ni sin coincidir con su documento y slot esperados.

## Siguiente puerta metodológica

La selección documental ya está lista. La tarea es llevar los **38/96 localizadores** actuales hacia **96/96** y aumentar la proporción de pasajes primarios directamente inspeccionados hasta convertirlos en verdaderos fragmentos congelados. Los primeros **4/96** ya demuestran que el pipeline de congelamiento funciona.

Solo después de completar el paquete se prepara el set de calibración, se congela la versión del codebook y comienza la codificación humana independiente.

## Autoría y citación

Proyecto iniciado por **Fernando Sandoval Gutiérrez**. La forma normalizada de citación se mantiene en [`CITATION.cff`](CITATION.cff).

## Licencias

El software original del repositorio se publica bajo **Apache License 2.0**. Los datos derivados originales, cuando exista capacidad jurídica para licenciarlos, se publican conforme a [`DATA_LICENSE.md`](DATA_LICENSE.md). Las licencias del repositorio **no se extienden a materiales fuente de terceros**.
