# Source-link audit protocol 0.1

## Purpose

Observe whether public URLs referenced by PDHD remain reachable without turning transient web failures into scientific claims about the existence of historical sources.

## Schedule

`.github/workflows/audit-source-links.yml` runs weekly and can also be triggered manually. It is intentionally separate from canonical CI.

The workflow writes CSV and JSON artifacts retained for 30 days. Broken external endpoints do not by themselves fail the repository integrity suite.

## URL-state classes

| State | Meaning |
|---|---|
| `reachable` | HTTP 2xx or redirect response completed. |
| `url_not_found` | HTTP 404 or 410 for the tested URL. |
| `access_restricted` | HTTP 401/403; endpoint may exist but deny automated/public access. |
| `rate_limited` | HTTP 429. |
| `server_error` | HTTP 5xx; treated as endpoint/server condition. |
| `timeout` | Request timed out. |
| `dns_error` | Hostname resolution failed. |
| `tls_error` | TLS negotiation/certificate error. |
| `network_error` | Other network-layer failure. |
| `client_error` | Unexpected local/request behavior. |
| `other_http` | Other HTTP status. |

## Source-existence separation

Every result also carries `source_entity_state` and `source_existence_inference`.

If a URL belongs to a `source_id` or `document_id` that remains in PDHD's canonical catalogs, the entity state is `catalogued` even when the tested URL fails. `source_existence_inference` is always `not_inferred_from_http` in this auditor.

Therefore:

`404 != historical source does not exist`

`timeout != historical source does not exist`

`403 != historical source does not exist`

A conclusion that a source/object does not exist would require separate documentary research and an explicit versioned catalog decision.

## Sources audited

The script deduplicates HTTP(S) URLs referenced by:

- source-family base URLs;
- rights/terms URLs;
- canonical document object URLs;
- source-candidate URLs;
- structured retrieval-attempt targets;
- fragment locator evidence URLs;
- frozen-fragment evidence URLs.

It retains all origin files/roles for every deduplicated URL.

## Request behavior

The auditor first attempts `HEAD`. Because some repositories reject `HEAD` but permit normal retrieval, it retries selected method-related failures with a minimal ranged `GET`. It follows redirects through the standard Python HTTP client and records the final URL.

## Interpretation

Use the report to identify maintenance work: update moved locators, investigate repeated failures, or preserve alternate aliases. Do not use it to remove documentary objects automatically.
