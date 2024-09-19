import unittest
import random
from algorithms.others.shuffle import shuffle


class TestShuffleFunction(unittest.TestCase):
    def test_shuffle(self):
        # Test that the list is modified
        numbers = [1, 2, 3, 4, 5]
        original_numbers = numbers.copy()
        shuffle(numbers)
        self.assertNotEqual(numbers, original_numbers)

    def test_shuffle_randomness(self):
        # Test that the shuffle is random
        numbers = list(range(20))
        shuffles = []
        for _ in range(10):
            numbers_copy = numbers.copy()
            shuffle(numbers_copy)
            shuffles.append(numbers_copy)
        self.assertEqual(len(set(tuple(x) for x in shuffles)), 10)

    def test_shuffle_empty_list(self):
        # Test that an empty list raises an error
        empty_list = []
        shuffle(empty_list)
        self.assertEqual(empty_list, [])

    def test_shuffle_non_list(self):
        # Test that a non-list input raises an error
        with self.assertRaises(ValueError):
            shuffle("12345")

    def test_shuffle_large_list(self):
        # Test that a large list is shuffled correctly
        large_list = list(range(1000))
        original_large_list = large_list.copy()
        shuffle(large_list)
        self.assertNotEqual(large_list, original_large_list)


if __name__ == '__main__':
    unittest.main()