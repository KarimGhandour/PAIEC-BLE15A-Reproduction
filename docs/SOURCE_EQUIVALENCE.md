# Connection to scored BLE 1.5-A #1032237

The local original `PAIEC_BLE15_A_PRODUCTION_001.zip` was stream-hashed again:
**695,451,321 bytes**, SHA-256
`90a6a22560328e4ff5ec3f86375dbf567aecf802d2632fe6829878b339be7c3c`.
This verifies the recorded local artifact; it is not a fresh hash obtained from
inside the organizer’s evaluated container.

The [machine-readable report](SOURCE_EQUIVALENCE.json) lists all 35 Python modules
and their original hashes. Every module under `hosted-ble15a/runtime` is byte-identical
to its member in that scored ZIP. The local hardening helpers live outside this
runtime and do not change prompts, tools, exclusions, acquisition handling,
MiniLM, recurrent beliefs or the Completion policy.

| Original member class | Public/reconstruction disposition |
|---|---|
| 63 nonconfiguration bundled members, including 35 Python modules | Unchanged byte contents |
| 6 derived evidence/firewall files plus 1 public MiniLM weight | Omitted, with exact size/hash metadata; original member hashes verified locally |
|`submission_config.json` | Secret removed and paid inference disabled |
|`PACKAGE_HASHES.json` | Regenerated to describe sanitized contents |
|Outer ZIP | Different metadata/compression and SHA-256 are expected |

Thus 70 of 72 member contents match in the preserved authorized reconstruction.
The original archive’s secret-detection result located a credential pattern in
`submission_config.json` only. No credential value is reproduced here. The original
ZIP remains private and unchanged; its key must not be reused as a public fixture.

The public immutable `v1.5.0-rc.1` release points to commit
`4d37176f2386cfc2ebcdb63eddfdf61c9d68267f`. Historical R1 remains at
`f50814a750aefad56378aa5b0e0e94c076bb7b58` under `v1.0.0-r1`.
This dedicated reviewer package changes tooling/docs outside the scored source;
it does not move either tag or replace the release asset.

Historical `submission/` is the CLI R1 research implementation. The scored
Responses/Completion implementation is `hosted-ble15a/runtime/`. Results from the
two cannot be presented as the same hosted experiment. See [RESULTS.md](../RESULTS.md).
