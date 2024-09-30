from typing import Any, Generator, List, Optional, Union


class Deque:
    """
    A double-ended queue (deque) implementation using a doubly linked list.

    Methods:
        add_first(val): Adds a value to the front of the deque.
        add_last(val): Adds a value to the back of the deque.
        from_list(elements): Alternative constructor, creates a Deque instance from a list.        
        peek_first(): Returns the value of the first element in the deque.
        peek_last(): Returns the value of the last element in the deque.
        remove_first(): Removes and returns the value from the front of the deque.
        remove_last(): Removes and returns the value from the back of the deque.

    Special Methods:
        __bool__(): Checks if the deque is empty.
        __getitem__(index): Allows indexing, supports both integer indices and slice objects.
        __iter__(): Generator function to iterate over the deque elements.
        __len__(): Returns the number of items in the deque.
        __repr__(): Returns a string representation of the deque.
        __reversed__(): Generator function to iterate over the deque elements in reverse.
        __str__(): Returns a string representation of the deque.
    """

    class Node:
        """
        Represents a node in the doubly linked list.
        
        Attributes:
            val (Any): The value stored in the node.
            next (Optional[Node]): Reference to the next node.
            prev (Optional[Node]): Reference to the previous node.
        """
        def __init__(self: 'Node', val: Any, next: Optional['Node'] = None, prev: Optional['Node'] = None) -> None:
            """
            Initializes a Node.

            Args:
                val (Any): The value stored in the node.
                next (Optional[Node]): Reference to the next node.
                prev (Optional[Node]): Reference to the previous node.
            """
            self.val: Any = val
            self.next: Optional['Node'] = next
            self.prev: Optional['Node'] = prev

    class DequeEmptyError(Exception):
        """
        Custom exception to be raised when attempting to access an element
        from an empty queue.

        Attributes:
            message (str): Custom message for empty deque.
        """
        def __init__(self: 'DequeEmptyError', message: str = "DequeEmptyError: The deque is empty.") -> None:
            """
            Initialize the exception.
            """
            self.message: str = message
        
        def __str__(self: 'DequeEmptyError') -> str:
            """
            Returns the exception message.
            """
            return self.message

    def __init__(self: 'Deque') -> None:
        """
        Initializes an empty deque.
        """
        self.__first: Optional[Node] = None
        self.__last: Optional[Node] = None
        self._size: int = 0

    def add_first(self: 'Deque', val: Any) -> None:
        """
        Adds an item to the front of the deque.

        Args:
            val (Any): The item to be added.

        Raises:
            ValueError: If the val is None.
        """
        if val is None:
            raise ValueError("Cannot push None value onto the deque.")

        self._size += 1
        if not self.__bool__():
            self.__first = self.__last = self.Node(val)
        else:
            new_node = self.Node(val, next = self.__first)
            self.__first.prev = new_node
            self.__first = new_node

    def add_last(self: 'Deque', val: Any) -> None:
        """
        Adds an item to the back of the deque.

        Args:
            val (Any): The item to be added.

        Raises:
            ValueError: If the val is None.
        """
        if val is None:
            raise ValueError

        self._size += 1
        if not self.__bool__():
            self.__first = self.__last = self.Node(val)
        else:
            new_node = self.Node(val, prev = self.__last)
            self.__last.next = new_node
            self.__last = new_node

    def peek_first(self: 'Deque') -> Any:
        """
        Returns the value of the first element in the deque.

        Returns:
            Any: The value of the first node in the deque.
        
        Raises:
            DequeEmptyError: If the deque is empty.
        """
        if self.__first is None:
            raise self.DequeEmptyError()
        return self.__first.val

    def peek_last(self: 'Deque') -> Any:
        """
        Returns the value of the last element in the deque.

        Returns:
            Any: The value of the last node in the deque.
        
        Raises:
            DequeEmptyError: If the deque is empty.
        """
        if self.__last is None:
            raise self.DequeEmptyError()
        return self.__last.val

    def remove_first(self: 'Deque') -> Any:
        """
        Removes and returns the item from the front of the deque.

        Returns:
            Any: The removed item.

        Raises:
            DequeEmptyError: If the deque is empty.
        """
        if not self.__bool__():
            raise self.DequeEmptyError()

        self._size -= 1
        item = self.__first.val
        self.__first = self.__first.next
        if self.__first is None:
            self.__last = None
        else:
            self.__first.prev = None
        return item

    def remove_last(self: 'Deque') -> Any:
        """
        Removes and returns the item from the back of the deque.

        Returns:
            Any: The removed item.

        Raises:
            DequeEmptyError: If the deque is empty.
        """
        if not self.__bool__():
            raise self.DequeEmptyError()

        self._size -= 1
        item = self.__last.val
        self.__last = self.__last.prev
        if self.__last is None:
            self.__first = None
        else:
            self.__last.next = None
        return item

    @classmethod
    def from_list(cls, elements: List[Any]) -> 'Deque':
        """
        Alternative constructor, creates a Deque instance from a list.

        Args:
            elements (List[Any]): List of elements to create a deque.

        Returns:
            deque (Deque): Returns the created instance of Deque.
        """
        deque = cls()
        for element in elements:
            deque.add_last(element)
        return deque

    def __bool__(self: 'Deque') -> bool:
        """
        Checks if the deque is empty.

        Returns:
            bool: True if the deque has elements, False otherwise.
        """
        return self.__first is not None

    def __getitem__(self: 'Deque', index: Union[int, slice]) -> Union[Any, List[Any]]:
        """
        Allows indexing, supports both integer indices and slice objects.

        Args:
            index (Union[int, slice]): The index or slice to retrieve items from the deque.

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

    def __iter__(self) -> Generator[Any, None, None]:
        """
        Generator function to iterate over the deque elements.
        
        Yields:
            Any: Value of the current node.
        """
        current = self.__first
        while current:
            yield current.val
            current = current.next

    def __len__(self: 'Deque') -> int:
        """
        Returns the number of items in the deque.

        Returns:
            int: The number of items in the deque.
        """
        return self._size

    def __repr__(self: 'Deque') -> str:
        """
        Returns a string representation of the deque.

        Returns:
            str: A string showing the items in the deque.
        """
        sequence = [item for item in self]
        return f"{self.__class__.__name__}.from_list({sequence})"

    def __reversed__(self) -> Generator[Any, None, None]:
        """
        Generator function to iterate over the deque elements in reverse.
        
        Yields:
            Any: Value of the current node.
        """
        current = self.__last
        while current:
            yield current.val
            current = current.prev

    def __str__(self: 'Deque') -> str:
        """
        Returns a string representation of the deque.

        Returns:
            str: A string showing the items in the deque.
        """
        sequence = [str(item) for item in self]
        return ' <-> '.join(sequence)