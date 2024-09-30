from typing import Any, Iterator, List, Union


class BinaryHeap:
    """
    A binary heap implementation (max-heap) using an array.

    Methods:
        del_max(): Removes and returns the maximum value from the heap.
        insert(new_value): Inserts a new value into the heap.
        peek_max(): Returns the maximum value from the heap.

    Special Methods:
        __getitem__(index): Allows indexing, supports both integer indices and slice objects.
        __iter__(): Returns an iterator over the heap's elements.
        __len__(): Returns the number of items in the heap.
        __repr__(): Returns a string representation of the heap.
        __reversed__(): Returns a reversed iterator over the heap's elements.
    """

    class HeapEmptyError(Exception):
        """
        Custom exception to be raised when attempting to access an element from an empty heap.
        """
        def __init__(self: 'HeapEmptyError', message: str = "The heap is empty.") -> None:
            self.message = message
            super().__init__(self.message)

    def __init__(self: 'BinaryHeap') -> None:
        """
        Initializes an empty binary heap.
        """
        self._list: list = [None]
        self._n: int = 0

    def _swim(self: 'BinaryHeap', k: int) -> None:
        """
        Restores the heap order property by swimming up the element at index k.

        Args:
            k (int): The index of the element to swim up.
        """
        while k > 1 and self._list[k // 2] < self._list[k]:
            self._list[k // 2], self._list[k] = self._list[k], self._list[k // 2]
            k = k // 2

    def _sink(self: 'BinaryHeap', k: int) -> None:
        """
        Restores the heap order property by sinking down the element at index k.

        Args:
            k (int): The index of the element to sink down.
        """
        while 2 * k <= self._n:
            j = 2 * k

            # Find the larger child
            if j < self._n and self._list[j] < self._list[j + 1]:
                j += 1

            # If the parent is larger than the largest child, stop sinking
            if self._list[k] > self._list[j]:
                break

            # Swap the parent with the largest child
            self._list[k], self._list[j] = self._list[j], self._list[k]
            k = j

    def insert(self: 'BinaryHeap', new_value: Any) -> None:
        """
        Inserts a new value into the heap.

        Args:
            new_value (Any): The value to be inserted into the heap.

        Raises:
            ValueError: If the val is None.
        """
        if new_value is None:
            raise ValueError("ValueError: Invalid value.")

        self._list.append(new_value)
        self._n += 1
        self._swim(self._n)

    def del_max(self: 'BinaryHeap') -> Any:
        """
        Removes and returns the maximum value from the heap.

        Returns:
            val(Any): The maximum value from the heap.

        Raises:
            IndexError: If the heap is empty.
        """
        if self._n == 0:
            raise self.HeapEmptyError()

        self._list[1], self._list[-1] = self._list[-1], self._list[1]
        val = self._list.pop()
        self._n -= 1
        self._sink(1)
        return val

    def peek_max(self: 'BinaryHeap') -> Any:
        """
        Returns the maximum value from the heap.

        Returns:
            val(Any): The maximum value from the heap.

        Raises:
            IndexError: If the heap is empty.
        """
        if self._n == 0:
            raise self.HeapEmptyError()

        return self._list[1]

    def __getitem__(self: 'BinaryHeap', index: Union[int, slice]) -> Union[Any, List[Any]]:
        """
        Allows indexing, supports both integer indices and slice objects.

        Args:
            index (Union[int, slice]): The index or slice to retrieve items from the heap.

        Returns:
            Union[Any, List[Any]]: The item at the specified index or a list of items for the specified slice.
        """
        return self._list[1:][index]

    def __iter__(self: 'BinaryHeap') -> Iterator[Any]:
        """
        Returns an iterator over the heap's elements.

        Returns:
            Iterator[Any]: Iterator over the heap's elements.
        """
        return iter(self._list[1::])

    def __len__(self: 'BinaryHeap') -> int:
        """
        Returns the number of items in the heap.

        Returns:
            int: The number of items in the heap.
        """
        return self._n

    def __repr__(self: 'BinaryHeap') -> str:
        """
        Returns a string representation of the heap.

        Returns:
            str: The string representation of the heap.
        """
        return f"{self._list[1::]}"

    def __reversed__(self: 'BinaryHeap') -> Iterator[Any]:
        """
        Returns a reversed iterator over the heap's elements.

        Returns:
            Iterator[Any]: Reversed iterator over the heap's elements.
        """
        return reversed(self._list[1::])