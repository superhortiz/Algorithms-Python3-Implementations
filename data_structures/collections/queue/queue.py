from typing import Any, Generator, List, Optional, Union


class Queue:
    """
    A queue implementation using a singly linked list.

    Methods:
        dequeue(): Removes and returns the value from the front of the queue.
        enqueue(val): Adds a value to the end of the queue.
        from_list(elements): Alternative constructor, creates a Queue instance from a list.
        peek_first(): Returns the value of the first element in the queue.
        peek_last(): Returns the value of the last element in the queue.


    Special Methods:
        __bool__(): Checks if the queue is empty.
        __getitem__(index): Allows indexing, supports both integer indices and slice objects.
        __iter__(): Generator function to iterate over the queue elements.
        __len__(): Returns the number of items in the queue.
        __repr__(): Returns a string representation of the queue.
        __reversed__(): Returns a reversed iterator over the queue.
        __str__(): Returns a string representation of the queue.
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
            Initializes a node.

            Args:
                val (Any): The value stored in the node.
                next (Optional[Node]): Reference to the next node.
            """
            self.val: Any = val
            self.next: 'Node' = next

    class QueueEmptyError(Exception):
        """
        Custom exception to be raised when attempting to access an element
        from an empty queue.

        Attributes:
            message (str): Custom message for empty queue.
        """
        def __init__(self: 'QueueEmptyError', message: str = "QueueEmptyError: The queue is empty.") -> None:
            """
            Initializes the exception.

            Args:
                message (str): Custom message for empty queue.
            """
            self.message: str = message
        
        def __str__(self: 'QueueEmptyError') -> str:
            """
            Returns the exception message.
            """
            return self.message

    def __init__(self: 'Queue') -> None:
        """
        Initializes an empty queue.
        """
        self.__first: Node = None
        self.__last: Node = None
        self._size: int = 0

    def enqueue(self: 'Queue', val: Any) -> None:
        """
        Add an item to the end of the queue.

        Args:
            val (Any): The item to be added.

        Raises:
            ValueError: If the val is None.
        """
        if val is None:
            raise ValueError("Cannot push None value onto the queue.")

        self._size += 1
        oldlast = self.__last
        self.__last = Queue.Node(val)
        
        if oldlast is None:
            self.__first = self.__last
        else:
            oldlast.next = self.__last

    def dequeue(self: 'Queue') -> Any:
        """
        Removes and returns the value from the front of the queue.

        Returns:
            Any: The removed item.

        Raises:
            QueueEmptyError: If the queue is empty.
        """
        if not self.__bool__():
            raise self.QueueEmptyError()

        self._size -= 1
        val = self.__first.val
        self.__first = self.__first.next

        if not self.__bool__():
            self.__last = None
        return val

    def peek_first(self: 'Queue') -> Any:
        """
        Returns the value of the first element in the queue.

        Returns:
            Any: The value of the first node in the queue.
        
        Raises:
            QueueEmptyError: If the queue is empty.
        """
        if self.__first is None:
            raise self.QueueEmptyError()
        return self.__first.val

    def peek_last(self: 'Queue') -> Any:
        """
        Returns the value of the last element in the queue.

        Returns:
            Any: The value of the last node in the queue.
        
        Raises:
            QueueEmptyError: If the queue is empty.
        """
        if self.__last is None:
            raise self.QueueEmptyError()
        return self.__last.val

    @classmethod
    def from_list(cls, elements: List[Any]) -> 'Queue':
        """
        Alternative constructor, creates a Queue instance from a list.

        Args:
            elements (List[Any]): List of elements to create a queue.

        Returns:
            queue (Queue): Returns the created instance of Queue.
        """
        queue = cls()

        for element in elements:
            queue.enqueue(element)

        return queue

    def __bool__(self: 'Queue') -> bool:
        """
        Checks if the queue is empty.

        Returns:
            bool: True if the queue has elements, False otherwise.
        """
        return self.__first is not None

    def __getitem__(self: 'Queue', index: Union[int, slice]) -> Union[Any, List[Any]]:
        """
        Allows indexing, supports both integer indices and slice objects.

        Args:
            index (Union[int, slice]): The index or slice to retrieve items from the queue.

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

    def __iter__(self: 'Queue') -> Generator[Any, None, None]:
        """
        Generator function to iterate over the queue elements.
        
        Yields:
            Any: Value of the current node.
        """
        current = self.__first
        while current:
            yield current.val
            current = current.next

    def __len__(self: 'Queue') -> int:
        """
        Returns the number of items in the queue.

        This attribute is read-only and cannot be modified directly.

        Returns:
            int: The number of items in the queue.
        """
        return self._size

    def __repr__(self: 'Queue') -> str:
        """
        Returns a string representation of the queue.

        Returns:
            str: The string representation of the queue.
        """
        sequence = list(self)
        return f"{type(self).__name__}.from_list({sequence})"

    def __reversed__(self: 'Queue') -> Generator[Any, None, None]:
        """
        Returns a reversed iterator over the queue.

        Returns:
            list: A list of queue elements in reverse order.
        """
        return reversed(list(self))

    def __str__(self: 'Queue') -> str:
        """
        Returns a string representation of the queue.

        Returns:
            str: The string representation of the queue.
        """
        sequence = map(str, list(self))
        return ' -> '.join(sequence)