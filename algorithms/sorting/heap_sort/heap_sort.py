class Heapsort:
    """
    A binary heap implementation (max-heap) using an array.
    This class performs heapsort on an array.

    Performance:
        Time complexity: O(N log N)
        Space complexity: O(1)

    Note:
        This class modifies the original list.
    """

    def __init__(self: 'Heapsort', a: list) -> None:
        """
        Initializes the heapsort process and sorts the array.

        Args:
            a (list): The list of elements to be sorted.

        Raises:
            ValueError: If the argument is not a list.
        """

        if not isinstance(a, list):
            raise ValueError("ValueError: Input must be a list.")

        n = len(a)

        # Insert a dummy value None at index 0
        a.insert(0, None)

        # Build the heap in array a so that largest value is at the root
        for k in range(n // 2, 0, -1):
            self._sink(a, k, n)

        # Extract elements from the heap one by one
        while n > 1:
            # Move current root to end
            a[1], a[n] = a[n], a[1]
            n -= 1
            # Call sink on the reduced heap
            self._sink(a, 1, n)

        # Remove the placeholder None
        a.pop(0)
            
    @staticmethod
    def _sink(a: list, k: int, n: int) -> None:
        """
        Restores the heap order property by sinking down the element at index k.

        Args:
            k (int): The index of the element to sink down.
        """
        while 2 * k <= n:
            j = 2 * k

            # Find the larger child
            if j < n and a[j] < a[j + 1]:
                j += 1

            # If the parent is larger than the largest child, stop sinking
            if a[k] > a[j]:
                break

            # Swap the parent with the largest child
            a[k], a[j] = a[j], a[k]
            k = j
