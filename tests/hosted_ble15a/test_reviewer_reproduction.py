"""Meaningful boundaries for frozen A, using only invented inputs and replies."""
import json
from pathlib import Path
import tempfile
import unittest

from examples.reviewer_fixture import run_fixture
from r1api.responses import BudgetError
from scripts.reproduce import asset_status, hosted_results, trace_check
from production_budget import ProductionBudget, refuse_budget_fallback


class ReviewerReproduction(unittest.TestCase):
    def test_all_six_populated_budgets_and_acquired_exclusion(self):
        for b in (0, 1, 3, 7, 15, 31):
            with self.subTest(budget=b):
                out = run_fixture(b)
                self.assertEqual(out['readout'], 'submitted')
                self.assertEqual(out['probability'], .68)
                self.assertEqual(out['requests'], 2)
                start = next(d for event, d in out['events'] if event == 'forecast_start')
                self.assertEqual(start['acquired_labels'], b)
                self.assertEqual(out['eligible_items'], ['relevant', 'weak'] if b == 0 else ['relevant'])

    def test_spending_exhaustion_fails_closed_even_with_a_belief(self):
        for index in (0, 1):
            with self.subTest(index=index), self.assertRaises(BudgetError):
                run_fixture(7, failure_at=index, failure_kind='financial')

    def test_provider_and_oversized_failures_preserve_valid_earlier_belief(self):
        for kind in ('provider', 'oversized'):
            out = run_fixture(7, failure_at=1, failure_kind=kind)
            self.assertEqual((out['readout'], out['probability']), ('intermediate_return', .55))
            out = run_fixture(7, failure_at=0, failure_kind=kind)
            self.assertEqual(out['readout'], 'fallback')
            self.assertNotEqual(out['probability'], .55)

    def test_worker_exception_and_invalid_model_probability_are_not_final_submit(self):
        out = run_fixture(7, failure_kind='worker')
        self.assertEqual((out['readout'], out['probability']), ('intermediate_return', .55))
        out = run_fixture(7, malformed=True)
        self.assertEqual(out['readout'], 'fallback')
        self.assertFalse(any(event == 'belief_validated' for event, _ in out['events']))

    def test_missing_assets_are_explicit_and_all_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            report = asset_status(Path(directory))
        self.assertEqual(report['status'], 'BLOCKED')
        self.assertEqual(len(report['assets']), 7)
        self.assertEqual(sum(x['delivery'] == 'authorized-exact-data' for x in report['assets']), 6)
        self.assertTrue(all(x['status'] == 'missing' for x in report['assets']))

    def test_public_aggregates_and_observed_metadata_have_distinct_scopes(self):
        self.assertEqual(hosted_results()['official_headline'], '0.1590607804')
        trace = trace_check()
        self.assertEqual(trace['new_API_requests'], 0)
        self.assertIs(trace['native_submit'], False)

    def test_shared_financial_scope_retains_uncertain_cost_and_refuses_baseline(self):
        runtime = Path(__file__).resolve().parents[2] / 'hosted-ble15a/runtime'
        config = json.loads((runtime / 'submission_config.json').read_text())
        with tempfile.TemporaryDirectory() as directory:
            config['run_budget_root'] = str(Path(directory) / 'scope')
            first = ProductionBudget(config, lambda *args: None)
            first.reserve('synthetic-one', '30')
            second = ProductionBudget(config, lambda *args: None)
            second.reserve('synthetic-two', '20')
            first.close_uncertain_local_requests(['synthetic-one', 'synthetic-two'])
            self.assertEqual(first.snapshot()['held'], 50_000_000)
            with self.assertRaises(BudgetError):
                second.reserve('synthetic-over-cap', '.01')
        with self.assertRaises(RuntimeError):
            refuse_budget_fallback([{'event': 'fallback', 'reason': 'BudgetError'}])


if __name__ == '__main__':
    unittest.main()
