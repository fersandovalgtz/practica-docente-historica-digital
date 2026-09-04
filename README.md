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
| Conflictos cronológicos preservados | **5** |
| Documentos congelados para el primer piloto | **24** |
| Fragmentos fijos previstos | **96** |
| Slots con localizador candidato/resuelto | **64 / 96** |
| Fragmentos completamente congelados | **12 / 96** |
| Fragmentos pedagógicos validados por humanos | **0** |

Los 75 objetos forman una **cohorte de estabilización y preparación metodológica**, no una muestra nacional representativa. El tablero vigente está en [`docs/PDHD_U1_COHORT_STATUS.md`](docs/PDHD_U1_COHORT_STATUS.md).

## Avance metodológico clave

El principal bloqueo previo era la falta de fuentes rurales/postrevolucionarias primarias con localizador estable. Ese problema ya no depende de localizar primero números digitalizados de *El Maestro Rural*.

PDHD incorporó objetos contemporáneos de la SEP con identidad primaria verificable, entre ellos *El papel social del maestro rural* (1925), *El sistema de escuelas rurales en México* (1927), *Las misiones culturales en 1927: Las escuelas normales rurales* (1928), *Proyecto para la organización de las misiones federales de educación* (1923), *Las misiones culturales, 1932-1933* (1933), *El esfuerzo educativo en México* (1928) y memorias de la Secretaría de Educación Pública de 1932, 1934, 1937 y 1938.

El proyecto ya tiene tres lotes completos de **fragment freezing**. `PDHD-F000013`–`PDHD-F000016`, derivados de una página directamente inspeccionada de *El Escolar Mexicano* del 2 de septiembre de 1888; `PDHD-F000017`–`PDHD-F000020`, derivados de *La Enseñanza Objetiva* del 12 de diciembre de 1891; y `PDHD-F000053`–`PDHD-F000056`, derivados del primer número de *El Maestro. Revista de Cultura Nacional* de 1921, tienen límites estructurales fijos. El tercer lote combina la portada primaria de HNDM con una página directamente inspeccionada del artículo de Ezequiel A. Chávez *Los rasgos distintivos de la educación moderna*. Como HNDM permanece `metadata_only`, el repositorio conserva localizadores, límites y metadatos de preparación; no publica el texto histórico ni las imágenes de página.

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

La cola de trabajo está organizada en shards auditables `data/samples/fragment_locator_progress*.csv`. En el corte actual su unión contiene **64/96** slots con una página o sección candidata, resuelta o congelada. Los fragmentos que ya cruzaron el gate completo se registran en `data/samples/frozen_fragments*.csv`; su unión contiene **12/96** fragmentos.

La fase reciente ha reforzado especialmente la revista *El Maestro*. Además del lote congelado del primer número, se añadieron localizadores de página para José U. Escobar, *Las tribus indígenas mexicanas*; Abel Ayala, *Mejores maestros*; Gabriela Mistral, *Lecturas escolares. El cardo*; Rufino Blanco-Fombona, *Democracia Criolla*; José Suirob, *Orientación obrera*; y el manifiesto *La internacional de los intelectuales* del Grupo Claridad. Todos permanecen como `locator_candidate` hasta cotejar directamente las páginas del objeto histórico.

El caso de tomo II, núm. 3 expuso además una discrepancia cronológica. Una fuente académica identifica el objeto digital como 1922, mientras una tesis de la UNAM cita *Lecturas escolares. El cardo* en diciembre de 1921. El conflicto está preservado en `data/catalog/chronology_conflicts.csv`; PDHD mantiene 1922 como año de trabajo del catálogo hasta inspeccionar el pie de imprenta original.

El volumen II de la *Memoria de la Secretaría de Educación Pública* de 1937 ya tiene sus cuatro slots localizados. Dos proceden directamente del índice de Google Books —Consejo Nacional de la Educación Superior y de la Investigación, p. 41, y Distribución de Becas en la República, p. 40—. Otros dos son punteros secundarios verificables: p. 371 para la relación entre trabajo manual y desarrollo educativo, y p. 444 para estadísticas de asistencia a bibliotecas. Estos últimos no se congelarán sin cotejo primario.

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

`validate_repository.py` controla el catálogo base. `validate_fragment_shards.py` trata todos los shards de localización y congelamiento como una sola unión lógica: detecta duplicados entre archivos, verifica documento y slot contra el manifiesto determinista, exige límites fijos para todo fragmento `frozen` y cruza cada registro congelado con su correspondiente localizador. Esto permite ampliar el trabajo por lotes sin perder una única identidad metodológica.

`pilot_content_leads.csv` conserva hallazgos de contenido antes de su promoción a página. `validate_content_leads.py` distingue entre contenido verificado a nivel de número, punteros secundarios de página verificados y material aún no apto para convertirse en localizador. Esto evita colapsar la cadena `issue identity -> content lead -> page locator -> frozen fragment`.

## Siguiente puerta metodológica

La selección documental ya está lista. **64/96 slots —dos tercios del piloto— tienen ya un localizador documentado.** La prioridad deja de ser alcanzar una mayoría simple y pasa a convertir la mayor cantidad posible de los 52 localizadores no congelados en páginas primarias inspeccionadas con límites fijos. Los **12/96** congelados demuestran el pipeline en tres publicaciones históricas distintas.

Solo después de completar el paquete se prepara el set de calibración, se congela la versión del codebook y comienza la codificación humana independiente.

## Autoría y citación

Proyecto iniciado por **Fernando Sandoval Gutiérrez**. La forma normalizada de citación se mantiene en [`CITATION.cff`](CITATION.cff).

## Licencias

El software original del repositorio se publica bajo **Apache License 2.0**. Los datos derivados originales, cuando exista capacidad jurídica para licenciarlos, se publican conforme a [`DATA_LICENSE.md`](DATA_LICENSE.md). Las licencias del repositorio **no se extienden a materiales fuente de terceros**.
