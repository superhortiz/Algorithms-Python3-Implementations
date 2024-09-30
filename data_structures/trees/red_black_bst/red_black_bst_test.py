import unittest
from data_structures import RedBlackBST
import random


class TestBST(unittest.TestCase):

    def test_init(self):
        bst = RedBlackBST()
        self.assertFalse(bst)

    def test_setitem(self):
        bst = RedBlackBST()
        bst[5] = "five"
        self.assertEqual(bst[5], "five")

    def test_getitem(self):
        bst = RedBlackBST()
        bst[5] = "five"
        self.assertEqual(bst[5], "five")

    def test_delitem(self):
        bst = RedBlackBST()
        bst[5] = "five"
        del bst[5]
        with self.assertRaises(KeyError):
            bst[5]

    def test_len(self):
        bst = RedBlackBST()
        bst[5] = "five"
        bst[3] = "three"
        self.assertEqual(len(bst), 2)

    def test_contains(self):
        bst = RedBlackBST()
        bst[5] = "five"
        self.assertTrue(5 in bst)
        self.assertFalse(3 in bst)

    def test_min_max(self):
        bst = RedBlackBST()
        bst[5] = "five"
        bst[3] = "three"
        bst[7] = "seven"
        self.assertEqual(bst.min(), 3)
        self.assertEqual(bst.max(), 7)

    def test_floor_ceiling(self):
        bst = RedBlackBST()
        bst[5] = "five"
        bst[3] = "three"
        bst[7] = "seven"
        self.assertEqual(bst.floor(4), 3)
        self.assertEqual(bst.ceiling(4), 5)

    def test_rank(self):
        bst = RedBlackBST()
        bst[5] = "five"
        bst[3] = "three"
        bst[7] = "seven"
        self.assertEqual(bst.rank(4), 1)

    def test_iter(self):
        bst = RedBlackBST()
        bst[5] = "five"
        bst[3] = "three"
        bst[7] = "seven"
        self.assertEqual(list(bst), ["three", "five", "seven"])

    def test_reversed(self):
        bst = RedBlackBST()
        bst[5] = "five"
        bst[3] = "three"
        bst[7] = "seven"
        self.assertEqual(list(reversed(bst)), ["seven", "five", "three"])

    def test_random_insertions(self):
        bst = RedBlackBST()
        keys = random.sample(range(100), 50)
        values = [f"value_{key}" for key in keys]
        for key, value in zip(keys, values):
            bst[key] = value
        self.assertEqual(len(bst), 50)
        for key in keys:
            self.assertTrue(key in bst)
            self.assertEqual(bst[key], f"value_{key}")

    def test_random_deletions(self):
        bst = RedBlackBST()
        keys = random.sample(range(100), 50)
        values = [f"value_{key}" for key in keys]
        for key, value in zip(keys, values):
            bst[key] = value
        delete_keys = random.sample(keys, 20)
        for key in delete_keys:
            del bst[key]
        self.assertEqual(len(bst), 30)
        for key in delete_keys:
            self.assertFalse(key in bst)

    def test_duplicate_keys(self):
        bst = RedBlackBST()
        bst[5] = "five"
        bst[5] = "five_again"
        self.assertEqual(bst[5], "five_again")

    def test_none_values(self):
        bst = RedBlackBST()
        with self.assertRaises(ValueError):
            bst[5] = None

    def test_non_integer_keys(self):
        bst = RedBlackBST()
        with self.assertRaises(ValueError):
            bst["five"] = "value"

    def test_empty_tree(self):
        bst = RedBlackBST()
        self.assertEqual(len(bst), 0)
        with self.assertRaises(KeyError):
            bst[5]

    def test_single_node_tree(self):
        bst = RedBlackBST()
        bst[5] = "five"
        self.assertEqual(len(bst), 1)
        self.assertEqual(bst.min(), 5)
        self.assertEqual(bst.max(), 5)


if __name__ == "__main__":
    unittest.main()