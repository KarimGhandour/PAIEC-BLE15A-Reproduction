#!/usr/bin/env python3
"""Reviewer entry point. Defaults require no credential, assets, or API calls."""
import argparse
import csv
from decimal import Decimal
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
HOSTED = ROOT / 'hosted-ble15a'
spec = importlib.util.spec_from_file_location('scored_reconstructor', HOSTED / 'reconstruct.py')
reconstructor = importlib.util.module_from_spec(spec)
spec.loader.exec_module(reconstructor)


def asset_status(directory, *, runtime=False):
    manifest = json.loads((HOSTED / 'ARTIFACT_MANIFEST.json').read_text())
    entries = manifest['members'] if runtime else [x for x in manifest['members'] if x['delivery'] != 'bundled']
    results = []
    for item in entries:
        path = directory / item['path']
        status = 'missing'
        if path.is_symlink():
            status = 'symlink_rejected'
        elif path.is_file():
            status = 'verified' if path.stat().st_size == item['bytes'] and reconstructor.sha256(path) == item['sha256'] else 'different'
        results.append({'path': item['path'], 'bytes': item['bytes'], 'sha256': item['sha256'],
                        'delivery': item['delivery'], 'status': status})
    return {'status': 'PASS' if all(x['status'] == 'verified' for x in results) else 'BLOCKED',
            'scope': 'Complete sanitized runtime' if runtime else 'Six restricted assets plus pinned public model weight',
            'assets': results, 'paid_requests': 0}


def verify_runtime(directory):
    result = asset_status(directory, runtime=True)
    if result['status'] != 'PASS':
        raise ValueError('RUNTIME_MISSING_OR_DIFFERENT')
    allowed = {x['path'] for x in result['assets']} | {'PACKAGE_HASHES.json'}
    for path in directory.rglob('*'):
        if path.is_symlink():
            raise ValueError('RUNTIME_SYMLINK')
        if path.is_file() and path.relative_to(directory).as_posix() not in allowed:
            raise ValueError('UNREVIEWED_RUNTIME_FILE')
    cfg = json.loads((directory / 'submission_config.json').read_text())
    if cfg.get('api_keys') != {} or cfg.get('enable_paid_inference') is not False:
        raise ValueError('RUNTIME_MUST_HAVE_SANITIZED_OFFLINE_CONFIG')
    return result


def hosted_results():
    score = json.loads((ROOT / 'results/hosted_ble15a_aggregates/score.json').read_text())
    with (ROOT / 'results/hosted_ble15a_aggregates/groups.csv').open() as f:
        rows = list(csv.DictReader(f))
    weights = list(map(lambda x: Decimal(str(x)), score['official_weights']))
    tol = Decimal(str(score['rounding_tolerance']))
    means = [sum(Decimal(row['b' + str(b)]) for row in rows) / len(rows) for b in score['budgets']]
    group_alcs = [sum(w * Decimal(row['b' + str(b)]) for w, b in zip(weights, score['budgets'])) for row in rows]
    assert len(rows) == score['groups'] == 9
    assert sum(int(row['pairs']) for row in rows) == score['distinct_pairs'] == 489
    assert all(abs(v - Decimal(str(ref))) <= tol for v, ref in zip(means, score['displayed_mean_brier']))
    assert all(abs(v - Decimal(row['published_group_alc'])) <= tol for v, row in zip(group_alcs, rows))
    alc = sum(group_alcs) / len(group_alcs)
    assert abs(alc - Decimal(score['official_formative_alc'])) <= tol
    return {'status': 'PASS', 'official_headline': score['official_formative_alc'],
            'ALC_from_rounded_public_cells': str(alc), 'tolerance': str(tol), 'groups': len(rows),
            'pairs': sum(int(row['pairs']) for row in rows),
            'scope': 'Published aggregate arithmetic; no hidden labels, fresh forecasts, raw bootstrap or score rerun.'}


def trace_check():
    trace = json.loads((ROOT / 'examples/observed_standard_b0.json').read_text())
    assert trace['kind'] == 'observed_metadata_only'
    assert trace['source_is_mock'] is False and trace['source_has_paid_requests'] is True
    assert trace['evidence_content_released'] is False and trace['native_submit'] is False
    assert len(trace['responses']) == 2
    for row in trace['responses']:
        assert row['validated'] and row['model'] == 'gpt-6-luna' and row['service_tier'] == 'default'
        assert 0 <= row['belief_probability'] <= 1 and row['encrypted_continuation_present']
        assert row['output_tokens'] >= row['reasoning_tokens'] >= 0
    assert trace['readout_probability'] == trace['responses'][-1]['belief_probability'] == .88
    assert trace['readout'] == 'intermediate_return' and trace['reason'] == 'Third_call_not_admitted'
    return {'status': 'PASS', 'mode': 'offline observed metadata replay', 'validated_responses': 2,
            'probability': .88, 'native_submit': False, 'new_API_requests': 0,
            'scope': 'Checks released telemetry coherence; does not reconstruct prompts, evidence or generate a prediction.'}


def run(command):
    subprocess.run([sys.executable, *command], cwd=ROOT, check=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='mode', required=True)
    offline = sub.add_parser('offline', help='Source, schema, budget, failure, auth-boundary and aggregate checks; no network needed')
    offline.add_argument('--notebooks', action='store_true', help='Also execute both notebooks and generate HTML')
    assets = sub.add_parser('assets', help='Validate authorized copies without downloading or installing anything')
    assets.add_argument('--asset-dir', type=Path, required=True)
    assets.add_argument('--runtime', action='store_true', help='Validate the full sanitized unpacked runtime')
    sub.add_parser('results', help='Historical aggregate checks plus official hosted rounded-cell arithmetic')
    sub.add_parser('trace', help='Replay the released observed metadata; no API or private records')
    args = parser.parse_args()
    if args.mode == 'assets':
        result = asset_status(args.asset_dir, runtime=args.runtime)
        print(json.dumps(result, indent=2))
        return 0 if result['status'] == 'PASS' else 2
    if args.mode in ('offline', 'results'):
        run(['scripts/verify_results.py'])
        print(json.dumps(hosted_results(), indent=2))
    if args.mode in ('offline', 'trace'):
        print(json.dumps(trace_check(), indent=2))
    if args.mode == 'offline':
        run(['scripts/check_source.py'])
        run(['scripts/validate_release.py'])
        run(['-m', 'unittest', 'discover', '-s', 'tests/hosted_ble15a', '-p', 'test_*.py', '-v'])
        if args.notebooks:
            run(['scripts/verify_notebook.py'])
            run(['scripts/verify_observed_notebook.py'])
        print(json.dumps({'status': 'PASS', 'mode': 'offline', 'paid_requests': 0,
                          'scope': 'Synthetic frozen-controller tests, observed metadata replay and aggregate arithmetic. No exact hidden score reproduction.'}))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
