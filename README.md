# Práctica Docente Histórica Digital (PDHD)

**Infraestructura abierta de investigación para estudiar históricamente la práctica docente en México mediante prensa pedagógica, manuales, revistas profesionales, publicaciones oficiales y otros impresos educativos.**

> Estado: `v0.1.0-dev` · estabilización de `PDHD-U1` y preparación del primer protocolo de validación humana.

## Qué es PDHD

Práctica Docente Histórica Digital (PDHD) es una infraestructura de investigación orientada a construir un corpus histórico-computacional trazable sobre el acto de enseñar en México. Su objeto no es reunir documentos por acumulación, sino convertir fuentes heterogéneas en evidencia reproducible sobre métodos de enseñanza, evaluación, disciplina, autoridad docente, materiales, formación profesional, inspección escolar, ruralidad, inclusión, concepciones del alumnado e identidad del magisterio.

PDHD distingue entre **fuente**, **identidad documental**, **procesamiento técnico**, **fragmento pedagógico**, **anotación**, **validación humana** e **interpretación histórica**. Esta separación es un requisito epistemológico del proyecto.

## Pregunta general

> ¿Cómo se transforma históricamente el acto de enseñar en México y qué huellas documentales dejan sus métodos, normas, prácticas, materiales, formas de evaluación, concepciones del alumnado y representaciones de la profesión docente?

## Estado científico de PDHD-U1

Corte de referencia: **3 de septiembre de 2026**.

| Capa | Estado |
|---|---:|
| Candidatos documentales registrados | **25** |
| Objetos documentales con identidad y localizador | **65** |
| Fuentes con política de derechos explícita | **10 / 10** |
| Leads hemerográficos activos sin resolver | **19** |
| Conflictos cronológicos preservados | **2** |
| Fragmentos pedagógicos validados por humanos | **0** |

Los 65 objetos forman una **cohorte de estabilización**, no una muestra históricamente representativa. Cuarenta registros todavía proceden de dos series pedagógicas de 1904–1907. El proyecto mantiene explícita esta concentración y no autoriza inferencias longitudinales a partir del conteo bruto.

El tablero metodológico vigente está en [`docs/PDHD_U1_COHORT_STATUS.md`](docs/PDHD_U1_COHORT_STATUS.md).

## Ecosistema de fuentes

La cohorte se construye mediante catálogos, hemerotecas, bibliotecas y repositorios institucionales. Entre las fuentes registradas se encuentran:

- **Hemeroteca Nacional Digital de México (HNDM)** y sistemas hemerográficos de la UNAM;
- **Repositorio Institucional de la UNAM**;
- **Biblioteca Virtual Miguel de Cervantes**;
- **Internet Archive**, utilizado como localizador de objetos cuando su procedencia puede documentarse;
- **Secretaría de Educación Pública** y colecciones históricas institucionales;
- fuentes universitarias secundarias de alta calidad utilizadas para descubrir, contextualizar o verificar publicaciones antes de resolver el objeto primario.

La inclusión de una fuente en el catálogo **no implica autorización para redistribuir su facsímil, imagen u OCR íntegro**. Cada fuente y, cuando es necesario, cada objeto debe pasar por una decisión explícita de derechos.

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
- `absence_of_hit != demonstrated_absence`

Un texto puede prescribir una conducta docente sin demostrar que esa conducta ocurrió. Una publicación abundante en los repositorios tampoco representa automáticamente una mayor importancia histórica. La infraestructura debe conservar ambas diferencias.

## Unidad inicial: PDHD-U1

**PDHD-U1 — Genealogía documental de la práctica docente mexicana** es la primera cohorte de construcción. Su propósito es probar el modelo documental, estabilizar una muestra de fuentes defendible y validar el sistema de anotación antes de escalar.

Para análisis y muestreo se utilizan estratos no superpuestos. La justificación y reglas se documentan en [`docs/PERIODIZATION_PROTOCOL.md`](docs/PERIODIZATION_PROTOCOL.md).

| Código | Periodo | Problema de trabajo |
|---|---|---|
| E1 | 1870–1910 | profesionalización liberal y porfiriana, prensa pedagógica, normalismo, enseñanza objetiva e inspección |
| E2 | 1911–1920 | transición revolucionaria y reconfiguración de autoridad e instituciones escolares |
| E3 | 1921–1934 | reconstrucción educativa de la SEP, expansión rural, misiones y formación del maestro |
| E4 | 1935–1940 | educación socialista y reconfiguración cardenista |
| E5 | 1941–1970 | consolidación nacional y expansión masiva de la escolarización |
| E6 | 1971–2000 | planeación, modernización, tecnificación y evaluación |
| E7 | 2001–2026 | inclusión, rendición de cuentas, digitalización y Nueva Escuela Mexicana |

`era_code` es una variable de estratificación; **no constituye por sí misma una explicación causal del cambio pedagógico**.

## Unidad analítica: fragmento pedagógico

El objeto analítico principal es el `pedagogical_fragment`: un fragmento localizado dentro de un documento y anotado de forma trazable.

Ejemplo conceptual:

```json
{
  "fragment_id": "PDHD-F000001",
  "document_id": "PDHD-D000001",
  "source_id": "HNDM",
  "date": "1891-12-12",
  "page": 4,
  "fragment_locator": "p4-c2",
  "transcription_status": "local_ocr_unverified",
  "pedagogical_act_primary": "examine",
  "dimensions": ["assessment"],
  "actor": "teacher",
  "target": "student",
  "normativity": "prescriptive",
  "validation_status": "unvalidated",
  "rights_status": "metadata_only"
}
```

## Taxonomía y validación humana

La taxonomía 0.2 incluye dimensiones como `teaching_method`, `teacher_authority`, `discipline`, `assessment`, `materials`, `lesson_organization`, `teacher_training`, `inspection_supervision`, `rurality`, `indigenous_education`, `inclusion_difference`, `gender`, `student_conception`, `professional_identity`, `school_community` y `pedagogical_change`.

De manera transversal, PDHD registra **actos pedagógicos** mediante códigos controlados como `explain`, `ask`, `examine`, `correct`, `punish`, `reward`, `demonstrate`, `read`, `dictate`, `observe`, `organize`, `classify`, `adapt`, `record`, `repeat`, `memorize`, `practice` y `guide`.

El primer piloto humano está preespecificado en [`docs/ANNOTATION_PILOT_PROTOCOL.md`](docs/ANNOTATION_PILOT_PROTOCOL.md). Su diseño prevé 24 documentos estratificados, 96 fragmentos fijos y al menos dos codificadores humanos independientes. La confiabilidad de campos nominales se evaluará mediante alfa de Krippendorff; las dimensiones multilabel se evaluarán por dimensión y mediante diagnósticos de solapamiento. La adjudicación ocurre **después** de congelar el cálculo de acuerdo independiente.

El manual vigente es [`docs/ANNOTATION_MANUAL.md`](docs/ANNOTATION_MANUAL.md), la plantilla pública está en [`data/samples/annotation_pilot_template.csv`](data/samples/annotation_pilot_template.csv) y el cálculo reproducible de acuerdo se implementa en [`scripts/annotation_agreement.py`](scripts/annotation_agreement.py).

## Derechos y reutilización

PDHD aplica una política conservadora a los objetos digitales de terceros. En particular, las condiciones de HNDM impiden tratar la disponibilidad digital como autorización automática para incorporar imágenes o reproducciones a otro sistema.

Por ello, salvo autorización o licencia compatible documentada, PDHD conserva públicamente **metadatos, localizadores, código, esquemas, decisiones de procedencia y derivados jurídicamente publicables**, mientras que imágenes, facsímiles y OCR íntegro restringido permanecen fuera del repositorio público.

El Repositorio Institucional de la UNAM expone algunos objetos históricos bajo CC BY-NC-ND 4.0. PDHD registra esa circunstancia a nivel de objeto, pero no la simplifica como una autorización general de redistribución o creación de derivados.

Consulte [`RIGHTS.md`](RIGHTS.md), [`docs/RIGHTS_AND_REUSE.md`](docs/RIGHTS_AND_REUSE.md) y [`data/catalog/rights_registry.csv`](data/catalog/rights_registry.csv).

## Integridad y reproducibilidad

El repositorio mantiene:

- catálogos separados de fuentes, candidatos, documentos, leads y conflictos cronológicos;
- identificadores estables `PDHD-C`, `PDHD-D`, `PDHD-L`, `PDHD-X` y `PDHD-F`;
- un registro explícito de discrepancias, en vez de normalizaciones silenciosas;
- validación automática de identificadores, fuentes, derechos, duplicados y relaciones entre leads y documentos;
- auto-pruebas del calculador de confiabilidad de anotación dentro de GitHub Actions.

La política es que una discrepancia real **se documenta; no se borra para que el catálogo parezca limpio**.

## Principios de integridad científica

1. La fuente no se corrige silenciosamente.
2. La automatización no fabrica validación humana.
3. La prescripción documental no se confunde con práctica observada.
4. Los problemas de derechos se registran antes de procesar o redistribuir contenido.
5. Todo fragmento debe poder regresar a su documento y localizador de origen.
6. La incertidumbre y los resultados negativos forman parte del dato.
7. Una release es un corte histórico reproducible y no cambia retroactivamente.

## Estado actual y siguiente puerta metodológica

PDHD se encuentra en fase `0.1`, pero ya ha superado la prueba de infraestructura inicial. El trabajo actual es **estabilizar la cohorte**, reducir el sesgo de disponibilidad y resolver suficientes fuentes rurales y tipos documentales distintos de la prensa periódica.

La primera validación humana no comenzará solo porque se alcance un número mayor de documentos. La puerta metodológica requiere, entre otras condiciones, material rural con localizador primario, al menos tres procedencias geográficas fuera de Ciudad de México, diversidad de tipos documentales y que ninguna publicación domine más de una cuarta parte del piloto.

## Autoría y citación

Proyecto iniciado por **Fernando Sandoval Gutiérrez**. La forma normalizada de citación se mantiene en [`CITATION.cff`](CITATION.cff).

## Licencias

El software original del repositorio se publica bajo **Apache License 2.0**. Los datos derivados originales, cuando exista capacidad jurídica para licenciarlos, se publican conforme a [`DATA_LICENSE.md`](DATA_LICENSE.md). Las licencias del repositorio **no se extienden a materiales fuente de terceros**.
