# Secure access and independent reviewer execution

## Three modes

| Mode | API credential | Six restricted assets | What success establishes |
|---|---|---|---|
| Public offline fixtures / observed metadata replay | None | None | Frozen-code mechanisms, metadata coherence and aggregate arithmetic only |
| Authenticated genuine local BLE | Reviewer-owned environment credential | All six, pinned MiniLM and supported dependencies | A live model-derived evidence/revision readout, if its receipt confirms it |
| Official organizer hidden evaluation | Organizer-owned protected runner injection | All six plus official hidden inputs, acquisitions, outcomes and scorer | A new official evaluation, subject to organizer rules |

A local smoke result, emergency Beta readout, cached previous result or an initial
belief without a completed evidence/revision cycle is not successful genuine BLE
reproduction. A valid earlier model belief after evidence is separately identified
from native final submit. The scored Completion policy remains unchanged.

## Lowest-friction local authentication

An approved secret-injection mechanism sets `OPENAI_API_KEY` in the execution
environment. The optional `OPENAI_PROJECT_ID` comes from the same credential’s
issuer and is forwarded by the frozen AIMS helper. Do not put a key on a command
line or in a notebook. An approved secrets manager may inject these same variables.
Repository secrets are not inherited by a local clone or fork.

Sample environment schema (descriptive, contains no values and is not a dotenv file):

| Variable | Supplied by |
|---|---|
| `OPENAI_API_KEY` | Reviewer/organizer secret store; never source-controlled |
| `OPENAI_PROJECT_ID` | Optional verified non-secret project identifier from issuer |
| `PAIEC_RUNTIME_DIR` | Authorized sanitized unpacked runtime path |
| `PAIEC_REVIEW_OUTPUT` | New output path under an operator-owned private scratch directory |
| `OPENAI_BASE_URL` | Leave unset; only the official OpenAI endpoint is accepted |

After approved exact-asset reconstruction, inspect the launcher without any network:

```sh
python scripts/run_authorized_ble15a.py --help
python scripts/run_authorized_ble15a.py preflight --runtime "$PAIEC_RUNTIME_DIR"
```

Preflight requires all 71 manifest members, verifies their sizes/hashes and rejects
an embedded/nonempty credential configuration. It makes zero API requests and does
not prove project entitlement. The key is read from the environment by the original
Responses client; it is not serialized into input, config, logs or a distribution.

The following is the **conditional live invocation**, requiring the operator’s
separate spending decision and environment secret. Its CLI/inference route is
validated locally using mocked HTTP and authorized assets; no new paid run or
current provider entitlement is claimed by this hardening task:

```sh
python scripts/run_authorized_ble15a.py live --allow-paid \
  --runtime "$PAIEC_RUNTIME_DIR" \
  --input examples/synthetic_authorized_input.json \
  --output-dir "$PAIEC_REVIEW_OUTPUT"
```

`--labels` may point only to legitimately revealed acquisition pairs. Omit it at
B0. The included input is explicitly invented; its probability is not an accuracy
benchmark. Use an authorized scientific case for a separately approved real study.
The output directory must be new, private and outside the checkout. Do not retry
an uncertain invocation. The launcher verifies the complete sanitized runtime,
enables the original inference flag only in memory and gives it a new private
ledger directory. No scored Python file or on-disk config is changed.

A request guard permits only HTTPS POST to `https://api.openai.com/v1/responses`,
Luna Medium, explicit Standard (`default`), no hosted tools and no API storage.
The actual frozen transport applies TLS, proxy and continuation rules. Offline
tests verify that the synthetic key appears only in the Authorization header to
that endpoint; arbitrary endpoints, Fast, other models and hosted tools are rejected.
This guard covers the trusted scored entry point, not arbitrary modified Python.
Run only the hash-verified runtime in a trusted environment.

The runtime may write evidence tool files into its private journal directory.
Never upload that directory as a GitHub artifact, publish its logs or enable shell
tracing. Public reporting needs a separate allowlist export. Provider errors are
reported through fixed categories without arbitrary error text.

## Organizer instructions

1. Obtain authorization for the exact six files, pinned model and their use in
   review. Verify hashes before executing anything. A key alone is insufficient.
2. Provision the supported official environment and enough scratch disk/RAM.
   Restrict allowed egress to the approved inference endpoint; retain TLS verification.
3. Inject the organizer’s own scoped credential into each authorized worker’s
   environment using their secrets system. No repository secret transfers to them.
4. For a one-case technical replay, use the local launcher above. For the official
   worker pool, prepare a private **credential-free** operational config: retain
   all scientific/guard values, keep `api_keys` empty, enable inference and set one
   approved shared run ID/root for the execution scope. Do this before workers
   import `model.py`; a parent-only in-memory change does not configure fresh
   worker subprocesses. This official-runner integration remains an organizer gate.
5. Execute their official acquisition/scoring process with their hidden data.
   Record real-model/evidence/readout coverage, errors, usage and scope/replay counts.
   Hidden outcomes and private journals stay inside their review environment.

## Account separation, limits and expiration

For repeat demonstrations, a dedicated reviewer project and narrowly scoped
service account are appropriate. Prefer `api.responses.write` only, subject to
its underlying role and Luna access; no admin, Files, Search or Agents permission
is needed for this transport. Set an approved expiration covering the review period,
monitor per-project usage and use a verified enforced project limit. Do not assume
an empty scope array is restricted: it removes key restrictions. No key/project
was created, changed, inspected through an authenticated API or rotated here.
[Service-account key scopes/expiry](https://developers.openai.com/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/subresources/api_keys/methods/create) ·
[Update scopes/expiry](https://developers.openai.com/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/methods/update)

The frozen runtime guard is $1 per forecast and $50 per shared execution scope. It is
not an account-wide cap; independent containers/replays can multiply exposure.
Its prices are historical engineering values and must be reviewed before a new
paid campaign. Provider spend alerts do not stop traffic; enforced hard limits
can stop affected requests, with propagation delay and possible small overage.
The proposed review limit must be approved and verified separately. This document
changes no existing account control. [Official spend-limit behavior](https://developers.openai.com/api/docs/guides/spend-limits)

## Original artifact and GitHub demonstration

The original scored ZIP contains an embedded credential in `submission_config.json`.
Its verified hash is recorded in [source equivalence](docs/SOURCE_EQUIVALENCE.md).
The credential-bearing original is not a release asset. This is known private
artifact exposure, not evidence that the key was published. Treat its continued
use/revocation as an owner decision; do not silently extract or reuse it for review.

The optional [workflow design](docs/workflow_examples/ble15a-review.yml) is stored
outside `.github/workflows` and is not activated. Before enabling it, an owner must
approve activation, a fixed reviewed commit, trusted operators, environment-required
reviewers, main-only deployment rules, an ephemeral isolated runner with approved
assets/dependencies and the dedicated Environment Secret. The workflow accepts
no arbitrary inputs or PR code and injects the key only in the last inference step.
It uploads no runtime, keys, journals or private outputs. Its current placeholder
commit deliberately fails closed. Local structural checks do not prove GitHub
protection settings or successful live execution.
[Environment protection](https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments) ·
[Secret inheritance and handling](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets) ·
[Untrusted PR risks](https://docs.github.com/en/actions/reference/security/securely-using-pull_request_target)
