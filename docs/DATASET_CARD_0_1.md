# PDHD-U1 — Dataset Card 0.1

## Identidad

**Práctica Docente Histórica Digital (PDHD)** es una infraestructura abierta de investigación para estudiar históricamente la práctica docente en México mediante fuentes documentales como prensa pedagógica, revistas profesionales, manuales, publicaciones oficiales y otros impresos educativos.

Esta tarjeta describe el estado **pre-validación** del piloto PDHD-U1. El proyecto permanece en `0.1.0-dev`; no constituye todavía el release final `v0.1.0` porque la validación semántica humana y la primera ronda formal de confiabilidad intercodificador no han ocurrido.

## Estado del corpus

El piloto documental contiene 24 documentos seleccionados y 96 fragmentos con localización y límites congelados. Los 96 fragmentos están trazados a una página, hoja, imagen o superficie primaria equivalente y conservan provenance de recuperación, acceso y derechos según la arquitectura del repositorio.

Los 96 fragmentos se encuentran pre-particionados en 12 casos de calibración y una reserva fija de 84 casos para la futura ronda formal de confiabilidad. Esta partición no crea fragmentos adicionales y fue fijada antes de observar cualquier etiqueta humana.

## Estado de validación

La codificación humana permanece en **0 fragmentos**. No existe todavía una estimación formal de confiabilidad intercodificador y no existe un gold set. El codebook registrado `PDHD-CB-0.2-calibration` es un baseline de calibración, no la versión congelada que gobernará la futura ronda independiente.

Los archivos de calibración y las herramientas automáticas preparan el trabajo futuro, pero ninguna salida automatizada se considera validación humana.

## Unidad de análisis

La unidad de codificación es un fragmento documental con identidad estable, `document_id`, página o localizador equivalente y una frontera fija. Cada uno de los 24 documentos piloto aporta cuatro slots documentales. La unidad de fragmento sirve para codificación, pero no debe confundirse con 96 fuentes históricas independientes: existe dependencia estructural por documento.

## Cobertura

PDHD-U1 fue diseñado como un piloto metodológico y documental, no como una muestra probabilística nacional. La cobertura busca diversidad temporal, regional y documental suficiente para probar recuperación de fuentes, trazabilidad, derechos, congelación de fragmentos y confiabilidad futura.

Por ello, frecuencias calculadas dentro del piloto no deben presentarse como estimadores de la práctica docente mexicana en su conjunto. Las comparaciones por era, procedencia o tipo documental serán descriptivas del corpus salvo que una fase posterior introduzca un diseño de muestreo apto para inferencia poblacional.

## Contenido público y contenido no redistribuido

El repositorio publica metadatos PDHD, identificadores, localizadores, reglas metodológicas, estados de acceso, información de derechos, límites derivados y otros productos propios. No funciona como espejo de colecciones históricas de terceros.

Cuando la política de la fuente o la base jurídica no autorizan redistribución, el repositorio no incorpora facsímiles, páginas completas ni OCR de terceros simplemente porque sean visibles o descargables. El acceso para investigación y el permiso de republicación son tratados como cuestiones distintas.

## Campos semánticos previstos

El esquema de anotación contempla actos pedagógicos controlados, dimensiones pedagógicas multi-etiqueta, normatividad o modo evidencial, actor, destinatario y confianza del codificador. Esos campos existen como esquema y taxonomía, pero en el estado descrito por esta tarjeta **no contienen un benchmark humano validado**.

## Usos apropiados en el estado actual

El corpus puede utilizarse para auditar metodología de recuperación y trazabilidad, estudiar arquitectura de provenance y derechos, replicar la selección y congelación del piloto, examinar cobertura documental, desarrollar herramientas compatibles con el esquema o preparar protocolos de validación.

También puede sustentar una nota o artículo metodológico sobre construcción de corpus histórico-digital, siempre que se distinga claramente entre cierre documental y validación semántica.

## Usos que todavía no están respaldados

El estado actual no respalda afirmar exactitud de etiquetas automáticas, rendimiento de un clasificador histórico, confiabilidad humana formal, prevalencias nacionales de prácticas docentes ni existencia de un gold standard.

Tampoco debe inferirse práctica observada a partir de una prescripción, ni convertirse una mención institucional o un reporte retrospectivo en observación directa sin soporte documental compatible con el codebook.

## Sesgos y limitaciones

La disponibilidad digital de fuentes condiciona qué objetos pueden recuperarse y congelarse. Las interfaces de HNDM, BVMC, Internet Archive, Google Books y otros repositorios tienen patrones distintos de acceso, metadatos y persistencia. El corpus conserva intentos fallidos y sustituciones para que esos efectos no desaparezcan de la provenance.

La selección piloto tampoco elimina sesgos de conservación histórica, centralización editorial, desigual disponibilidad regional ni predominio de ciertos géneros documentales. La capa de source criticism debe acompañar cualquier interpretación sustantiva.

## Reproducibilidad

El estado científico pre-validación está fijado en `data/snapshots/prevalidation_snapshot_0_1.json`. Ese registro identifica el commit firmado, el Git tree correspondiente, la corrida de CI y los conteos canónicos 96/12/84.

Los generadores y validadores del repositorio comprueban de forma determinista la selección de calibración, la reserva de confiabilidad, los fragmentos congelados, las compuertas de codebook y la integridad estructural del corpus.

## Derechos y licencias

El software y los componentes propios del proyecto se rigen por los archivos de licencia y gobernanza del repositorio. Los metadatos y datos derivados tienen condiciones documentadas en `DATA_LICENSE.md`. Los derechos de fuentes históricas de terceros permanecen sujetos a la institución de origen y se registran por separado en `RIGHTS.md` y en el registro de derechos.

## Citación

La referencia canónica del software/proyecto se mantiene en `CITATION.cff`. Mientras `VERSION` siga en `0.1.0-dev`, cualquier cita o depósito debe identificar el commit o snapshot utilizado además de la versión de desarrollo.

## Próximo gate científico

El siguiente gate sustantivo requiere intervención humana real: dos primeras pasadas independientes de los 12 casos de calibración, discusión documentada, congelación versionada del codebook independiente y ejecución de la ronda formal sobre los 84 casos pre-registrados.

Hasta entonces:

`documentary_freeze_complete != semantic_validation_complete`
