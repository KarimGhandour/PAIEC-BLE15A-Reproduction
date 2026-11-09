"""No network or real key: verify environment use through the frozen transport."""
from contextlib import redirect_stdout
import io
import json
import os
import unittest
from unittest.mock import patch
import urllib.request

from examples.offline_walkthrough import RUNTIME
from scripts.run_authorized_ble15a import BoundaryError, openai_responses_only, validate_environment
from r1api.responses import credential
import aims_r1_transport


class ReviewerAuthentication(unittest.TestCase):
    def test_environment_precedence_and_no_credential_is_fail_closed(self):
        with patch.dict(os.environ, {'OPENAI_API_KEY': 'synthetic-test-key'}, clear=True):
            self.assertEqual(credential({'api_keys': {'OPENAI_API_KEY': 'unused-placeholder'}}), 'synthetic-test-key')
            validate_environment()
        with patch.dict(os.environ, {}, clear=True), self.assertRaises(BoundaryError):
            validate_environment()

    def test_frozen_transport_key_only_in_authorization_to_expected_endpoint(self):
        seen = []

        class Reply:
            status = 200
            headers = {'x-request-id': 'req_synthetic'}
            def __enter__(self): return self
            def __exit__(self, *args): pass
            def read(self, *args): return b'{"synthetic":true}'

        def offline_open(opener, request, *args, **kwargs):
            self.assertEqual(request.get_header('Authorization'), 'Bearer synthetic-test-key')
            self.assertNotIn(b'synthetic-test-key', request.data)
            seen.append(request.full_url)
            return Reply()

        body = {'model': 'gpt-6-luna', 'reasoning': {'mode': 'standard', 'effort': 'medium'},
                'service_tier': 'default', 'tools': [], 'store': False, 'input': 'Invented fixture'}
        with patch.dict(os.environ, {'OPENAI_API_KEY': 'synthetic-test-key'}, clear=True):
            with patch.object(urllib.request.OpenerDirector, 'open', offline_open):
                with openai_responses_only() as operations:
                    reply, _, _ = aims_r1_transport.post_r1('synthetic-test-key', body, 1, 'synthetic-client', lambda *a: None)
        self.assertEqual(reply, {'synthetic': True})
        self.assertEqual(seen, ['https://api.openai.com/v1/responses'])
        self.assertEqual(len(operations), 1)

    def test_arbitrary_endpoint_fast_and_hosted_tools_are_rejected_before_network(self):
        body = {'model': 'gpt-6-luna', 'reasoning': {'mode': 'standard', 'effort': 'medium'},
                'service_tier': 'default', 'tools': [], 'store': False}
        with patch.dict(os.environ, {'OPENAI_API_KEY': 'synthetic-test-key'}, clear=True):
            with patch.object(urllib.request.OpenerDirector, 'open', side_effect=AssertionError('Network forbidden')):
                with openai_responses_only():
                    req = urllib.request.Request('https://example.invalid/responses', data=b'{}')
                    with self.assertRaises(BoundaryError): urllib.request.urlopen(req)
                    for changed in ({'service_tier': 'fast'}, {'tools': [{'type': 'web_search'}]}, {'model': 'other'}):
                        req = urllib.request.Request('https://api.openai.com/v1/responses', data=json.dumps({**body, **changed}).encode(),
                                                     headers={'Authorization': 'Bearer synthetic-test-key'})
                        with self.assertRaises(BoundaryError): urllib.request.urlopen(req)


if __name__ == '__main__':
    unittest.main()
