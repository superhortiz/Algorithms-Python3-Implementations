import random
from typing import Any, Generator, List
from copy import deepcopy

class RandomizedQueue:
    """
    A randomized queue implementation using a dynamic array (Python list) for efficient operations.
    The 'RandomizedQueue' class ensures that each iterator returns the items in uniformly random order.

    Attributes:
        size (int): number of items in the randomized queue.

    Methods:
        dequeue(): Removes and returns a random item from the randomized queue.
        enqueue(val): Adds an item to the randomized queue.
        from_list(elements): Alternative constructor, creates a Randomized Queue instance from a list.
        is_empty(): Checks if the randomized queue is empty.
        sample(): Returns a random item from the randomized queue without removing it.

    Special Methods:
        __iter__(): Returns an iterator over a shuffled copy of the elements in the randomized queue.
        __repr__(): Returns a string representation of the randomized queue.
        __str__(): Returns a string representation of the randomized queue.
    """

    class QueueEmptyError(Exception):
        """
        Custom exception to be raised when attempting to access an element
        from an empty queue.

        Attributes:
            message (str): Custom message for empty queue.
        """
        def __init__(self: 'QueueEmptyError', message: str = "QueueEmptyError: The queue is empty.") -> None:
            """
            Initialize the exception.
            
            Args:
                message (str): Custom message for empty queue.
            """
            self.message: str = message
        
        def __str__(self: 'QueueEmptyError') -> str:
            """
            Returns the exception message.
            """
            return self.message

    def __init__(self: 'RandomizedQueue') -> None:
        """
        Initializes an empty randomized queue.
        """
        self.__list: List[Any] = [] # Internal list to store elements
        self.__size: int = 0 # Number of elements in the queue

    @property
    def size(self: 'RandomizedQueue') -> int:
        """
        Returns the number of items in the randomized queue.

        This attribute is read-only and cannot be modified directly.

        Returns:
            int: The number of items in the randomized queue.
        """
        return self.__size

    @size.setter
    def size(self: 'RandomizedQueue', *args, **kwargs) -> None:
        """
        Raises AttributeError to prevent modification.

        The size attribute is updated internally by add and remove operations.
        Attempting to set it directly will raise an AttributeError.

        Raises:
            AttributeError: Always raised to prevent modification.
        """
        raise AttributeError("This attribute is immutable")

    def is_empty(self: 'RandomizedQueue') -> bool:
        """
        Checks if the randomized queue is empty.

        Returns:
            True if empty, False otherwise.
        """
        return self.__size == 0

    def enqueue(self: 'RandomizedQueue', item: Any) -> None:
        """
        Adds an item to the randomized queue.

        Args:
            item: The item to enqueue.

        Raises:
            ValueError: If the item is None.
        """
        if item is None:
            raise ValueError

        self.__list.append(item)
        self.__size += 1

    def dequeue(self: 'RandomizedQueue') -> Any:
        """
        Removes and returns a random item from the randomized queue.

        Returns:
            The dequeued item.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise self.QueueEmptyError()

        index = random.randint(0, self.__size - 1)
        item = self.__list[index]
        self.__list[index] = self.__list[self.__size - 1]
        self.__list.pop()
        self.__size -= 1
        return item

    def sample(self: 'RandomizedQueue') -> Any:
        """
        Returns a random item from the randomized queue without removing it.

        Returns:
            A randomly sampled item.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise self.QueueEmptyError()

        index = random.randint(0, self.__size - 1)
        return self.__list[index]

    @classmethod
    def from_list(cls: 'RandomizedQueue', elements: List[Any]) -> 'RandomizedQueue':
        """
        Alternative constructor, creates a Randomized Queue instance from a list.

        Args:
            elements (List[Any]): List of elements to create a randomized queue.

        Returns:
            random_queue (RandomizedQueue): Returns the created instance of RandomizedQueue.
        """
        random_queue = cls()
        random_queue.__list = deepcopy(elements)
        random.shuffle(random_queue.__list)
        random_queue.__size = len(elements)
        return random_queue

    def __repr__(self: 'RandomizedQueue') -> str:
        """
        Returns a string representation of the queue.

        Returns:
            str: The string representation of the queue.
        """
        return f"{self.__class__.__name__}.from_list({self.__list})"

    def __str__(self: 'RandomizedQueue') -> str:
        """
        Returns a string representation of the queue.

        Returns:
            str: The string representation of the queue.
        """
        return f"{self.__list}"

    def __iter__(self: 'RandomizedQueue') -> Generator[Any, None, None]:
        """
        Returns an iterator over a shuffled copy of the elements in the randomized queue.
        The original queue remains unchanged.

        Returns:
            An iterator.
        """
        copy = deepcopy(self.__list)
        random.shuffle(copy)
        for item in copy:
            yield item