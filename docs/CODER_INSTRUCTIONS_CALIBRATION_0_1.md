# PDHD-U1 — instrucciones para codificación de calibración 0.1

## Alcance

Estas instrucciones corresponden únicamente a la **calibración humana de 12 fragmentos** previa a la primera ronda formal de confiabilidad intercodificador.

La calibración sirve para detectar ambigüedades del codebook y entrenar una aplicación común de las categorías. **No forma parte del cálculo final de confiabilidad** y no produce todavía un gold set.

## Material que sí debe utilizar cada codificador

Cada codificador recibe una copia local independiente de:

- `data/samples/calibration_coder_sheet_0_1.csv`;
- `docs/ANNOTATION_MANUAL.md`;
- `data/taxonomy/pedagogical_acts.csv`;
- `data/taxonomy/pedagogical_dimensions.csv`;
- las páginas u objetos primarios enlazados en la columna `source_url` de la hoja de calibración.

La versión de trabajo del codebook para esta etapa es:

`PDHD-CB-0.2-calibration`

## Material que no debe consultar durante la primera pasada

Para preservar la independencia de las decisiones, el codificador **no debe consultar** antes de entregar su primera pasada:

- `data/samples/calibration_manifest_0_1.csv`;
- archivos `frozen_fragments*.csv`;
- archivos `fragment_locator_progress*.csv`;
- `preparation_note`, `selection_role`, slots A/B/C/D o cualquier metadato de selección investigadora;
- historial de pull requests o commits donde se discutan interpretaciones de esos fragmentos;
- etiquetas sugeridas por modelos, búsquedas, heurísticas o clasificaciones automáticas;
- respuestas del otro codificador.

La restricción se refiere al **primer pase independiente**. Después de congelar ambas respuestas, la discusión conjunta es parte deliberada de la calibración.

## Identificación del codificador

Cada persona usa un identificador pseudónimo estable, por ejemplo `C01` y `C02`. No use nombre, correo u otro dato personal dentro de la hoja pública o de trabajo.

En cada fila:

- `coder_id`: identificador pseudónimo estable;
- `annotation_id`: `PDHD-CALANN-<coder_id>-<item_id>`, por ejemplo `PDHD-CALANN-C01-CAL001`;
- `annotated_at`: fecha y hora ISO 8601 de finalización de esa decisión o de la sesión, según el flujo adoptado.

## Regla de evidencia

**Codifique únicamente lo que el fragmento y su contexto inmediato permiten defender.** No complete el sentido a partir de lo que sabe del periodo, del autor, de la institución o del género documental.

Se mantienen las reglas epistemológicas centrales:

`prescription != observed_practice`

`model_label != human_validation`

`search_hit != historical_claim`

Cuando la página sea inaccesible, ilegible o insuficiente, registre el problema en `access_problem`. No adivine.

## Campos de respuesta

### `pedagogical_act_primary`

Use un único código controlado de `pedagogical_acts.csv`, o `none` / `unclear` cuando corresponda. No invente sinónimos.

### `pedagogical_act_secondary`

Puede dejarse vacío cuando no exista un segundo acto defendible. Cuando exista, use únicamente códigos controlados y sepárelos con `;` si hubiera más de uno.

### Dimensiones

Cada columna `dimension_*` debe recibir `1` cuando exista evidencia afirmativa y `0` cuando no exista. No convierta la ausencia de evidencia en una inferencia positiva.

Si un problema real de acceso impide decidir el conjunto completo de campos, documente el problema antes que rellenar artificialmente valores.

### `normativity`

Use exclusivamente uno de estos valores:

`prescriptive`, `policy_normative`, `descriptive`, `reported_practice`, `observed_practice`, `testimonial`, `analytical`, `mixed`, `unclear`.

Preste especial atención a las fronteras descritas en el manual entre prescripción y norma institucional, entre práctica reportada y testimonio, y entre práctica reportada y observación directa.

### `actor`

Use:

`teacher`, `student`, `inspector`, `director`, `family`, `community`, `state_authority`, `other`, `unclear`.

### `target`

Use:

`student`, `teacher`, `family`, `community`, `institution`, `self`, `other`, `unclear`.

### `evidence_confidence`

Use `high`, `medium` o `low`. La confianza expresa seguridad del codificador en la aplicación de la categoría; no representa verdad histórica.

### `notes`

Use notas breves únicamente cuando ayuden a explicar una frontera de codificación, una duda o un problema de evidencia. **No copie transcripciones extensas del documento histórico** ni reproduzca imágenes de la fuente en el repositorio.

## Procedimiento de primera pasada

Cada codificador trabaja por separado y completa los 12 ítems `CAL001`–`CAL012`. No discute casos concretos con el otro codificador hasta que ambas hojas hayan sido entregadas y congeladas como archivos de provenance.

El orden `CAL001`–`CAL012` debe conservarse. No se omite un ítem por parecer poco pedagógico: algunos fragmentos están deliberadamente diseñados para permitir `none`, `unclear` o múltiples ceros en las dimensiones.

## Después de la primera pasada

Una vez preservadas las dos respuestas independientes:

1. se comparan las decisiones campo por campo;
2. se identifican desacuerdos recurrentes y fronteras ambiguas;
3. se discuten los 12 casos utilizando la evidencia primaria;
4. se revisan definiciones o ejemplos sólo cuando exista un problema real del codebook;
5. toda modificación queda versionada;
6. se registra una nueva versión **frozen** del codebook para la ronda formal;
7. los 12 fragmentos de calibración quedan excluidos de la ronda de confiabilidad de 84 fragmentos.

No se debe calcular ni presentar la calibración como si fuera la confiabilidad final del estudio.
