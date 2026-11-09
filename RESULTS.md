# Results, provenance and verification scope

The selected competition result is **BLE 1.5-A #1032237, official formative Brier
ALC 0.1590607804**. Lower Brier loss is better. Historical CLI R1, local API pilots,
mock engineering campaigns and failed hosted candidates remain separate evidence.

| Claim or result family | Released support | What the offline command verifies | Remaining limit |
|---|---|---|---|
| Hosted A: ALC 0.1590607804; 9 groups; 489 pairs; 6 budgets | `results/hosted_ble15a_aggregates/score.json` and `groups.csv` | Equal-group weighted ALC from rounded cells, per-budget means, group/pair totals and rounding tolerance | Exact headline is a recorded organizer result; hidden outcomes, raw probabilities, acquisition paths and a fresh score rerun are unavailable |
| Historical CLI confirmation: direct 0.203883 to R1 final 0.153728; gain 0.050155 | Confirmation aggregate cells/reference and original scorer functions | Point Brier/NLL aggregation, initial/final decomposition and agreement with recorded references | 32 questions at B0/B7 from previously encountered families; not a matched hosted baseline. Original clustered interval [0.001569, 0.103059] is a retained reference, not regenerated bootstrap |
| Development/ledger/effort studies | Public aggregate cells, ledger/xhigh references and frozen numerical functions | Development/confirmation, equal-family ledger and Medium/xhigh point arithmetic | Raw prediction/outcome/source-group records and original resampling unavailable; recorded uncertainties cannot be rebuilt from loss summaries |
| Ledger B7 gain 0.014907; interval spans zero | Ledger aggregate cells/reference | Point arithmetic | Uncertainty remains reference-only. Shrinkage proxy delta −0.003375 in decision ledger is a separate historical proxy, not scored-A improvement |
| Factor transfer 0.340420 vs scalar 0.272994; reverse 0.283372 vs 0.216085 | MF-001 reference/settings/functions | Recorded gain arithmetic and synthetic numerical tests where requested | Requires original arrays, group splits and encoder cache for historical rerun; not paired with BLE |
| Early-stop 49-readout panel: 96 vs 99 attempts, 3.03% saved; separate history+0.014ALC harm | `results/decision_ledger.csv` | Existence and arithmetic interpretation of the recorded summary | Counterfactual historical replay; underlying traces and paired outcome records not publicly regenerated here |
| A.2 reliability simulation: 3,000 forecasts, 9,020 requests, 200 faults; 2,820 native + 180 earlier, 0 emergency | `results/reliability.json` | Readout-count accounting | Historical mocked A.2 campaign, not observed scored-A coverage or hosted reliability |
| Native tool-call adapter: 2.20 vs 3.00 requests; 24.86 vs 19.90 seconds | Decision ledger | Recorded summary only | Separate adapter experiment; incomplete finalization confounds speed. No promotion claim |
| Local worker tests and hosted concurrency diagnostic | Decision ledger and deployment documentation | Recorded scope/limitations | Host assignment, total wall time, throughput and completion probability cannot be inferred from the score |
| Hosted #1031040/#1032500 and Fast A.2 #1033843 failed | Decision ledger; A.2 diagnostic `PAIEC-UNKNOWN-001` | Accurate recorded status/cause wording | Exact causes remain unverified; no assertion of timeout or of a repaired root cause |
| Teaching fixture: 0.55 to 0.68, filtered counts 9/20 | `examples/offline_walkthrough.py` | Executes actual controller and SQLite filtering on invented inputs/replies | Illustrative mechanism, not measured model accuracy |
| Observed Standard local readout 0.88 | `examples/observed_standard_b0.json` and second notebook | Two validated-response metadata, tool sequence and intermediate readout coherence | Authentic historical metadata, not a released full evidence trajectory; no target outcome or Brier claim |

Run `python scripts/reproduce.py results` for existing historical point checks and
hosted rounded-cell arithmetic. Run `python scripts/reproduce.py offline --notebooks`
for controller fixtures and notebook regeneration as well. The original scorer’s
ALC weights are 0.1/0.2/0.2/0.2/0.2/0.1 at budgets 0/1/3/7/15/31. Group sizes are
not used as weights for the headline equal-group score. Rounded feedback supports
agreement within its recorded tolerance, not re-creation of full-precision labels.

The flagship notebook’s scientific charts derive from the released result files
and reference summaries. Figures that show retained confidence intervals remain
reference displays. Re-executing a plot does not independently regenerate those
intervals. No newly generated demonstration is presented as a historical live call.

[Scientific claims](docs/scientific_claims.md) and the [decision ledger](results/decision_ledger.csv)
retain the fuller scientific qualifications. This hardening task changes none of
the scored source, approved figures, paper or scientific numerical records.
