# Práctica Docente Histórica Digital (PDHD)

**Infraestructura abierta de investigación para estudiar históricamente la práctica docente en México mediante prensa pedagógica, manuales, revistas profesionales, publicaciones oficiales y otros impresos educativos.**

> Estado: `v0.1.0-dev` · fase de diseño y construcción de `PDHD-U1`.

## Qué es PDHD

Práctica Docente Histórica Digital (PDHD) es una infraestructura de investigación orientada a construir un corpus histórico-computacional trazable sobre el acto de enseñar en México. Su objeto no es reunir documentos por acumulación, sino convertir fuentes heterogéneas en evidencia reproducible sobre métodos de enseñanza, evaluación, disciplina, autoridad docente, materiales, formación profesional, inspección escolar, ruralidad, inclusión, concepciones del alumnado e identidad del magisterio.

PDHD distingue entre **fuente**, **identidad documental**, **procesamiento técnico**, **fragmento pedagógico**, **anotación**, **validación humana** e **interpretación histórica**. Esta separación es un requisito epistemológico del proyecto.

## Pregunta general

> ¿Cómo se transforma históricamente el acto de enseñar en México y qué huellas documentales dejan sus métodos, normas, prácticas, materiales, formas de evaluación, concepciones del alumnado y representaciones de la profesión docente?

## Fuentes iniciales

La primera unidad de trabajo considera tres familias de fuentes públicas o institucionales:

- **Hemeroteca Nacional Digital de México (HNDM)**: prensa pedagógica, periódicos, revistas y publicaciones profesionales históricas.
- **Repositorio Institucional de la UNAM**: publicaciones académicas, históricas, hemerográficas y colecciones universitarias pertinentes.
- **Secretaría de Educación Pública (SEP)**: publicaciones históricas, materiales oficiales, manuales y colecciones documentales.

La inclusión de una fuente en el catálogo **no implica autorización para redistribuir su facsímil, imagen u OCR íntegro**. Cada registro debe pasar por el `rights_registry` y adoptar una política explícita de reutilización.

## Arquitectura de evidencia

```text
fuente institucional
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
validación humana
        ↓
análisis longitudinal e interpretación histórica
```

### Contrato epistemológico

PDHD adopta estas reglas:

- `source_found != source_reusable`
- `ocr_available != text_verified`
- `search_hit != historical_claim`
- `model_label != human_validation`
- `prescription != observed_practice`
- `absence_of_hit != demonstrated_absence`

Un texto puede prescribir una conducta docente sin demostrar que esa conducta ocurrió. La infraestructura debe conservar esa diferencia.

## Unidad inicial: PDHD-U1

**PDHD-U1 — Genealogía documental de la práctica docente mexicana** es la primera cohorte de construcción. Su propósito es probar el modelo con una colección pequeña, controlada y trazable antes de escalar.

La periodización de referencia es:

| Periodo | Problemas de interés |
|---|---|
| 1870–1940 | prensa pedagógica, normalismo, inspección, métodos, disciplina y profesionalización |
| 1921–1970 | maestro posrevolucionario, escuela rural, campañas, política educativa y construcción estatal del magisterio |
| 1970–2000 | planeación, tecnificación, evaluación, formación y profesionalización |
| 2000–2026 | inclusión, competencias, tecnologías, evaluación institucional y Nueva Escuela Mexicana |

La meta de `PDHD-U1` no es exhaustividad nacional inmediata. El primer corte debe reunir **50–100 documentos de alta calidad documental**, con procedencia, derechos y unidad analítica explícitos.

## Unidad analítica: fragmento pedagógico

El objeto analítico principal es el `pedagogical_fragment`: un fragmento localizado dentro de un documento y anotado de forma trazable.

Ejemplo conceptual:

```json
{
  "fragment_id": "PDHD-F000001",
  "document_id": "PDHD-D000001",
  "source_id": "HNDM",
  "date": "1892-05-15",
  "page": 4,
  "fragment_locator": "p4-c2",
  "transcription_status": "local_ocr_unverified",
  "pedagogical_act": "examinar",
  "dimension": "assessment",
  "actor": "teacher",
  "target": "student",
  "normativity": "prescriptive",
  "validation_status": "unvalidated",
  "rights_status": "metadata_only"
}
```

## Taxonomía 0.1

La primera taxonomía incluye estas dimensiones: `teaching_method`, `teacher_authority`, `discipline`, `assessment`, `materials`, `lesson_organization`, `teacher_training`, `inspection_supervision`, `rurality`, `indigenous_education`, `inclusion_difference`, `gender`, `student_conception`, `professional_identity`, `school_community` y `pedagogical_change`.

De manera transversal, PDHD registra **actos pedagógicos**: explicar, preguntar, examinar, corregir, castigar, premiar, mostrar, leer, dictar, observar, organizar, clasificar, adaptar y registrar, entre otros. Esta capa busca estudiar transformaciones históricas de la acción docente, no solo cambios temáticos en el vocabulario.

## Derechos y HNDM

PDHD aplica una política especialmente restrictiva a la HNDM. Sus disposiciones de uso señalan que los contenidos digitales están protegidos, que su uso debe ser personal o académico, que debe reconocerse la procedencia y que las imágenes digitales no pueden incorporarse a sistemas o aplicaciones sin autorización previa y por escrito.

Por ello, salvo autorización específica, PDHD conserva públicamente **metadatos, localizadores, código, esquemas y derivados jurídicamente publicables**, mientras que imágenes, facsímiles y OCR íntegro de materiales restringidos permanecen fuera del repositorio público.

Referencia institucional: <https://hndm.iib.unam.mx/index.php/es/tramites-y-servicios?start=1>

## Estructura prevista

```text
.
├── README.md
├── CITATION.cff
├── LICENSE
├── DATA_LICENSE.md
├── RIGHTS.md
├── GOVERNANCE.md
├── PROVENANCE.md
├── VERSION
├── CHANGELOG.md
├── data/
│   ├── catalog/
│   ├── taxonomy/
│   └── samples/
├── schemas/
├── docs/
├── scripts/
└── .github/workflows/
```

## Principios de integridad científica

1. La fuente no se corrige silenciosamente.
2. La automatización no fabrica validación humana.
3. La prescripción documental no se confunde con práctica observada.
4. Los problemas de derechos se registran antes de procesar o redistribuir contenido.
5. Todo fragmento debe poder regresar a su documento y localizador de origen.
6. La incertidumbre y los resultados negativos forman parte del dato.
7. Una release es un corte histórico reproducible y no cambia retroactivamente.

## Estado actual

`PDHD` se encuentra en fase `0.1`: definición del modelo de datos, política de fuentes, registro de derechos, taxonomía inicial y construcción del universo `PDHD-U1`.

## Autoría y citación

Proyecto iniciado por **Fernando Sandoval Gutiérrez**. La forma normalizada de citación se mantiene en [`CITATION.cff`](CITATION.cff).

## Licencias

El software original del repositorio se publica bajo **Apache License 2.0**. Los datos derivados originales, cuando exista capacidad jurídica para licenciarlos, se publican conforme a [`DATA_LICENSE.md`](DATA_LICENSE.md). Las licencias del repositorio **no se extienden a materiales fuente de terceros**.
