# PDHD-U1 — protocolo de compuertas para etapas humanas futuras 0.1

## Propósito

Este protocolo define qué puede automatizarse antes de disponer de intervención humana y qué estados deben bloquearse hasta que exista evidencia humana real. La automatización prepara, verifica y transforma metadatos; no sustituye codificación, discusión ni adjudicación humanas.

## Estado actual

PDHD-U1 tiene 96/96 fragmentos documentales congelados. Doce están fijados para calibración bajo `PDHD-CAL-0.1-20260907` y los 84 restantes están fijados en la reserva `PDHD-RR-0.1-20260907`. El único codebook registrado es `PDHD-CB-0.2-calibration` con estado `calibration_baseline`.

Por tanto, la ronda formal de confiabilidad **no está abierta**.

## Compuerta 1 — calibración humana

Antes de cualquier ronda formal deben existir dos primeras pasadas reales e independientes de los 12 casos de calibración. `scripts/validate_completed_calibration_sheet.py` puede verificar esas hojas, pero no puede producirlas ni corregirlas.

`scripts/compare_calibration_sheets.py` puede comparar dos hojas ya válidas. Su salida es un diagnóstico de acuerdos, desacuerdos y celdas no comparables por problemas de acceso. No adjudica, no modifica respuestas y no constituye el cálculo formal de confiabilidad.

## Compuerta 2 — congelación del codebook independiente

Después de discutir la calibración, cualquier cambio al manual o a las taxonomías debe versionarse. La versión destinada a la ronda independiente sólo abre la siguiente compuerta cuando existe **exactamente una** fila en `data/samples/codebook_registry.csv` con:

`status=frozen_for_independent_reliability`

Esa fila debe registrar la versión y los Git blob SHA del manual de anotación, taxonomía de actos y taxonomía de dimensiones. `scripts/build_formal_reliability_package.py` recalcula esos blob SHA antes de generar cualquier paquete. Una modificación silenciosa posterior al freeze vuelve inválida la compuerta.

## Compuerta 3 — generación formal de 84 casos

La identidad de los 84 fragmentos no se decide después de la calibración: ya está pre-registrada en `reliability_reserve_0_1.csv`.

Cuando la compuerta del codebook se abra, `scripts/build_formal_reliability_package.py` podrá generar de forma determinista:

- `data/samples/reliability_manifest_0_1.csv`;
- `data/samples/reliability_coder_sheet_0_1.csv`.

El orden de los 84 ítems se permuta de manera determinista con un hash basado en `PDHD-REL-0.1`, la versión congelada del codebook y `fragment_id`. No utiliza etiquetas humanas, etiquetas de modelo ni `selection_role`.

La hoja para codificadores omite era, slot A-D, rol de selección y notas de preparación. Conserva únicamente identidad mínima, página, URL de evidencia, límite fijo del fragmento, versión de codebook y campos de respuesta vacíos.

## Estado que CI debe exigir hoy

Mientras no exista codebook `frozen_for_independent_reliability`, CI exige simultáneamente:

- que el generador formal se mantenga bloqueado;
- que `reliability_manifest_0_1.csv` no exista;
- que `reliability_coder_sheet_0_1.csv` no exista.

La presencia prematura de cualquiera de esos archivos hace fallar la validación.

Cuando en el futuro exista un codebook congelado, el mismo comando `--check-state` cambia de obligación: requerirá que el paquete formal exista y sea reproducible byte por byte.

## Estados que no pueden automatizarse legítimamente

Ningún script puede convertir una predicción de modelo en `human_validation`, declarar que dos codificadores existen, decidir que una discusión de calibración ocurrió, adjudicar un desacuerdo sin una decisión real o crear un gold label en nombre de una persona.

Las herramientas pueden facilitar esas etapas, pero la provenance debe conservar la diferencia entre ejecución automática y decisión humana.

## Regla central

`automation_prepares_and_checks != human_validation`

`pre_registered_reserve != formal_reliability_round`

`calibration_diagnostic != formal_reliability`

`independent_responses != adjudicated_gold`
