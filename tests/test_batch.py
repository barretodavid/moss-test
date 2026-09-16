import unittest
from m5app.batch import page_sizes

class BatchTests(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(page_sizes([]), [])
    def test_normalizes_each_entry(self):
        self.assertEqual(page_sizes([None, 0, 50, 500]), [20, 1, 50, 100])
    def test_returns_new_list(self):
        values = [12, 20]
        result = page_sizes(values)
        self.assertIsNot(result, values)
        self.assertEqual(result, [12, 20])
    def test_does_not_mutate_input(self):
        values = [None, 0, 50, 500]
        page_sizes(values)
        self.assertEqual(values, [None, 0, 50, 500])
    def test_result_is_new_list_when_all_in_range(self):
        values = [1, 100]
        result = page_sizes(values)
        self.assertIsNot(result, values)
        self.assertEqual(result, [1, 100])
