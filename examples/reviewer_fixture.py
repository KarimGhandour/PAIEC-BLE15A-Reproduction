"""Invented six-budget/failure fixture; never presented as an observed forecast."""
from contextlib import closing
import json
from pathlib import Path
import tempfile
from examples.offline_walkthrough import AuditedDB, TARGET, TeachingJournal, create_fixture, forecast, typed_action
from r1api.responses import ResponsesClient, APIError, BudgetError, InputEnvelopeError


def revealed_labels(budget):
    assert budget in (0, 1, 3, 7, 15, 31)
    return [[[TARGET[0], {'benchmark_id': 'toy-math', 'item_content':
             'Count vertices in a tree.' if i == 0 else 'Invented acquired exercise ' + str(i)}], i % 2]
            for i in range(budget)]


def run_fixture(budget, *, failure_at=None, failure_kind='provider', malformed=False):
    labels = revealed_labels(budget)
    requests = []; outputs = []
    with tempfile.TemporaryDirectory(prefix='paiec-reviewer-fixture-') as directory:
        root = Path(directory); path = root / 'fixture.sqlite'; create_fixture(path)
        log = TeachingJournal(root)

        def store(inp, acquired):
            if failure_kind == 'worker':
                raise RuntimeError('Synthetic worker exception')
            return AuditedDB(path=path, targets=[{'input': inp}] + [{'input': x} for x, _ in acquired])

        def post(body, timeout):
            index = len(requests); requests.append(body)
            assert body['service_tier'] == 'default' and body['model'] == 'gpt-6-luna'
            assert body['reasoning']['effort'] == 'medium' and body['tools'] == []
            if index == failure_at:
                errors = {'provider': APIError, 'financial': BudgetError, 'oversized': InputEnvelopeError}
                raise errors[failure_kind]('Synthetic injected failure', stage='offline_fixture')
            if index:
                assert all(item in body['input'] for item in outputs[-1])
            action = typed_action('get_scores' if index == 0 else 'submit', .55 if index == 0 else .68)
            if malformed:
                action = typed_action('submit', -1)
            output = [{'type': 'reasoning', 'id': 'synthetic-' + str(index), 'encrypted_content': 'synthetic-opaque'},
                      {'type': 'message', 'role': 'assistant', 'content': [{'type': 'output_text', 'text': json.dumps(action)}]}]
            outputs.append(output)
            return {'id': 'synthetic-' + str(index), 'model': body['model'], 'status': 'completed',
                    'service_tier': 'default', 'output': output, 'usage': {'input_tokens': 100, 'output_tokens': 40}}

        p = forecast(TARGET, labels, config={'enable_paid_inference': False, 'max_forecast_usd': 1, 'max_output_tokens': 8192},
                     journal=log, client_factory=lambda c, j: ResponsesClient(c, j, post=post), db_factory=store)
        with closing(AuditedDB(path=path, targets=[{'input': TARGET}] + [{'input': x} for x, _ in labels])) as db:
            eligible = [r[0] for r in db.c.execute('select iid from permitted_items order by id')]
        readout = next((kind for kind, _ in reversed(log.events) if kind in ('submitted', 'intermediate_return', 'fallback')), None)
        return {'kind': 'invented_mock_fixture', 'budget': budget, 'probability': p, 'readout': readout,
                'requests': len(requests), 'events': log.events, 'eligible_items': eligible, 'paid_requests': 0}
