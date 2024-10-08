import unittest
from data_structures import Queue


class TestQueue(unittest.TestCase):
    def test_init(self):
        queue = Queue()
        self.assertIsNone(queue._Queue__first)
        self.assertIsNone(queue._Queue__last)
        self.assertEqual(len(queue), 0)

    def test_enqueue(self):
        queue = Queue()
        queue.enqueue(1)
        self.assertEqual(len(queue), 1)
        self.assertEqual(queue.peek_first(), 1)
        self.assertEqual(queue.peek_last(), 1)

    def test_dequeue(self):
        queue = Queue()
        queue.enqueue(1)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(len(queue), 0)
        with self.assertRaises(Queue.QueueEmptyError):
            queue.dequeue()

    def test_peek_first_last(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        self.assertEqual(queue.peek_first(), 1)
        self.assertEqual(queue.peek_last(), 2)

    def test_is_empty(self):
        queue = Queue()
        self.assertFalse(bool(queue))
        queue.enqueue(1)
        self.assertTrue(bool(queue))

    def test_from_list(self):
        elements = [1, 2, 3]
        queue = Queue.from_list(elements)
        self.assertEqual(len(queue), len(elements))
        self.assertEqual([item for item in queue], elements)

    def test_repr_str(self):
        queue = Queue.from_list([1, 2, 3])
        self.assertEqual(repr(queue), f"Queue.from_list({[1, 2, 3]})")
        self.assertEqual(str(queue), "1 -> 2 -> 3")

    def test_iter(self):
        queue = Queue.from_list([1, 2, 3])
        self.assertEqual([item for item in queue], [1, 2, 3])
        self.assertEqual([item for item in reversed(queue)], list(reversed([1, 2, 3])))

    def test_queue_empty_error(self):
        queue = Queue()
        with self.assertRaises(Queue.QueueEmptyError):
            queue.dequeue()
        with self.assertRaises(Queue.QueueEmptyError):
            queue.peek_first()
        with self.assertRaises(Queue.QueueEmptyError):
            queue.peek_last()

    def test_getitem(self):
        elements = list(range(100))
        queue = Queue.from_list(elements)
        self.assertEqual(queue[0], elements[0])
        self.assertEqual(queue[-1], elements[-1])
        self.assertEqual(queue[15:30], elements[15:30])


if __name__ == "__main__":
    unittest.main()