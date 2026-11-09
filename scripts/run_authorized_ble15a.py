#!/usr/bin/env python3
"""Local reviewer launcher around unchanged scored modules; never writes a key."""
import argparse
from contextlib import contextmanager, redirect_stdout
import importlib.util
import io
import json
import math
import os
from pathlib import Path
import sys
import urllib.request
import uuid

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from scripts.reproduce import verify_runtime


class BoundaryError(RuntimeError):
    pass


def validate_environment():
    if not os.environ.get('OPENAI_API_KEY'):
        raise BoundaryError('MISSING_ENVIRONMENT_CREDENTIAL')
    if os.environ.get('OPENAI_BASE_URL', 'https://api.openai.com/v1').rstrip('/') != 'https://api.openai.com/v1':
        raise BoundaryError('UNAPPROVED_API_BASE')
    if os.environ.get('PREDICTIVE_EVAL_LOCAL_SMOKE_TEST'):
        raise BoundaryError('LOCAL_SMOKE_CANNOT_BE_LIVE_INFERENCE')


@contextmanager
def openai_responses_only():
    """Guard the frozen urllib transport. No arbitrary URL, model or hosted tool."""
    original = urllib.request.OpenerDirector.open
    observed = []

    def guarded(opener, request, *args, **kwargs):
        if not isinstance(request, urllib.request.Request) or request.full_url != 'https://api.openai.com/v1/responses' or request.get_method() != 'POST':
            raise BoundaryError('UNAPPROVED_REQUEST')
        raw = request.data or b''
        key = os.environ.get('OPENAI_API_KEY', '')
        if not key or request.get_header('Authorization') != 'Bearer ' + key:
            raise BoundaryError('ENVIRONMENT_CREDENTIAL_NOT_USED')
        if key.encode() in raw:
            raise BoundaryError('CREDENTIAL_IN_BODY')
        body = json.loads(raw)
        if body.get('model') != 'gpt-6-luna' or body.get('reasoning') != {'mode': 'standard', 'effort': 'medium'} or body.get('service_tier') != 'default':
            raise BoundaryError('SCIENTIFIC_CONFIGURATION_CHANGED')
        if body.get('tools') != [] or body.get('store') is not False:
            raise BoundaryError('UNAPPROVED_HOSTED_TOOLS_OR_STORAGE')
        observed.append({'method': 'POST', 'endpoint': 'https://api.openai.com/v1/responses',
                         'model': 'gpt-6-luna', 'effort': 'medium', 'requested_tier': 'default',
                         'credential_in_body': False})
        return original(opener, request, *args, **kwargs)

    urllib.request.OpenerDirector.open = guarded
    try:
        yield observed
    finally:
        urllib.request.OpenerDirector.open = original


def configure_in_memory(runtime, scope_root):
    """Operational enable flag and private ledger path; no scientific overrides."""
    verify_runtime(runtime)
    sys.path[:0] = [str(runtime), str(runtime / 'src')]
    spec = importlib.util.spec_from_file_location('reviewer_scored_model', runtime / 'model.py')
    model = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(model)
    import production
    original = dict(production.CFG)
    production.CFG = {**original, 'enable_paid_inference': True, 'api_keys': {},
                      'run_budget_id': 'reviewer-' + uuid.uuid4().hex, 'run_budget_root': str(scope_root)}
    return model


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=('preflight', 'live'))
    parser.add_argument('--runtime', type=Path, required=True, help='Authorized sanitized unpacked reconstruction; never the private original')
    parser.add_argument('--input', type=Path, help='Authorized JSON [subject,item]; no target outcome')
    parser.add_argument('--labels', type=Path, help='Only legitimately revealed JSON [[input,0-or-1],...]')
    parser.add_argument('--output-dir', type=Path, help='New private directory outside this checkout')
    parser.add_argument('--allow-paid', action='store_true', help='Explicit operator spending opt-in; up to the frozen per-forecast guard')
    args = parser.parse_args(argv)
    try:
        if args.mode == 'preflight':
            result = verify_runtime(args.runtime.resolve())
            print(json.dumps({'status': result['status'], 'members_verified': len(result['assets']),
                              'environment_key_present': bool(os.environ.get('OPENAI_API_KEY')),
                              'API_requests': 0, 'live_credential_entitlement_verified': False}))
            return 0
        if not args.allow_paid or not args.input or not args.output_dir:
            raise BoundaryError('EXPLICIT_SPENDING_INPUT_AND_PRIVATE_OUTPUT_REQUIRED')
        validate_environment()
        output = args.output_dir.resolve()
        if output == ROOT or ROOT in output.parents:
            raise BoundaryError('LIVE_OUTPUT_MUST_BE_OUTSIDE_CHECKOUT')
        output.mkdir(mode=0o700, parents=False, exist_ok=False)
        if output.stat().st_mode & 0o077:
            raise BoundaryError('UNSAFE_OUTPUT_PERMISSIONS')
        # No restart/retry after a possibly uncertain invocation.
        (output / 'STARTED').write_text('One explicit live invocation; do not replay uncertain work.\n')
        inp = json.loads(args.input.read_text())
        labels = json.loads(args.labels.read_text()) if args.labels else []
        captured = io.StringIO()
        with redirect_stdout(captured):
            model = configure_in_memory(args.runtime.resolve(), output / 'runtime-state')
            with openai_responses_only() as requests:
                probability = model.predict(inp, labels)
        summaries = [json.loads(line.split(' ', 1)[1]) for line in captured.getvalue().splitlines()
                     if line.startswith('PAIEC_PRODUCTION_SUMMARY ')]
        if len(summaries) != 1 or not math.isfinite(probability) or not 0 <= probability <= 1:
            raise BoundaryError('MISSING_OR_INVALID_COMPLETION_RECEIPT')
        summary = summaries[0]
        full = summary.get('genuine_model_probability') is True and summary.get('full_retrieval_continuation') is True and len(requests) >= 2
        receipt = {'mode': 'authenticated_live_inference', 'status': 'FULL_BLE_RECEIPT' if full else 'INCOMPLETE_OR_EMERGENCY',
                   'probability': probability, 'native_submit': summary.get('genuine_submit'),
                   'model_derived': summary.get('genuine_model_probability'),
                   'initial_evidence_revised_belief': summary.get('full_retrieval_continuation'),
                   'budget': summary.get('budget'), 'transport_attempts': len(requests),
                   'key_source': 'execution environment', 'credential_written_to_config': False,
                   'scored_modules_modified': False, 'summary': summary}
        target = output / 'receipt.json'
        fd = os.open(target, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
        with os.fdopen(fd, 'w') as f:
            json.dump(receipt, f, indent=2); f.write('\n')
        print(json.dumps({k: v for k, v in receipt.items() if k != 'summary'}))
        return 0 if full else 2
    except Exception as exc:
        # No raw provider message, request body, credential, task text or traceback.
        print(json.dumps({'status': 'BLOCKED_OR_FAILED', 'exception_class': type(exc).__name__,
                          'stage': str(exc) if isinstance(exc, BoundaryError) else 'DETAIL_WITHHELD',
                          'successful_live_reproduction_claimed': False}))
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
