class Heapsort:
    """
    A class to perform heapsort on an array.

    Methods:
        __init__(a): Initializes the heapsort process and sorts the array.
        sink(a, k, n): Restores the heap order property by sinking down.
    """

    def __init__(self, a):
        """
        Initializes the heapsort process and sorts the array.

        Args:
            a (list): The list of elements to be sorted.
        """
        n = len(a) - 1

        # Build the heap in array a so that largest value is at the root
        for k in range(n // 2, 0, -1):
            self.sink(a, k, n)

        # Extract elements from the heap one by one
        while n > 1:
            # Move current root to end
            a[1], a[n] = a[n], a[1]
            n -= 1
            # Call sink on the reduced heap
            self.sink(a, 1, n)
            
    def sink(self, a, k, n):
        """
        Restores the heap order property by sinking down the element at index k.

        Args:
            a (list): The list of elements.
            k (int): The index of the element to sink down.
            n (int): The size of the heap.
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


# Example usage
if __name__ == "__main__":
    a = [None, 10, 9, 6, 20, 7, 8, 13, 15, 11, 19, 12, 1, 18, 4, 17, 2, 14, 16, 3, 5]
    print(a[1:])
    print("\nSorted Array in Ascending Order:")
    Heapsort(a)
    print(a[1:])