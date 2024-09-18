import unittest
from data_structures.stack import Stack

class TestStack(unittest.TestCase):
    def test_init(self):
        stack = Stack()
        self.assertIsNone(stack._Stack__first)
        self.assertEqual(stack.size, 0)

    def test_push(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.size, 1)

    def test_pop(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(stack.size, 0)
        with self.assertRaises(Stack.StackEmptyError):
            stack.pop()

    def test_is_empty(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())
        stack.push(1)
        self.assertFalse(stack.is_empty())

    def test_from_list(self):
        elements = [1, 2, 3]
        stack = Stack.from_list(elements)
        self.assertEqual(stack.size, len(elements))
        self.assertEqual([item for item in stack], elements)

    def test_repr_str(self):
        stack = Stack.from_list([1, 2, 3])
        self.assertEqual(repr(stack), f"Stack.from_list({[1, 2, 3]})")
        self.assertEqual(str(stack), "1 -> 2 -> 3")

    def test_iter(self):
        stack = Stack.from_list([1, 2, 3])
        self.assertEqual([item for item in stack], [1, 2, 3])


if __name__ == "__main__":
    unittest.main()