# Reproduce scored BLE 1.5-A: three execution tiers

This post-competition reviewer package reuses the completed offline hardening
audit. Commands below are tested from a fresh isolated checkout. The immutable
original `v1.5.0-rc.1` predates these reviewer entry points. This repository does
not change the original competition submission or establish a new hidden score.
See [publication provenance](PUBLICATION_PROVENANCE.json).

## Tier 1 — Public offline reproduction

Python 3.12 with SQLite FTS5 is supported. Install the notebook/test dependencies:

```sh
python3.12 -m venv .venv-notebook
. .venv-notebook/bin/activate
python -m pip install -r requirements-notebook.txt
python scripts/reproduce.py offline --notebooks
```

The install uses the public package index. All runtime checks can then run with
networking denied and credentials absent. Direct dependencies are pinned; the QA
report records the resolved transitive environment. This is not a full platform image lock.
The offline command runs existing source/result/release checks, focused frozen-A
regressions, the released observed metadata replay and both notebooks. Fresh notebook
copies and standalone HTML are written under ignored `outputs/`. A passing test of
an invented API reply is a controller test, not paid model inference.

Smaller entry points:

```sh
python scripts/reproduce.py results
python scripts/reproduce.py trace
python scripts/run_authorized_ble15a.py --help
```

The flagship notebook teaches the science through explicitly synthetic SQLite/API
fixtures and released aggregate analyses. The second notebook shows an authentic
historical local Standard forecast: two validated beliefs at 0.88, real semantic
retrieval and an earlier-belief readout. It omits protected inputs, evidence,
provider identifiers and encrypted payloads. This is metadata coherence replay,
not a full prompt/evidence replay or a new prediction. No complete independently
releasable historical evidence-bearing trajectory is currently established.

## Tier 2 — Exact authorized assets and optional real inference

You need **all six files** in [the restricted inventory](hosted-ble15a/RESTRICTED_ASSETS.md),
the exact public MiniLM weight and the supported inference dependencies. Their
original relative paths must be retained. There is no automatic authorized asset
delivery channel and no verified public derivation pipeline. Do not substitute
another corpus/index while claiming exact reconstruction.

Validate an approved asset directory without downloading, installing or using keys:

```sh
python scripts/reproduce.py assets --asset-dir /path/to/authorized-assets
```

An empty/mismatched directory produces an explicit BLOCKED result listing all
seven external files. Six are restricted; one is publicly retrievable MiniLM.
The sole public weight is pinned to revision
`c9745ed1d9f207416be6d2e6f8de32d1f16199bf`. Its SHA-256 is in the artifact manifest.
The exact `models.txt` remains unchanged; model download alone is insufficient.

The existing [reconstruct.py](hosted-ble15a/reconstruct.py) is the assembly tool.
Its existing arguments and output were previously verified with authorized assets:

```sh
python hosted-ble15a/reconstruct.py --help
```

Supply `--asset-dir`, `--fetch-minilm` and a new `--output` path as described in
[its original guide](hosted-ble15a/README_OPENREVIEW.md). This reconstruction creates
an offline-default archive with no key; it is not a new scientific submission.
Use roughly 9 GB of free scratch space for complete local checks and hydration.
The historical local versions for real MiniLM are recorded in
[OFFLINE_VALIDATION_DEPENDENCIES.txt](hosted-ble15a/OFFLINE_VALIDATION_DEPENDENCIES.txt).
The notebook environment intentionally does not install the full Torch stack.
Use a separate environment for the complete runtime; do not mix its NumPy pins
with the notebook environment:

```sh
python3.12 -m venv .venv-runtime
.venv-runtime/bin/python -m pip install -r requirements-runtime.txt
```

This minimal CPU stack avoids the historical Arrow/pandas/SentenceTransformers
wrapper dependencies. It is a local reproduction environment, not a portable
guarantee about every operating system or future organizer image.

The real-inference entry point is `scripts/run_authorized_ble15a.py`. Its preflight
verifies every runtime member against the scored manifest and requires the sanitized
configuration. Its live mode requires an explicit paid flag, an authorized input,
a new private output directory and `OPENAI_API_KEY` supplied by the operator’s
secret-injection system. It changes enablement/ledger location only in memory;
it never writes a credential into configuration or an archive. The unchanged
`model.predict` and frozen transport perform the inference. See
[SECURITY_AND_ACCESS.md](SECURITY_AND_ACCESS.md) for the conditional invocation.

**No live call was run during this hardening task.** The invocation is tested with
mocked transport and real local assets, and its credential boundary is tested using
only a synthetic key. Fresh provider entitlement, actual project accounting and
future model output remain live validation gates. Emergency/prior-only outputs
are not reported as successful genuine BLE reproduction.

## Tier 3 — Official organizer summative evaluation

Stanford controls the hidden families/items, subject outcomes, acquired-label
sequence, six budgets, scoring, worker allocation and runtime environment. A
common summative evaluation is distinct from the original formative result; no
forecast of its score is implied. The formative ALC cannot be regenerated from
aggregate feedback. Organizers need
their own hidden inputs/outcomes, six-budget acquisition process, official scorer
and supported worker environment, plus authorized copies of the runtime assets.
They must inject their own project credential into every authorized prediction
worker. Repository or Environment Secrets do not transfer to a clone or fork.

The frozen public configuration disables paid inference. For an official runner,
an organizer must create a private **credential-free operational configuration**
that enables inference and sets one shared ledger scope before workers start.
The secret itself stays in their runner’s environment. This runner integration has
not been exercised against hidden data here; instructions are a design requiring
organizer approval, not a claim of an executed hidden rerun.

Existing official checks on a complete sanitized reconstruction are referenced in
[the validation record](hosted-ble15a/RECONSTRUCTION_VALIDATION.json). Local QA uses
the preserved official checker and smoke tools with networking denied. The smoke
branch intentionally avoids paid inference and does not prove genuine BLE coverage.

## What exact means

[Source equivalence](docs/SOURCE_EQUIVALENCE.md) documents all 35 unchanged Python
modules. The original private container has a different configuration and hash
manifest. Rebuilt ZIP bytes are not identical. The current reconstructor insists
on the exact six asset hashes; several runtime checks also pin corpus, protected
input and trace identities. A future behaviorally equivalent rebuild would need
its own disclosed manifest, row/order/FTS/exclusion/ranking checks and approval.

Historical CLI R1 bootstrap/accuracy results require nonpublic original records;
public loss cells verify point arithmetic only. See [RESULTS.md](RESULTS.md).
