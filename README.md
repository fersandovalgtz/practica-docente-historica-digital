# Práctica Docente Histórica Digital (PDHD)

**Infraestructura abierta de investigación para estudiar históricamente la práctica docente en México mediante prensa pedagógica, manuales, revistas profesionales, publicaciones oficiales y otros impresos educativos.**

> Estado: `v0.1.0-dev` · `PDHD-U1` en congelamiento activo del primer piloto de validación humana.

## Qué es PDHD

Práctica Docente Histórica Digital (PDHD) construye un corpus histórico-computacional trazable sobre el acto de enseñar en México. Su objetivo no es acumular documentos, sino transformar fuentes heterogéneas en evidencia reproducible sobre métodos de enseñanza, evaluación, disciplina, autoridad docente, materiales, formación profesional, inspección y supervisión, ruralidad, inclusión, concepciones del alumnado e identidad del magisterio.

PDHD distingue entre **fuente**, **identidad documental**, **derechos**, **procesamiento técnico**, **fragmento pedagógico**, **anotación**, **validación humana** e **interpretación histórica**. Esta separación es parte del método.

## Pregunta general

> ¿Cómo se transforma históricamente el acto de enseñar en México y qué huellas documentales dejan sus métodos, normas, prácticas, materiales, formas de evaluación, concepciones del alumnado y representaciones de la profesión docente?

## Estado científico de PDHD-U1

Corte de referencia: **5 de septiembre de 2026**.

| Capa | Estado |
|---|---:|
| Candidatos documentales registrados | **25** |
| Objetos documentales con identidad y localizador | **75** |
| Fuentes con política de derechos explícita | **13 / 13** |
| Leads hemerográficos activos sin resolver | **19** |
| Conflictos cronológicos preservados | **5** |
| Documentos congelados para el primer piloto | **24** |
| Fragmentos fijos previstos | **96** |
| Slots con localizador candidato/resuelto | **80 / 96** |
| Fragmentos completamente congelados | **22 / 96** |
| Fragmentos pedagógicos validados por humanos | **0** |

Los 75 objetos forman una **cohorte de estabilización y preparación metodológica**, no una muestra nacional representativa. El tablero vigente está en [`docs/PDHD_U1_COHORT_STATUS.md`](docs/PDHD_U1_COHORT_STATUS.md).

## Avance metodológico clave

El principal bloqueo previo era la falta de fuentes rurales/postrevolucionarias primarias con localizador estable. Ese problema ya no depende de localizar primero números digitalizados de *El Maestro Rural*.

PDHD incorporó objetos contemporáneos de la SEP con identidad primaria verificable, entre ellos *El papel social del maestro rural* (1925), *El sistema de escuelas rurales en México* (1927), *Las misiones culturales en 1927: Las escuelas normales rurales* (1928), *Proyecto para la organización de las misiones federales de educación* (1923), *Las misiones culturales, 1932-1933* (1933), *El esfuerzo educativo en México* (1928) y memorias de la Secretaría de Educación Pública de 1932, 1934, 1937 y 1938.

El proyecto ya tiene tres lotes completos de **fragment freezing**. `PDHD-F000013`–`PDHD-F000016`, derivados de una página directamente inspeccionada de *El Escolar Mexicano* del 2 de septiembre de 1888; `PDHD-F000017`–`PDHD-F000020`, derivados de *La Enseñanza Objetiva* del 12 de diciembre de 1891; y `PDHD-F000053`–`PDHD-F000056`, derivados del primer número de *El Maestro. Revista de Cultura Nacional* de 1921, tienen límites estructurales fijos.

A esos doce fragmentos se suman tres unidades directamente inspeccionadas de *La Enseñanza Moderna*, tomo I, segunda época, núm. 1, del 1 de julio de 1907: `PDHD-F000038`–`PDHD-F000040`. La imagen primaria de BVMC permite fijar el bloque editorial/profesional, la región programática de apertura y un bloque administrativo de control. El slot A de ese documento (`PDHD-F000037`) sigue pendiente porque todavía no se ha inspeccionado un pasaje de acto pedagógico explícito con resolución suficiente.

El número inaugural de *La Enseñanza Normal*, 15 de septiembre de 1904, aporta dos unidades adicionales congeladas desde el PDF primario de BVMC. `PDHD-F000034` fija el bloque profesional/editorial de primera página y `PDHD-F000036` fija la línea autónoma de periodicidad como control administrativo. El slot A (`PDHD-F000033`) permanece pendiente de cotejo primario en p. 12.

*El Maestro* suma ahora cuatro congelamientos adicionales a su primer lote completo. En tomo II, núm. 3, `PDHD-F000050` fija en `n237` el bloque institucional de la Secretaría de Educación Pública y Talleres Gráficos de la Nación, mientras `PDHD-F000052` fija en `n236` el cartucho bibliográfico de portada como control. La portada identifica explícitamente tomo II, número III, diciembre de 1921 y la imprenta independiente confirma México, diciembre de 1921. Para los números 2 y 4 de 1921, `PDHD-F000044` y `PDHD-F000048` quedan congelados como controles mediante los cartuchos bibliográficos de las portadas primarias `n104` y `n4`, respectivamente.

`PDHD-F000060`, control de *El esfuerzo educativo en México* (1928), cruza ahora el mismo gate de imagen primaria. Google Books expone `PR5`; un workflow de recuperación resolvió el PDF público vigente desde el HTML de la página seleccionada y renderizó las primeras hojas. La correspondencia `PR5` → orden 6 del libro → imagen PDF 009 se verificó antes de fijar el núcleo bibliográfico de la portada como control. La cola de conversión directa queda vacía; esto no equivale a completar el paquete de 96 fragmentos.

Como HNDM permanece `metadata_only` y la reutilización de objetos BVMC e Internet Archive se maneja conservadoramente, el repositorio conserva localizadores, límites y metadatos de preparación; no publica el texto histórico ni las imágenes de página.

## Ecosistema de fuentes

La infraestructura registra, entre otras, HNDM y sistemas hemerográficos UNAM, Repositorio Institucional UNAM, Biblioteca Virtual Miguel de Cervantes, Internet Archive, Open Library, Fondo Reservado de la Biblioteca México, HathiTrust, Google Books/Google Play Books y colecciones históricas de la SEP. Fuentes universitarias secundarias de alta calidad se utilizan para descubrimiento y contextualización cuando todavía falta cotejar una página en el objeto primario.

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
- `primary_ocr_region != image_verified_span`
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

La cola de trabajo está organizada en shards auditables `data/samples/fragment_locator_progress*.csv`. En el corte actual su unión contiene **80/96** slots con una página o sección candidata, resuelta o congelada. Los fragmentos que ya cruzaron el gate completo se registran en `data/samples/frozen_fragments*.csv`; su unión contiene **22/96** fragmentos.

La fase reciente ha reforzado especialmente la revista *El Maestro*. Además del lote congelado del primer número, el tomo II, núm. 3 ya aporta dos regiones congeladas y los números 2 y 4 de 1921 aportan controles de portada directamente inspeccionados. Entre los targets analíticos pendientes figuran José U. Escobar, *Las tribus indígenas mexicanas*; Abel Ayala, *Mejores maestros*; Rafael Ramos Pedrueza, *Historia de México*; Gabriela Mistral, *Lecturas escolares. El cardo*; Rufino Blanco-Fombona, *Democracia Criolla*; José Suirob, *Orientación obrera*; y el manifiesto *La internacional de los intelectuales* del Grupo Claridad. Los punteros secundarios permanecen como `locator_candidate` hasta cotejar directamente las páginas del objeto histórico.

Los reader targets de Internet Archive se mantienen como rutas de recuperación, no como sustitutos de inspección. Para `PDHD-F000044`, el target registrado `n103` condujo a una ventana que mostró el cierre del número anterior y la portada inequívoca del número II en `n104`; para `PDHD-F000048`, el target `n6` condujo a la portada inequívoca del número IV en `n4`. En ambos casos el span congelado es el cartucho bibliográfico visible en la imagen primaria, no el target genérico original.

*México intelectual* tiene ya sus cuatro slots localizados en el tomo I. La p. 5 se usa para el slot A por la formulación programática de difusión de métodos, sistemas y enseñanza pedagógica moderna; la p. 2 alimenta el componente profesional/institucional; la p. 6 se reserva como control administrativo por contener precios e instrucciones de correspondencia; y `PDHD-F000011` resuelve ahora el slot C con *La Escuela Normal de Jalapa*, pp. 26–27. Este último puntero procede de un volumen de historia de la educación editado por la Sociedad Mexicana de Historia de la Educación y evaluado por pares. Los cuatro permanecen sujetos al estatus de evidencia individual de sus respectivos shards; el nuevo slot C sigue pendiente de cotejo contra la página histórica.

*La Enseñanza Normal* tiene ya congelados `PDHD-F000034` y `PDHD-F000036` en la primera página del número inaugural del 15 de septiembre de 1904. La inspección del PDF primario de BVMC fija, respectivamente, la región profesional/editorial y una línea administrativa de periodicidad como control. El slot A apunta a la p. 12, donde una tesis de la UNAM localiza una prescripción de Leopoldo Kiel sobre práctica con grupos de niños, observación y comprobación de procedimientos de enseñanza; este último permanece pendiente de inspección directa de la página histórica.

*La Enseñanza Primaria* incorpora ahora `PDHD-F000025`: una publicación de la Universidad Pedagógica Nacional proporciona la cita exacta de Ponciano Rodríguez, *El método en los libros de texto*, tomo I, núm. 11, pp. 167–168. La identidad del número y la fecha de 1 de diciembre de 1901 están respaldadas por investigación histórica independiente. El rango de páginas queda resuelto para el slot A, pero el pasaje permanece como `locator_candidate` hasta inspeccionar directamente la página histórica y fijar el span del codificador.

El mismo número incorpora `PDHD-F000027`: una tesis de la UNAM localiza Gregorio Torres Quintero, *Los ejercicios físicos en la escuela*, pp. 161–163. El rango resuelve el slot C como puntero secundario exacto sobre escolarización corporal y educación física; sigue pendiente el cotejo de la página histórica en HNDM antes del congelamiento.

*El Periquito* incorpora `PDHD-F000003`: una monografía académica de la Biblioteca Nacional de México cita el texto homónimo en el número 4, fechado el 6 de noviembre de 1870, p. 2, dentro de su análisis de la simbolización animal en la prensa. El dato coincide exactamente con el objeto piloto de Campeche y resuelve el slot C como puntero secundario de página para crítica de fuentes. La página histórica del volumen encuadernado en HNDM continúa pendiente de inspección, por lo que el fragmento no está congelado.

`PDHD-F000050` y `PDHD-F000052`, correspondientes a *El Maestro*, tomo II, núm. 3, ya cruzaron el gate de imagen primaria. El workflow corregido recuperó BookReader `n232–n238`; la inspección directa fija `F000050` en el bloque institucional SEP/Talleres de `n237` y `F000052` en el cartucho bibliográfico de la portada `n236`. `n238` comienza *La inconsciencia de la hora* en la p. 227 y confirma la secuencia interna del número.

El conflicto cronológico de *El Maestro*, tomo II, núm. 3 queda resuelto a **1921-12**. La portada `n236` identifica tomo II, número III y diciembre de 1921; la imprenta `n237` confirma independientemente México, diciembre de 1921. `PDHD-X000005` conserva el registro secundario de 1922 como discrepancia historiográfica, pero la cronología canónica adopta ahora la evidencia primaria a precisión mensual.

El volumen II de la *Memoria de la Secretaría de Educación Pública* de 1937 ya tiene sus cuatro slots localizados. Dos proceden directamente del índice de Google Books —Consejo Nacional de la Educación Superior y de la Investigación, p. 41, y Distribución de Becas en la República, p. 40—. Otros dos son punteros secundarios verificables: p. 371 para la relación entre trabajo manual y desarrollo educativo, y p. 444 para estadísticas de asistencia a bibliotecas. Estos últimos no se congelarán sin cotejo primario.

La *Memoria relativa al estado que guarda el ramo de educación pública* de 1932 ya completa también sus cuatro slots de localización: el slot C apunta a la p. 487, identificada por investigación alojada en el IPN para una comparación institucional entre educación técnica, primaria y rural. Se conserva como puntero secundario pendiente de cotejo en el objeto primario.

La fuerza de la evidencia se interpreta conforme a [`docs/LOCATOR_EVIDENCE_POLICY.md`](docs/LOCATOR_EVIDENCE_POLICY.md): un pasaje primario directo, un inicio de sección, un facsímil histórico reproducido dentro de una fuente secundaria y una cita académica con página no tienen el mismo estatus metodológico.

## Taxonomía y confiabilidad

La taxonomía vigente incluye dimensiones como `teaching_method`, `teacher_authority`, `discipline`, `assessment`, `materials`, `lesson_organization`, `teacher_training`, `inspection_supervision`, `rurality`, `indigenous_education`, `inclusion_difference`, `gender`, `student_conception`, `professional_identity`, `school_community` y `pedagogical_change`.

La capa de actos pedagógicos utiliza códigos controlados como `explain`, `ask`, `examine`, `correct`, `punish`, `reward`, `demonstrate`, `read`, `dictate`, `observe`, `organize`, `classify`, `adapt`, `record`, `repeat`, `memorize`, `practice` y `guide`.

El protocolo humano está en [`docs/ANNOTATION_PILOT_PROTOCOL.md`](docs/ANNOTATION_PILOT_PROTOCOL.md). Prevé 12 fragmentos de calibración y 96 fragmentos independientes, al menos dos codificadores humanos, alfa de Krippendorff para campos nominales, diagnóstico multilabel por dimensión y adjudicación solo después de congelar el acuerdo independiente.

El manual vigente está en [`docs/ANNOTATION_MANUAL.md`](docs/ANNOTATION_MANUAL.md) y el cálculo reproducible en [`scripts/annotation_agreement.py`](scripts/annotation_agreement.py).

## Derechos y reutilización

PDHD aplica una política conservadora a objetos digitales de terceros. HNDM se mantiene `metadata_only` salvo autorización adicional. HathiTrust, Internet Archive y Google Books/Google Play Books se utilizan como localizadores de investigación; la disponibilidad de vista completa, OCR o ebook gratuito no se interpreta como permiso automático para republicar scans u OCR alojados por esas plataformas.

Cuando el texto no deba publicarse, el fragmento puede congelarse mediante página/localizador y utilizar texto de trabajo controlado fuera de GitHub. Consulte [`RIGHTS.md`](RIGHTS.md), [`docs/RIGHTS_AND_REUSE.md`](docs/RIGHTS_AND_REUSE.md) y [`data/catalog/rights_registry.csv`](data/catalog/rights_registry.csv).

## Integridad y reproducibilidad

El repositorio mantiene identificadores estables `PDHD-C`, `PDHD-D`, `PDHD-L`, `PDHD-X` y `PDHD-F`; registra discrepancias cronológicas; valida duplicados, fuentes, derechos y relaciones entre objetos; comprueba la selección de 24 documentos; auto-prueba el calculador de confiabilidad y verifica la generación de 96 slots en GitHub Actions.

`validate_repository.py` controla el catálogo base. `validate_fragment_shards.py` trata todos los shards de localización y congelamiento como una sola unión lógica: detecta duplicados entre archivos, verifica documento y slot contra el manifiesto determinista, exige límites fijos para todo fragmento `frozen` y cruza cada registro congelado con su correspondiente localizador. La misma validación exige que `fragment_gap_queue_0_1.csv` sea exactamente el complemento de los IDs localizados, de modo que un slot no pueda aparecer simultáneamente como resuelto y pendiente.

`pilot_content_leads.csv` conserva hallazgos de contenido antes de su promoción a página. Toda fila promovida declara ahora un `promoted_fragment_id`; `validate_content_leads.py` comprueba que ese fragmento exista en los shards, corresponda al mismo documento y no sea reclamado por otro lead. La cadena queda explícita como `issue identity -> content lead -> promoted_fragment_id -> page locator -> frozen fragment`.

`retrieval_attempts.csv` conserva intentos de acceso primario y sus desenlaces. `validate_retrieval_attempts.py` verifica IDs, correspondencia documento-fragmento, URLs, estados de bloqueo y rutas siguientes. Los intentos que culminan en localizadores congelados se conservan como `superseded_by_locator`, de modo que el historial técnico permanece auditable sin confundirse con un bloqueo vigente.

## Siguiente puerta metodológica

La selección documental ya está lista. **80/96 slots tienen ya un localizador documentado.** La prioridad es convertir la mayor cantidad posible de los **58 localizadores todavía no congelados** en páginas primarias inspeccionadas con límites fijos. Los **22/96** congelados demuestran el pipeline a través de HNDM, BVMC e Internet Archive y cubren prensa pedagógica de 1888, 1891, 1904 y 1907, además de *El Maestro* en 1921.

La cola dedicada de conversión directa quedó vacía después de `PDHD-F000060`; el siguiente frente es convertir punteros de página fuertes mediante inspección directa del objeto primario. Quedan **16 slots sin localizador**. El umbral operativo 80/96 ya fue alcanzado; el siguiente escalón cuantitativo de seguimiento será **84/96**, pero el indicador científicamente más importante es aumentar los fragmentos `frozen`, no maximizar referencias débiles. La cola directa queda reducida a `PDHD-F000060`, control `PR5` de *El esfuerzo educativo en México*, todavía pendiente de inspección primaria auditable.

Solo después de completar el paquete se prepara el set de calibración, se congela la versión del codebook y comienza la codificación humana independiente.

## Autoría y citación

Proyecto iniciado por **Fernando Sandoval Gutiérrez**. La forma normalizada de citación se mantiene en [`CITATION.cff`](CITATION.cff).

## Licencias

El software original del repositorio se publica bajo **Apache License 2.0**. Los datos derivados originales, cuando exista capacidad jurídica para licenciarlos, se publican conforme a [`DATA_LICENSE.md`](DATA_LICENSE.md). Las licencias del repositorio **no se extienden a materiales fuente de terceros**.