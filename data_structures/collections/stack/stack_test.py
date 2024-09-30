import unittest
from data_structures import Stack


class TestStack(unittest.TestCase):
    def test_init(self):
        stack = Stack()
        self.assertIsNone(stack._Stack__first)
        self.assertEqual(len(stack), 0)

    def test_push(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(len(stack), 1)

    def test_pop(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(len(stack), 0)
        with self.assertRaises(Stack.StackEmptyError):
            stack.pop()

    def test_is_empty(self):
        stack = Stack()
        self.assertFalse(bool(stack))
        stack.push(1)
        self.assertTrue(bool(stack))

    def test_from_list(self):
        elements = [1, 2, 3]
        stack = Stack.from_list(elements)
        self.assertEqual(len(stack), len(elements))
        self.assertEqual([item for item in stack], elements)

    def test_repr_str(self):
        stack = Stack.from_list([1, 2, 3])
        self.assertEqual(repr(stack), f"Stack.from_list({[1, 2, 3]})")
        self.assertEqual(str(stack), "[1 -> 2 -> 3]")

    def test_iter(self):
        elements = [1, 2, 3]
        stack = Stack.from_list(elements)
        self.assertEqual([item for item in stack], [1, 2, 3])
        self.assertEqual([item for item in reversed(stack)], list(reversed(elements)))

    def test_getitem(self):
        elements = list(range(100))
        stack = Stack.from_list(elements)
        self.assertEqual(stack[0], elements[0])
        self.assertEqual(stack[-1], elements[-1])
        self.assertEqual(stack[15:30], elements[15:30])


if __name__ == "__main__":
    unittest.main()