import unittest
from .binary_heap import BinaryHeap

class TestBinaryHeap(unittest.TestCase):
    def test_insert(self):
        heap = BinaryHeap()
        heap.insert(5)
        heap.insert(10)
        self.assertEqual(str(heap), "[10, 5]")

    def test_del_max(self):
        heap = BinaryHeap()
        heap.insert(5)
        heap.insert(10)
        self.assertEqual(heap.del_max(), 10)
        self.assertEqual(str(heap), "[5]")

    def test_peek_max(self):
        heap = BinaryHeap()
        heap.insert(5)
        heap.insert(10)
        self.assertEqual(heap.peek_max(), 10)
        self.assertEqual(str(heap), "[10, 5]")

    def test_sink(self):
        heap = BinaryHeap()
        heap.insert(5)
        heap.insert(10)
        heap.insert(3)
        self.assertEqual(str(heap), "[10, 5, 3]")

    def test_swim(self):
        heap = BinaryHeap()
        heap.insert(3)
        heap.insert(5)
        heap.insert(10)
        self.assertEqual(str(heap), "[10, 3, 5]")

    def test_empty(self):
        heap = BinaryHeap()
        with self.assertRaises(IndexError):
            heap.del_max()
        with self.assertRaises(IndexError):
            heap.peek_max()

    def test_none_insert(self):
        heap = BinaryHeap()
        with self.assertRaises(ValueError):
            heap.insert(None)


if __name__ == "__main__":
    unittest.main()