import unittest
import random
from .randomized_queue import RandomizedQueue

class TestRandomizedQueue(unittest.TestCase):
    def test_init(self):
        queue = RandomizedQueue()
        self.assertEqual(queue.size, 0)

    def test_enqueue(self):
        queue = RandomizedQueue()
        queue.enqueue(1)
        self.assertEqual(queue.size, 1)

    def test_dequeue(self):
        queue = RandomizedQueue()
        queue.enqueue(1)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.size, 0)
        with self.assertRaises(RandomizedQueue.QueueEmptyError):
            queue.dequeue()

    def test_sample(self):
        queue = RandomizedQueue()
        queue.enqueue(1)
        self.assertIn(queue.sample(), [1])

    def test_from_list(self):
        elements = [1, 2, 3]
        queue = RandomizedQueue.from_list(elements)
        self.assertEqual(queue.size, len(elements))

    def test_repr_str(self):
        queue = RandomizedQueue.from_list([1])
        self.assertEqual(repr(queue), f"RandomizedQueue.from_list({[1]})")
        self.assertEqual(str(queue), f"[1]")

    def test_iter(self):
        queue = RandomizedQueue.from_list([1, 2, 3])
        self.assertEqual(len([item for item in queue]), 3)

    def test_randomness(self):
        # Test randomness of iterator
        queue = RandomizedQueue.from_list([0, 1, 2])
        iterations = 1000
        counts = {0: 0, 1: 0, 2: 0}
        for _ in range(iterations):
            for i, item in enumerate(queue):
                if i == item:
                    counts[item] += 1
        self.assertAlmostEqual(counts[0] / iterations, 1/3, places=1)
        self.assertAlmostEqual(counts[1] / iterations, 1/3, places=1)
        self.assertAlmostEqual(counts[2] / iterations, 1/3, places=1)

    def test_enqueue_none(self):
        queue = RandomizedQueue()
        with self.assertRaises(ValueError):
            queue.enqueue(None)

    def test_empty_queue(self):
        queue = RandomizedQueue()
        with self.assertRaises(RandomizedQueue.QueueEmptyError):
            queue.sample()
        with self.assertRaises(RandomizedQueue.QueueEmptyError):
            queue.dequeue()


if __name__ == "__main__":
    unittest.main()