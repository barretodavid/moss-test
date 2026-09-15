import json
import os
import time
import unittest
import urllib.request
from m5app.retry import retry_count

class RetryTests(unittest.TestCase):
    def test_service_and_range(self):
        url = os.environ["FIXTURE_ENDPOINT"]
        for attempt in range(30):
            try:
                with urllib.request.urlopen(url, timeout=2) as response:
                    limit = json.load(response)["maximum"]
                break
            except OSError:
                time.sleep(0.2)
        else:
            self.fail("fixture service unavailable")
        self.assertEqual(retry_count(limit + 1), limit)
        self.assertEqual(retry_count(3), 3)
