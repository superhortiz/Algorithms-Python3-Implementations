from typing import Any, Generator, List, Optional

class Queue:
    """
    A queue implementation using a singly linked list.

    Attributes:
        size (int): number of items in the queue.

    Methods:
        dequeue(): Removes and returns the value from the front of the queue.
        enqueue(val): Adds a value to the end of the queue.
        from_list(elements): Alternative constructor, creates a Queue instance from a list.
        is_empty(): Checks if the queue is empty.
        peek_first(): Returns the value of the first element in the queue.
        peek_last(): Returns the value of the last element in the queue.


    Special Methods:
        __iter__(): Generator function to iterate over the queue elements.
        __repr__(): Returns a string representation of the queue.
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
        self.__size: int = 0

    @property
    def size(self: 'Queue') -> int:
        """
        Returns the number of items in the queue.

        This attribute is read-only and cannot be modified directly.

        Returns:
            int: The number of items in the queue.
        """
        return self.__size

    @size.setter
    def size(self: 'Queue', *args, **kwargs) -> None:
        """
        Raises AttributeError to prevent modification.

        The size attribute is updated internally by add and remove operations.
        Attempting to set it directly will raise an AttributeError.

        Raises:
            AttributeError: Always raised to prevent modification.
        """
        raise AttributeError("This attribute is immutable")

    def is_empty(self: 'Queue') -> bool:
        """
        Check if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return self.__first is None

    def enqueue(self: 'Queue', val: Any) -> None:
        """
        Add an item to the end of the queue.

        Args:
            val (Any): The item to be added.

        Raises:
            ValueError: If the val is None.
        """
        if val is None:
            raise ValueError

        self.__size += 1
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
        if self.is_empty():
            raise self.QueueEmptyError()

        self.__size -= 1
        val = self.__first.val
        self.__first = self.__first.next

        if self.is_empty():
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
    def from_list(cls: 'Queu', elements: List[Any]) -> 'Queue':
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

    def __repr__(self: 'Queue') -> str:
        """
        Returns a string representation of the queue.

        Returns:
            str: The string representation of the queue.
        """
        sequence = [item for item in self]
        return f"{self.__class__.__name__}.from_list({sequence})"

    def __str__(self: 'Queue') -> str:
        """
        Returns a string representation of the queue.

        Returns:
            str: The string representation of the queue.
        """
        sequence = [str(item) for item in self]
        return ' -> '.join(sequence)

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