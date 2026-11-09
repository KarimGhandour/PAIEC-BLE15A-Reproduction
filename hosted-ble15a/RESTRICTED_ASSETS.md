# Six restricted assets: exact inventory and unresolved access

This inventory is a provenance record, not distribution clearance. Every row has **unverified public and private-reviewer redistribution permission**. The private scored ZIP and this repository’s MIT code license do not grant rights to the data. See [DATA_PROVENANCE.md](../DATA_PROVENANCE.md) for lineage and access distinctions.

| Exact runtime path | Bytes | SHA-256 | Purpose |
|---|---:|---|---|
| `data/evidence.xz.bin` | 382,120,380 | `71c4794b96e2acd0f4f49c64aa5f982d8765f00767c38337461c5790a48e7eba` | Filtered numeric/keyword retrieval, source grouping and exclusion IDs. |
| `data/firewall_static_cache.json` | 6,177 | `1b09e48998484a1babd4f2b2cb7c22c9b242459df12e30bf186d1103688b4da4` | Accelerates frozen exclusion setup without removing dynamic per-forecast exclusions. |
| `data/protected_inputs.json` | 547,490 | `26ec64c9bdcc2ef301fddf345f27109069e9808497340ab2dd4069699db217ed` | Exact, source-group and near-duplicate research-input exclusions; current target/acquisitions are appended dynamically. |
| `data/semantic_items.json` | 4,914,337 | `e00695e97ab98c974753c6f96c194c29e9b360ff50fa1e37f70eeeae77f803ba` | Index-row-to-item identity, ordering, admissibility and evidence content. |
| `data/semantic_vectors.npy` | 21,195,392 | `eca8f8c6566d6d0e3a4e0387bf62db9a3d841377f08d9a8c6aa38c78ed2377c9` | Query-to-item similarity ranking and reported similarity values. |
| `data/traces_chunked.sqlite` | 311,312,384 | `67459dbde2cd90cb6ee923f740162985545c2b24d5255e2efc6c6e38533ad7ac` | Retrieval of actual historical attempt trace excerpts. |

All six require approved exact copies for the existing reconstruction path. A public deterministic regeneration procedure has not been verified. The separately retrievable pinned MiniLM weight is not one of these six files. Its Apache-2.0 terms do not extend to the index input content.

The detailed [JSON inventory](RESTRICTED_ASSETS.json) records origin, processing, role, rights status and gaps. Until permission is established, do not put any of these files into a public release. An authorized private handoff is a proposed route, not an already approved access procedure.
