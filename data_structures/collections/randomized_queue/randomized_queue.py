import random
from typing import Any, Generator, List
from copy import deepcopy


class RandomizedQueue:
    """
    A randomized queue implementation using a Python list for efficient operations.
    The 'RandomizedQueue' class ensures that each iterator returns the items in uniformly random order.

    Methods:
        dequeue(): Removes and returns a random item from the randomized queue.
        enqueue(val): Adds an item to the randomized queue.
        from_list(elements): Alternative constructor, creates a Randomized Queue instance from a list.
        sample(): Returns a random item from the randomized queue without removing it.

    Special Methods:
        __bool__(): Checks if the randomized queue is empty.
        __iter__(): Returns an iterator over a shuffled copy of the elements in the randomized queue.
        __len__(): Returns the number of items in the randomized queue.
        __repr__(): Returns a string representation of the queue.
        __str__(): Returns a string representation of the queue.
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
        self._list: List[Any] = [] # Internal list to store elements

    def dequeue(self: 'RandomizedQueue') -> Any:
        """
        Removes and returns a random item from the randomized queue.

        Returns:
            The dequeued item.

        Raises:
            IndexError: If the queue is empty.
        """
        if not self.__bool__():
            raise self.QueueEmptyError()

        index = random.randint(0, len(self._list) - 1)
        item = self._list[index]
        self._list[index] = self._list[len(self._list) - 1]
        self._list.pop()
        return item

    def enqueue(self: 'RandomizedQueue', item: Any) -> None:
        """
        Adds an item to the randomized queue.

        Args:
            item: The item to enqueue.

        Raises:
            ValueError: If the item is None.
        """
        if item is None:
            raise ValueError("Cannot push None value onto the queue.")

        self._list.append(item)

    def sample(self: 'RandomizedQueue') -> Any:
        """
        Returns a random item from the randomized queue without removing it.

        Returns:
            A randomly sampled item.

        Raises:
            IndexError: If the queue is empty.
        """
        if not self.__bool__():
            raise self.QueueEmptyError()

        index = random.randint(0, len(self._list) - 1)
        return self._list[index]

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
        random_queue._list = deepcopy(elements)
        random.shuffle(random_queue._list)
        return random_queue

    def __bool__(self: 'RandomizedQueue') -> bool:
        """
        Checks if the randomized queue is empty.

        Returns:
            False if empty, True otherwise.
        """
        return bool(self._list)

    def __iter__(self: 'RandomizedQueue') -> Generator[Any, None, None]:
        """
        Returns an iterator over a shuffled copy of the elements in the randomized queue.
        The original queue remains unchanged.

        Returns:
            An iterator.
        """
        copy = deepcopy(self._list)
        random.shuffle(copy)
        for item in copy:
            yield item

    def __len__(self: 'RandomizedQueue') -> int:
        """
        Returns the number of items in the randomized queue.

        Returns:
            int: The number of items in the randomized queue.
        """
        return len(self._list)

    def __repr__(self: 'RandomizedQueue') -> str:
        """
        Returns a string representation of the queue.

        Returns:
            str: The string representation of the queue.
        """
        return f"{type(self).__name__}.from_list({self._list})"

    def __str__(self: 'RandomizedQueue') -> str:
        """
        Returns a string representation of the queue.

        Returns:
            str: The string representation of the queue.
        """
        return f"{self._list}"