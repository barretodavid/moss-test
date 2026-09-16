import unittest
from m5app.paging import page_size, default_page_size

class PagingTests(unittest.TestCase):
    def test_in_range(self):
        self.assertEqual(page_size(12), 12)
    def test_upper_bound(self):
        self.assertEqual(page_size(101), 100)

class DefaultPageSizeTests(unittest.TestCase):
    def test_returns_twelve(self):
        self.assertEqual(default_page_size(), 12)
