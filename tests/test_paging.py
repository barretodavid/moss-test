import unittest
from m5app.paging import page_size

class PagingTests(unittest.TestCase):
    def test_in_range(self):
        self.assertEqual(page_size(12), 12)
    def test_upper_bound(self):
        self.assertEqual(page_size(101), 100)
    def test_lower_bound(self):
        self.assertEqual(page_size(0), 1)
        self.assertEqual(page_size(-3), 1)
        self.assertEqual(page_size(1), 1)
    def test_boundary_values(self):
        self.assertEqual(page_size(2), 2)
        self.assertEqual(page_size(100), 100)
    def test_none_returns_default(self):
        self.assertEqual(page_size(None), 20)
    def test_numeric_clamping_unchanged(self):
        self.assertEqual(page_size(0), 1)
        self.assertEqual(page_size(101), 100)
