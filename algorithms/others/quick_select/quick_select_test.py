import unittest
from algorithms import quick_select


class TestQuickSelectFunction(unittest.TestCase):
    def test_quick_select(self):
        numbers = [5, 2, 8, 3, 1, 6, 4]
        k = 4
        result = quick_select(numbers, k)
        self.assertEqual(result, 4)

    def test_sorted_list(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        k = 5
        result = quick_select(numbers, k)
        self.assertEqual(result, 5)

    def test_list_with_duplicates(self):
        numbers = [4, 2, 4, 3, 1, 4, 6, 4]
        k = 4
        result = quick_select(numbers, k)
        self.assertEqual(result, 4)

    def test_single_element_list(self):
        numbers = [42]
        k = 1
        result = quick_select(numbers, k)
        self.assertEqual(result, 42)

    def test_empty_list(self):
        numbers = []
        k = 1
        with self.assertRaises(ValueError):
            quick_select(numbers, k)

    def test_negative_numbers(self):
        numbers = [-5, -2, -8, -3, -1, -6, -4]
        k = 3
        result = quick_select(numbers, k)
        self.assertEqual(result, -5)


if __name__ == '__main__':
    unittest.main()
