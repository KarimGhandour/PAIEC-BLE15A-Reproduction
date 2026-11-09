# Reviewer hardening: local QA and remaining gates

Status: **completed offline hardening audit**, checked 2026-11-09.
Subsequently authorized publication is recorded in [publication provenance](../PUBLICATION_PROVENANCE.json).
This work does not replace `v1.5.0-rc.1`, change a scored module or rerun hidden scoring.

## Reproduction status matrix

| Category | Available now | Boundary |
|---|---|---|
| Independently reproducible from public files | Source/hash checks; synthetic controller/SQLite tests; six populated budgets; failure and credential-boundary tests; both notebooks and HTML | Invented replies are not genuine Luna forecasts |
| Reproducible with authorized exact assets | Full local retrieval, source-equivalent assembly and offline official tools | All six restricted files, pinned MiniLM and supported dependencies are needed; no public delivery or exact derivation is established |
| Numerically verifiable from published aggregates | Historical point-estimate Brier/NLL arithmetic and hosted rounded six-budget/equal-group ALC | Hidden predictions/outcomes and original confidence-interval resampling are unavailable |
| Not independently reproducible without organizer-held data | Exact official score, hidden acquisition paths, hosted coverage/runtime and runner behavior | Requires organizer inputs, labels, scorer and execution configuration |
| Missing or insufficiently established | Asset transfer rights; independent exact regeneration; complete releasable prompt/evidence trajectory; current live entitlement; protected GitHub Environment/runner setup | Documented gates, not assumed successes |

The public default README already led with scored BLE 1.5-A before this task.
This package makes reproduction tiers and access restrictions more explicit; it does
not claim to be the first promotion from R1. The prerelease asset is 8,589,884 bytes,
SHA-256 `1d22b20e71cebda5206e8394d84b49c3c188495c097ee78dd23f05b6c5552a88`.
The OpenReview supplement is a different 579,597-byte package and is not a
separate downloadable asset on that GitHub release.

## Fresh public checkout

A fresh clone of public `main` at `0a102886a4e76acf93b40b53dbc3529973da5711`
received only the proposed public-safe reviewer files. A new Python 3.12 environment
installed the pinned notebook requirements from the package index. Subsequent
tests ran under OS-enforced restrictions denying IP networking and reads/writes
outside the isolated checkout/environment and approved system libraries.
An outside canary was unreadable, an outside write failed and a localhost TCP
connection failed. No credential was supplied to this public test environment.

`python scripts/reproduce.py offline --notebooks` passed:

- 13 targeted tests covering the unchanged controller, real synthetic SQLite
  filtering, all six populated acquisition budgets, schemas, validated-belief
  retention, emergency distinctions, shared financial reservations and auth guards.
- 34 historical R1 source identities and 64 bundled scored-A member hashes.
- Published aggregate arithmetic: rounded hosted cells give
  `0.1590608444444444444444444444`, within `0.000001` of the recorded
  official `0.1590607804`; 9 groups and 489 pairs.
- Flagship notebook: 60 cells, 19 executed code cells, 9 embedded plots, no errors.
- Observed metadata notebook: 11 cells, 5 executed code cells, 2 plots, no errors.
  Both generated HTML previews were checked; the two new plots were inspected.

The restricted environment produces an IPython warning because an optional TCP
output pipe is denied. The kernel uses local IPC, all cells execute and neither
notebook depends on that pipe or external assets.

## Authorized assembled runtime, separate from public clean room

The existing credential-free reconstruction was used without rebuilding a
submission ZIP. SHA-256:
`d0c67d5896b7d738598a62cb81da18c367c78170bb19bfe280162d0cacf70235`.
A second fresh environment installed `requirements-runtime.txt` successfully.
With OS outbound IP networking denied and fake HTTP replies:

| Check | Observed result |
|---|---|
| Existing official ZIP checker | PASS on the exact preserved reconstruction |
| Existing official Starting Kit smoke | PASS; requested 4 workers, but its 2 toy inputs used 2 workers |
| Separate cold concurrency test | 4 distinct prediction processes, peak overlap 4; 8 completed mocked forecasts |
| Sequential budget integration | 6 completed mocked forecasts at 0, 1, 3, 7, 15, 31 labels |
| Real local evidence | MiniLM and SQLite used; static/dynamic target exclusions and both SQLite quick checks passed |
| Hydrated corpus | 6,768,676,864 bytes; expected SHA-256 verified |
| Cold per-worker initialization | Approximately 55.86–55.89 seconds, local macOS only |
| Per-worker peak RSS | Approximately 501–528 MB, local macOS only |
| Mocked inference | 42 responses across 14 forecasts, encrypted continuation and model-derived synthetic readouts; no emergency fallback |
| Own-key CLI route | PASS through unchanged `model.predict` and AIMS HTTP transport, real retrieval, 3 mocked responses and final submit |
| Paid API calls | **0** |

These are engineering checks with authorized assets. They are not independent
public-data reconstruction, provider entitlement checks, live latency benchmarks,
hosted concurrency measurements or another official score.

## Identity, security and release boundary

All 35 scored Python modules are byte-identical to the verified local original.
The source manifest, six omitted-asset hashes and source-equivalence report are
included. The original credential pattern occurred only in its private
`submission_config.json`; the public copy has no key and disables inference.
The existing release scanner passed on the prospective public files and all
190 reachable Git blobs. Synthetic transport-test credentials are fixtures.
Pattern scanning is evidence of a check, not proof that all possible sensitive
content or upstream legal conditions have been identified.

The proposed GitHub workflow is an inactive design under
`docs/workflow_examples/`, with a deliberately invalid placeholder commit. It
requires future owner approval, a reviewed revision, protected Environment,
trusted operators and an ephemeral runner; none was configured or executed here.

**Public-safe source/documentation checks passed. Full-runtime public redistribution
remains blocked by asset clearance and access.** Genuine live reproduction needs
separate spending approval and verified operator credentials. Organizer hidden
evaluation additionally requires their secret injection and worker integration.
During that offline audit, no commit, push, release, account change, API inference
or OpenReview change was made. Later publication does not retroactively change
those observations or imply a new scientific result.
