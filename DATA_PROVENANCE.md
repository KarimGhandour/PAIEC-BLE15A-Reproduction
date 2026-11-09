# Data provenance and the six exact external files

Code availability and data redistribution are separate. The current release has
**unverified public and private-reviewer distribution clearance** for the six
assembled evidence/firewall assets. Their private Codabench inclusion and active
retrieval eligibility do not grant distribution rights. The words “restricted”
and “do not redistribute” record a handling boundary while clearance is absent.

The [machine-readable inventory](hosted-ble15a/RESTRICTED_ASSETS.json) records each
exact filename, size, SHA-256, source, processing lineage, dependency role, access
status and verification gaps. The [compact table](hosted-ble15a/RESTRICTED_ASSETS.md)
is the reviewer checklist. The public package omits all six actual files.

## Underlying sources and processing

The pinned upstream research snapshot is `aims-foundations/measurement-db` at
`54074453da7b9911be0f48e4c560be547bc84d21`. The [upstream inventory](hosted-ble15a/UPSTREAM_DATA_INVENTORY.json)
records 304 selected raw files and hashes. Gated access to those inputs is not an
independently verified derivation route to the exact runtime files.

- **Evidence corpus:** source-specific admitted measurements, metadata and task
  text were materialized in SQLite. Unresolved distribution families were physically
  removed in an earlier deployment build. Later compaction removed unreachable
  numeric rows/build tables and XZ-compressed the database. Some text excluded
  from numerical retrieval remains for duplicate checks/global FTS statistics;
  inference filtering does not establish whole-file distribution clearance.
- **Trace database:** prepared trace records retain tool-visible 4,000-character
  prefixes, original full-text character counts/hashes and response ordering.
  Selected unreachable records were removed before a lossless prepared-row
  migration to SQLite/zlib chunks. The preserved migration comparison covered
  2,255,645 prepared rows. This is not lossless preservation of every raw trace byte.
- **Semantic map/vectors:** deterministic source-group/content-hash selection,
  representation preprocessing and source exclusions produced 13,799 index entries.
  Their pinned local MiniLM embeddings have 384 dimensions. Exact model availability
  does not establish permission to redistribute source representations or index data.
- **Protected input manifest:** 202 historical research entries—32 evaluation targets,
  16 development targets and 154 previously acquired inputs. Their canonical assembled
  payload matched frozen A. Acquisition outcomes were discarded during assembly;
  cohort records retain linkable source/response identifiers. Contents include task
  text and subject/harness metadata. This lineage is historical local research;
  no hidden organizer target/outcome reconstruction is claimed. Record-level source
  and disclosure conditions still need review before sharing.
- **Firewall cache:** a precomputed blocked-ID closure binds the exact corpus,
  protected inputs, family exclusions and policy. IDs depend on that corpus;
  the cache cannot safely be substituted or omitted to make a package easier to run.

## Captured licensing evidence and unresolved conditions

[Source-specific captured terms](hosted-ble15a/runtime/data/RETRIEVAL_ELIGIBILITY_AND_LICENSES.json)
are an audit record, not current external legal clearance. They include MIT,
Apache/BSD, attribution, share-alike, noncommercial and third-party content
conditions. The active-permission policy explicitly calls its eligibility choices
conservative research decisions rather than legal determinations.

Trace sources include AlgoTune (MIT), BABILong (Apache/BSD components),
BRACE/CAF-Score (Apache/MIT with underlying audio terms), DAVE (MIT), EditBench (Apache),
Finegrain T2I (conflicting MIT/CC-BY declarations retained) and SWE-rebench (CC-BY).
The final ChartMuseum trace store is empty; corpus rights remain a separate issue.
Compression, truncation, SQLite conversion and embeddings do not by themselves
remove source obligations. Dataset access terms may also govern onward transfer.

## Access choices

| Route | Required decision |
|---|---|
| Public complete download | Actual retained-content rights, attribution/notices and protected-input disclosure clearance |
| Private named-reviewer handoff | Approved recipients, original access obligations and permission for the exact derivative transfer; not automatically exempt |
| Reviewer regeneration | Permitted upstream access plus a verified preparation path; exact or equivalence evidence disclosed |

No guaranteed asset-delivery process or verified independent public exact
regenerator is currently established. The smallest external question is whether
AIMS/organizer review arrangements permit access to this credential-sanitized
exact derivative bundle for named authorized reviewers, under what conditions,
and which third-party conditions still require separate clearance. No external
contact is implied by this document.

The public MiniLM Safetensors weight is separately pinned by the artifact manifest
and Apache-2.0 notice. It is not one of the six restricted files. See the original
[source/asset guide](hosted-ble15a/README_OPENREVIEW.md) and [third-party notices](THIRD_PARTY_NOTICES.md).
