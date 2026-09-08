# PDHD-U1 — plan de análisis pre-registrado 0.1

## Estado y propósito

Este documento fija decisiones analíticas **antes de observar cualquier etiqueta humana**. Su finalidad es reducir grados de libertad retrospectivos y separar con claridad tres capas: construcción documental, confiabilidad de codificación e interpretación histórica.

Al momento de esta versión, PDHD-U1 contiene 24 documentos piloto y 96 fragmentos congelados. Doce fragmentos están reservados para calibración humana y los 84 restantes constituyen la reserva pre-registrada para la primera ronda formal de confiabilidad. No existe todavía ninguna codificación humana, gold label ni estimación de confiabilidad.

## Principios de inferencia

PDHD-U1 es un corpus metodológico y documental, no una muestra probabilística nacional. Ninguna frecuencia del piloto se interpretará como estimador de la práctica docente mexicana en su conjunto. Los resultados semánticos se formularán como patrones observados **dentro del corpus seleccionado**.

La fuente documental representa discurso, prescripción, reporte, testimonio u observación según el campo `normativity`. Una prescripción no se convertirá en evidencia de práctica ocurrida. Un reporte no se convertirá en observación contemporánea salvo que el codebook lo permita explícitamente.

La selección documental, la congelación de fragmentos y la codificación semántica permanecerán analíticamente separadas. Los metadatos usados para seleccionar o localizar un fragmento no podrán actuar como etiquetas sustitutas.

## Partición fija del piloto

El universo piloto congelado es de 96 fragmentos. La partición metodológica queda fijada como:

- 12 fragmentos de calibración humana, definidos en `data/samples/calibration_manifest_0_1.csv`;
- 84 fragmentos de reserva para la primera ronda formal de confiabilidad, definidos en `data/samples/reliability_reserve_0_1.csv` como el complemento exacto de esos 12 dentro de los 96 fragmentos congelados.

Los 12 fragmentos de calibración no entrarán en el cálculo formal de confiabilidad de la ronda de 84.

## Confiabilidad

La primera ronda formal requerirá dos codificadores humanos independientes y un codebook congelado posterior a calibración. Las respuestas originales se preservarán antes de cualquier adjudicación.

Para campos categóricos simples se reportará acuerdo observado y la medida de confiabilidad implementada por el protocolo del proyecto. Para dimensiones binarias multi-etiqueta se reportará acuerdo por dimensión y una síntesis global compatible con la estructura multi-label. Los cálculos nunca mezclarán respuestas adjudicadas con las respuestas independientes originales.

No se interpretará un coeficiente aislado sin el tamaño efectivo de la muestra, distribución marginal y número de casos válidos. Los problemas de acceso o legibilidad se reportarán como faltantes explícitos y no se convertirán en desacuerdos semánticos por defecto.

## Análisis descriptivo posterior a validación

Una vez construido un gold set válido, se permitirán únicamente análisis compatibles con la cobertura del corpus: distribución de actos pedagógicos, dimensiones pedagógicas, modos de normatividad/evidencia, actor y destinatario, y cruces descriptivos por era analítica, tipo documental y procedencia cuando el número de casos sea suficiente.

Las comparaciones temporales se presentarán como diferencias descriptivas del corpus, no como tendencias poblacionales nacionales. Si una celda queda escasamente poblada, se agregará o se reportará sin inferencia cuantitativa fuerte.

## Preguntas longitudinales permitidas

El primer análisis priorizará preguntas ya declaradas en el plan maestro: cambios en actos pedagógicos, autoridad docente, evaluación, disciplina, identidad profesional y relación entre regulación y discurso de práctica.

No se añadirá una hipótesis principal post hoc únicamente porque produzca una diferencia llamativa. Toda nueva pregunta exploratoria surgida después de observar etiquetas se marcará explícitamente como exploratoria.

## Multiplicidad y tamaño del piloto

Dado que el piloto tiene 96 fragmentos y no fue diseñado para estimación poblacional, el análisis principal será descriptivo y orientado a estructura histórica. No se utilizará significación estadística convencional como criterio central para decidir relevancia histórica.

Cuando se calculen asociaciones o intervalos, se reportarán como apoyo descriptivo y con cautela respecto de dependencia documental: cuatro fragmentos proceden de cada documento seleccionado y por tanto no deben tratarse ingenuamente como 96 observaciones históricas independientes.

## Dependencia por documento

La unidad de fragmento sirve para codificación, pero la unidad documental sigue siendo relevante para inferencia. Cualquier análisis que trate fragmentos como observaciones deberá reconocer agrupamiento por `document_id`. Los análisis posteriores podrán resumir también a nivel de documento para evitar que un documento con cuatro fragmentos se interprete como cuatro fuentes históricas independientes.

## Datos faltantes y acceso

Los problemas de acceso, legibilidad o contexto se mantendrán como estados explícitos. No se imputarán etiquetas semánticas faltantes para la primera ronda de confiabilidad. La exclusión de un caso de un cálculo deberá quedar reportada con motivo y denominador resultante.

## Adjudicación y gold set

La adjudicación ocurrirá sólo después de preservar y analizar las respuestas independientes. El gold set será una capa nueva de provenance; nunca reemplazará silenciosamente las hojas originales.

Toda modificación del codebook derivada de calibración se versionará antes de generar las hojas de la ronda formal. Toda modificación posterior a la ronda formal se documentará como revisión posterior y no alterará retroactivamente la versión con la que se calculó confiabilidad.

## Salidas previstas

Cuando exista validación humana, la canalización reproducible deberá producir como mínimo: un resumen de completitud y problemas de acceso, acuerdo por campo, medidas de confiabilidad, matriz de desacuerdos, gold set adjudicado con provenance, tablas descriptivas del corpus validado y reportes legible y machine-readable.

## Regla de congelación

Esta versión `ANALYSIS_PLAN_0_1` queda fijada antes de cualquier etiqueta humana. Cambios futuros son permitidos únicamente mediante versiones nuevas que expliquen qué cambió, por qué y si la decisión ocurrió antes o después de observar resultados humanos.
