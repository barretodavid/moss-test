import unittest
from m5app.paging import page_size, MIN_PAGE_SIZE, MAX_PAGE_SIZE, DEFAULT_PAGE_SIZE

class PagingTests(unittest.TestCase):
    def test_in_range(self):
        self.assertEqual(page_size(12), 12)
    def test_upper_bound(self):
        self.assertEqual(page_size(101), 100)
    def test_zero_returns_minimum(self):
        self.assertEqual(page_size(0), MIN_PAGE_SIZE)
    def test_negative_returns_minimum(self):
        self.assertEqual(page_size(-7), MIN_PAGE_SIZE)
    def test_lower_boundary(self):
        self.assertEqual(page_size(MIN_PAGE_SIZE), MIN_PAGE_SIZE)
    def test_upper_boundary_exact(self):
        self.assertEqual(page_size(MAX_PAGE_SIZE), MAX_PAGE_SIZE)
    def test_none_returns_default(self):
        self.assertEqual(page_size(None), DEFAULT_PAGE_SIZE)
    def test_non_integer_raises(self):
        with self.assertRaises(TypeError):
            page_size(2.5)
    def test_string_raises(self):
        with self.assertRaises(TypeError):
            page_size("20")
    def test_bool_raises(self):
        with self.assertRaises(TypeError):
            page_size(True)
