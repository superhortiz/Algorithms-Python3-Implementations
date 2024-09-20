from typing import Any

class BinaryHeap:
    """
    A binary heap implementation (max-heap) using an array.

    Methods:
        del_max(): Removes and returns the maximum value from the heap.
        insert(newValue): Inserts a new value into the heap.
        peek_max(): Returns the maximum value from the heap.

    Special Methods:
        __str__(): Returns a string representation of the heap.
    """
    def __init__(self: 'BinaryHeap') -> None:
        """
        Initializes an empty binary heap.
        """
        self.__array = [None]
        self.__n = 0

    def __swim(self: 'BinaryHeap', k: int) -> None:
        """
        Restores the heap order property by swimming up the element at index k.

        Args:
            k (int): The index of the element to swim up.
        """
        while k > 1 and self.__array[k // 2] < self.__array[k]:
            self.__array[k // 2], self.__array[k] = self.__array[k], self.__array[k // 2]
            k = k // 2

    def __sink(self: 'BinaryHeap', k: int) -> None:
        """
        Restores the heap order property by sinking down the element at index k.

        Args:
            k (int): The index of the element to sink down.
        """
        while 2 * k <= self.__n:
            j = 2 * k

            # Find the larger child
            if j < self.__n and self.__array[j] < self.__array[j + 1]:
                j += 1

            # If the parent is larger than the largest child, stop sinking
            if self.__array[k] > self.__array[j]:
                break

            # Swap the parent with the largest child
            self.__array[k], self.__array[j] = self.__array[j], self.__array[k]
            k = j

    def insert(self: 'BinaryHeap', newValue: Any) -> None:
        """
        Inserts a new value into the heap.

        Args:
            newValue (Any): The value to be inserted into the heap.

        Raises:
            ValueError: If the val is None.
        """
        if newValue is None:
            raise ValueError("ValueError: Invalid value.")

        self.__array.append(newValue)
        self.__n += 1
        self.__swim(self.__n)

    def del_max(self: 'BinaryHeap') -> Any:
        """
        Removes and returns the maximum value from the heap.

        Returns:
            val(Any): The maximum value from the heap.

        Raises:
            IndexError: If the heap is empty.
        """
        if self.__n == 0:
            raise IndexError("IndexError: The heap is empty.")

        self.__array[1], self.__array[-1] = self.__array[-1], self.__array[1]
        val = self.__array.pop()
        self.__n -= 1
        self.__sink(1)
        return val

    def peek_max(self: 'BinaryHeap') -> Any:
        """
        Returns the maximum value from the heap.

        Returns:
            val(Any): The maximum value from the heap.

        Raises:
            IndexError: If the heap is empty.
        """
        if self.__n == 0:
            raise IndexError("IndexError: The heap is empty.")

        return self.__array[1]

    def __str__(self: 'BinaryHeap') -> str:
        """
        Returns a string representation of the heap.

        Returns:
            str: The string representation of the heap.
        """
        return f"{self.__array[1::]}"
