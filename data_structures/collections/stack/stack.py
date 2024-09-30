from typing import Any, Generator, List, Optional, Union


class Stack:
    """
    A stack implementation using a singly linked list.

    Methods:
        from_list(elements): Alternative constructor, creates a Stack instance from a list.
        pop(): Pops a value from the stack.
        push(val): Pushes a value onto the stack.

    Special Methods:
        __bool__(): Checks if the stack is empty.
        __getitem__(index): Allows indexing, supports both integer indices and slice objects.
        __iter__(): Generator function to iterate over the stack elements.
        __len__(): Returns the number of items in the stack.
        __repr__(): Returns a string representation of the stack.
        __reversed__(): Returns a reversed iterator over the stack.
        __str__(): Returns a string representation of the stack.
    """

    class Node:
        """
        Represents a node in the linked list.
        
        Attributes:
            val (Any): The value stored in the node.
            next (Optional[Node]): Reference to the next node.
        """
        def __init__(self: 'Node', val: Any, next: Optional['Node'] = None) -> None:
            """
            Initializes a node

            Args:
                val (Any): The value stored in the node.
                next (Optional[Node]): Reference to the next node.
            """
            self.val: Any = val
            self.next: 'Node' = next

    class StackEmptyError(Exception):
        """
        Custom exception to be raised when attempting to access an element
        from an empty stack.

        Attributes:
            message (str): Custom message for empty stack.
        """
        def __init__(self: 'StackEmptyError', message: str = "StackEmptyError: The stack is empty.") -> None:
            """
            Initialize the exception.

            Args:
                message (str): Custom message for empty stack.
            """
            self.message: str = message
        
        def __str__(self: 'StackEmptyError') -> str:
            """
            Returns the exception message.

            Returns:
                str: The message for empty stack.
            """
            return self.message

    def __init__(self: 'Stack') -> None:
        """
        Initialize an empty stack.
        """
        self.__first: Node = None
        self._size: int = 0

    def push(self: 'Stack', val: Any) -> None:
        """
        Pushes a value onto the stack.

        Args:
            val (Any): The value to be pushed onto the stack.

        Raises:
            ValueError: If the val is None.
        """
        if val is None:
            raise ValueError("Cannot push None value onto the stack.")
            
        new_node = self.Node(val, next = self.__first)
        self.__first = new_node
        self._size += 1

    def pop(self: 'Stack') -> Any:
        """
        Pops a value from the stack.

        Returns:
            val (Any): The value popped from the stack.

        Raises:
            StackEmptyError: If the stack is empty.
        """
        if not self.__bool__():
            raise self.StackEmptyError()

        val = self.__first.val
        self.__first = self.__first.next
        self._size -= 1
        return val

    @classmethod
    def from_list(cls, elements: List[Any]) -> 'Stack':
        """
        Alternative constructor, creates a Stack instance from a list.

        Args:
            elements (List[Any]): List of elements to create a stack.

        Returns:
            stack (Stack): Returns the created instance of Stack.
        """
        stack = cls()

        for element in reversed(elements):
            stack.push(element)

        return stack

    def __bool__(self: 'Stack') -> bool:
        """
        Checks if the stack is empty.

        Returns:
            bool: True if the stack has elements, False otherwise.
        """
        return self.__first is not None

    def __getitem__(self: 'Stack', index: Union[int, slice]) -> Union[Any, List[Any]]:
        """
        Allows indexing, supports both integer indices and slice objects.

        Args:
            index (Union[int, slice]): The index or slice to retrieve items from the stack.

        Returns:
            Union[Any, List[Any]]: The item at the specified index or a list of items for the specified slice.

        Raises:
            IndexError: If the index is out of range.
            TypeError: If the argument is not an integer or slice.

        """
        # Case 1: Requesting a specific index
        if isinstance(index, int):
            if index >= self._size:
                raise IndexError("Index out of range.")

            index += self._size if index < 0 else 0
            current = self.__first
            for _ in range(index):
                current = current.next
            return current.val

        # Case 2: Requesting a slice
        elif isinstance(index, slice):
            start, stop, step = index.indices(self._size)
            return [self[i] for i in range(start, stop, step)]

        # Case 3: Invalid argument
        else:
            raise TypeError("Invalid argument.")

    def __iter__(self: 'Stack') -> Generator[Any, None, None]:
        """
        Generator function to iterate over the stack elements.

        Yields:
            Any: Value of the current node.
        """
        current = self.__first
        while current:
            yield current.val
            current = current.next

    def __len__(self: 'Stack') -> int:
        """
        Returns the number of items in the stack.

        Returns:
            int: The number of items in the stack.
        """
        return self._size

    def __reversed__(self: 'Stack') -> Generator[Any, None, None]:
        """
        Returns a reversed iterator over the stack.

        Returns:
            list: A list of stack elements in reverse order.
        """
        return reversed(list(self))

    def __repr__(self: 'Stack') -> str:
        """
        Returns a string representation of the stack.

        Returns:
            str: The string representation of the stack.
        """
        sequence = list(self)
        return f"{type(self).__name__}.from_list({sequence})"

    def __str__(self: 'Stack') -> str:
        """
        Return a string representation of the stack.

        Returns:
            str: The string representation of the stack.
        """
        sequence = map(str, list(self))
        return '[' + ' -> '.join(sequence) + ']'