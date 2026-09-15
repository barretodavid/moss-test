import unittest

from m5app.retry import retry_count

class RetryBoundTests(unittest.TestCase):
    def test_in_range(self):
        self.assertEqual(retry_count(3), 3)
    def test_upper_bound(self):
        self.assertEqual(retry_count(6), 5)
    def test_zero_becomes_one(self):
        self.assertEqual(retry_count(0), 1)
    def test_negative_becomes_one(self):
        self.assertEqual(retry_count(-3), 1)
