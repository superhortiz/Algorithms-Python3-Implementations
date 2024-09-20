import unittest
from .union_find import UnionFind

class TestUnionFind(unittest.TestCase):
    def test_init(self):
        uf = UnionFind(5)
        self.assertEqual(len(uf._UnionFind__id), 5)

    def test_root(self):
        uf = UnionFind(5)
        self.assertEqual(uf._UnionFind__root(0), 0)

    def test_connected(self):
        uf = UnionFind(5)
        uf.union(0, 1)
        self.assertTrue(uf.connected(0, 1))

    def test_union(self):
        uf = UnionFind(5)
        uf.union(0, 1)
        uf.union(1, 2)
        self.assertTrue(uf.connected(0, 2))

    def test_disconnected(self):
        uf = UnionFind(5)
        self.assertFalse(uf.connected(0, 1))

    def test_none_input(self):
        uf = UnionFind(5)
        with self.assertRaises(ValueError):
            uf.union(None, 1)
        with self.assertRaises(ValueError):
            uf.connected(None, 1)

    def test_out_of_range(self):
        uf = UnionFind(5)
        with self.assertRaises(IndexError):
            uf.union(5, 1)
        with self.assertRaises(IndexError):
            uf.connected(5, 1)

    def test_components(self):
        uf = UnionFind(5)
        uf.union(0, 1)
        uf.union(1, 2)
        uf.union(3, 4)

    def test_count(self):
        uf = UnionFind(5)
        self.assertEqual(uf.count, 5)
        uf.union(0, 1)
        self.assertEqual(uf.count, 4)
        uf.union(1, 2)
        self.assertEqual(uf.count, 3)
        uf.union(3, 4)
        self.assertEqual(uf.count, 2)


if __name__ == "__main__":
    unittest.main()