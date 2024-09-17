class BinaryHeap:
    """
    A binary heap implementation (max-heap) using an array.

    Methods:
        swim(k): Restores the heap order property by swimming up.
        insert(newValue): Inserts a new value into the heap.
        sink(k): Restores the heap order property by sinking down.
        del_max(): Removes and returns the maximum value from the heap.
        __str__(): Returns a string representation of the heap.
    """
    def __init__(self):
        """
        Initializes an empty binary heap.

        Args:
            a (list): The initial array to store heap elements. Defaults to [None].
        """
        self.a = [None]
        self.n = 0

    def swim(self, k):
        """
        Restores the heap order property by swimming up the element at index k.

        Args:
            k (int): The index of the element to swim up.
        """
        while k > 1 and self.a[k // 2] < self.a[k]:
            self.a[k // 2], self.a[k] = self.a[k], self.a[k // 2]
            k = k // 2

    def insert(self, newValue):
        """
        Inserts a new value into the heap.

        Args:
            newValue: The value to be inserted into the heap.
        """
        self.a.append(newValue)
        self.n += 1
        self.swim(self.n)

    def sink(self, k):
        """
        Restores the heap order property by sinking down the element at index k.

        Args:
            k (int): The index of the element to sink down.
        """
        while 2 * k <= self.n:
            j = 2 * k
            if j < self.n and self.a[j] < self.a[j + 1]:
                j += 1
            if self.a[k] > self.a[j]:
                break
            self.a[k], self.a[j] = self.a[j], self.a[k]
            k = j

    def del_max(self):
        """
        Removes and returns the maximum value from the heap.

        Returns:
            The maximum value from the heap.
        """
        self.a[1], self.a[-1] = self.a[-1], self.a[1]
        val = self.a.pop()
        self.n -= 1
        self.sink(1)
        return val

    def __str__(self):
        """
        Returns a string representation of the heap.

        Returns:
            str: The string representation of the heap.
        """
        printable = [str(self.a[i]) for i in range(1, self.n + 1)]
        return ', '.join(printable)

def main():
    """
    Example usage
    """
    heap = BinaryHeap()
    
    # Insert elements into the heap
    heap.insert(10)
    heap.insert(20)
    heap.insert(5)
    heap.insert(30)
    heap.insert(15)
    
    # Print the heap
    print("Heap after inserts:", heap)  # Output: 30, 15, 5, 10, 20
    
    # Delete the maximum element
    print("Deleted max element:", heap.del_max())  # Output: 30
    
    # Print the heap after deletion
    print("Heap after deleting max:", heap)  # Output: 20, 15, 5, 10


if __name__ == "__main__":
    main()
