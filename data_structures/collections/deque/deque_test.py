import unittest
from data_structures import Deque


class TestDeque(unittest.TestCase):
    """Test Deque data structure implementation"""

    def setUp(self):
        """Set up a fresh Deque for each test."""
        self.deque = Deque()

    def test_initialization(self):
        """Test the initialization of an empty Deque."""
        self.assertEqual(len(self.deque), 0)
        self.assertFalse(bool(self.deque))

    def test_add_first(self):
        """Test adding elements to the front of the Deque."""
        self.deque.add_first(1)
        self.assertEqual(len(self.deque), 1)
        self.assertEqual(self.deque.peek_first(), 1)
        self.deque.add_first(2)
        self.assertEqual(len(self.deque), 2)
        self.assertEqual(self.deque.peek_first(), 2)

    def test_add_last(self):
        """Test adding elements to the end of the Deque."""
        self.deque.add_last(1)
        self.assertEqual(len(self.deque), 1)
        self.assertEqual(self.deque.peek_last(), 1)
        self.deque.add_last(2)
        self.assertEqual(len(self.deque), 2)
        self.assertEqual(self.deque.peek_last(), 2)

    def test_remove_first(self):
        """Test removing elements from the front of the Deque."""
        self.deque.add_first(1)
        self.deque.add_first(2)
        self.assertEqual(self.deque.remove_first(), 2)
        self.assertEqual(len(self.deque), 1)
        self.assertEqual(self.deque.peek_first(), 1)

    def test_remove_last(self):
        """Test removing elements from the end of the Deque."""
        self.deque.add_last(1)
        self.deque.add_last(2)
        self.assertEqual(self.deque.remove_last(), 2)
        self.assertEqual(len(self.deque), 1)
        self.assertEqual(self.deque.peek_last(), 1)

    def test_peek_first(self):
        """Test peeking at the first element."""
        self.deque.add_first(1)
        self.assertEqual(self.deque.peek_first(), 1)
        self.deque.add_first(2)
        self.assertEqual(self.deque.peek_first(), 2)

    def test_peek_last(self):
        """Test peeking at the last element."""
        self.deque.add_last(1)
        self.assertEqual(self.deque.peek_last(), 1)
        self.deque.add_last(2)
        self.assertEqual(self.deque.peek_last(), 2)

    def test_is_empty(self):
        """Test checking if the Deque is empty."""
        self.assertFalse(bool(self.deque))
        self.deque.add_first(1)
        self.assertTrue(bool(self.deque))

    def test_len(self):
        """Test the size of the Deque."""
        self.assertEqual(len(self.deque), 0)
        self.deque.add_first(1)
        self.deque.add_last(2)
        self.assertEqual(len(self.deque), 2)

    def test_repr(self):
        """Test the string representation of the Deque."""
        self.deque.add_first(1)
        self.deque.add_last(2)
        self.assertEqual(repr(self.deque), "Deque.from_list([1, 2])")

    def test_str(self):
        """Test the string conversion of the Deque."""
        self.deque.add_first(1)
        self.deque.add_last(2)
        self.assertEqual(str(self.deque), "1 <-> 2")

    def test_iteration(self):
        """Test iteration over the Deque."""
        self.deque.add_first(1)
        self.deque.add_last(2)
        self.assertEqual(list(iter(self.deque)), [1, 2])

    def test_next(self):
        """Test the next element in the iterator."""
        self.deque.add_first(1)
        self.deque.add_last(2)
        iterator = iter(self.deque)
        self.assertEqual(next(iterator), 1)
        self.assertEqual(next(iterator), 2)

    def test_from_list(self):
        """Test creating a Deque from a list."""
        self.deque = Deque.from_list([1, 2, 3])
        self.assertEqual(len(self.deque), 3)
        self.assertEqual(self.deque.peek_first(), 1)
        self.assertEqual(self.deque.peek_last(), 3)

    def test_remove_first_empty(self):
        """Test removing the first element from an empty Deque."""
        with self.assertRaises(Deque.DequeEmptyError):
            self.deque.remove_first()

    def test_remove_last_empty(self):
        """Test removing the last element from an empty Deque."""
        with self.assertRaises(Deque.DequeEmptyError):
            self.deque.remove_last()

    def test_peek_first_empty(self):
        """Test peeking at the first element of an empty Deque."""
        with self.assertRaises(Deque.DequeEmptyError):
            self.deque.peek_first()

    def test_peek_last_empty(self):
        """Test peeking at the last element of an empty Deque."""
        with self.assertRaises(Deque.DequeEmptyError):
            self.deque.peek_last()


if __name__ == '__main__':
    unittest.main()