from typing import Any, Generator, List, Optional

class Deque:
    """
    A double-ended queue (deque) implementation using a doubly linked list.

    Attributes:
        size (int): number of items in the deque.

    Methods:
        add_first(val): Adds a value to the front of the deque.
        add_last(val): Adds a value to the back of the deque.
        from_list(elements): Alternative constructor, creates a Deque instance from a list.        
        is_empty(): Checks if the deque is empty.
        peek_first(): Returns the value of the first element in the deque.
        peek_last(): Returns the value of the last element in the deque.
        remove_first(): Removes and returns the value from the front of the deque.
        remove_last(): Removes and returns the value from the back of the deque.

    Special Methods:
        __iter__(): Generator function to iterate over the deque elements.
        __repr__(): Returns a string representation of the deque.
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
        self.__size: int = 0

    @property
    def size(self: 'Deque') -> int:
        """
        Returns the number of items in the deque.

        This attribute is read-only and cannot be modified directly.

        Returns:
            int: The number of items in the deque.
        """
        return self.__size

    @size.setter
    def size(self: 'Deque', *args, **kwargs) -> None:
        """
        Raises AttributeError to prevent modification.

        The size attribute is updated internally by add and remove operations.
        Attempting to set it directly will raise an AttributeError.

        Raises:
            AttributeError: Always raised to prevent modification.
        """
        raise AttributeError("This attribute is immutable")

    def add_first(self: 'Deque', val: Any) -> None:
        """
        Adds an item to the front of the deque.

        Args:
            val (Any): The item to be added.

        Raises:
            ValueError: If the val is None.
        """
        if val is None:
            raise ValueError

        self.__size += 1
        if self.is_empty():
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

        self.__size += 1
        if self.is_empty():
            self.__first = self.__last = self.Node(val)
        else:
            new_node = self.Node(val, prev = self.__last)
            self.__last.next = new_node
            self.__last = new_node

    def is_empty(self: 'Deque') -> bool:
        """
        Checks if the deque is empty.

        Returns:
            bool: True if the deque is empty, False otherwise.
        """
        return self.__first is None

    def remove_first(self: 'Deque') -> Any:
        """
        Removes and returns the item from the front of the deque.

        Returns:
            Any: The removed item.

        Raises:
            DequeEmptyError: If the deque is empty.
        """
        if self.is_empty():
            raise self.DequeEmptyError()

        self.__size -= 1
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
        if self.is_empty():
            raise self.DequeEmptyError()

        self.__size -= 1
        item = self.__last.val
        self.__last = self.__last.prev
        if self.__last is None:
            self.__first = None
        else:
            self.__last.next = None
        return item

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

    @classmethod
    def from_list(cls: 'Deque', elements: List[Any]) -> 'Deque':
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

    def __repr__(self: 'Deque') -> str:
        """
        Returns a string representation of the deque.

        Returns:
            str: A string showing the items in the deque.
        """
        sequence = [item for item in self]
        return f"{self.__class__.__name__}.from_list({sequence})"

    def __str__(self: 'Deque') -> str:
        """
        Returns a string representation of the deque.

        Returns:
            str: A string showing the items in the deque.
        """
        sequence = [str(item) for item in self]
        return ' <-> '.join(sequence)

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