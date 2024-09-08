class Queue:
    """
    A queue implementation using a singly linked list.

    Methods:
        isEmpty(): Checks if the queue is empty.
        enqueue(val): Adds a value to the end of the queue.
        dequeue(): Removes and returns the value from the front of the queue.
        __str__(): Returns a string representation of the queue.
    """

    def __init__(self):
        """
        Initialize an empty queue.
        """
        self.first = None
        self.last = None

    class Node:
        """
        A node in the linked list.

        Attributes:
            val: The value of the node (can be of any type).
            next (Node): The next node in the linked list.
        """

        def __init__(self, val = 0, next = None):
            self.val = val
            self.next = next

    def isEmpty(self):
        """
        Check if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return self.first is None

    def enqueue(self, val):
        """
        Add a value to the end of the queue.

        Args:
            val: The value to be added to the queue (can be of any type).
        """
        oldlast = self.last
        self.last = Queue.Node(val)
        
        if oldlast is None:
            self.first = self.last
        else:
            oldlast.next = self.last

    def dequeue(self):
        """
        Remove and return the value from the front of the queue.

        Returns:
            The value removed from the front of the queue.
            None: If the queue is empty.
        """
        if not self.isEmpty():
            val = self.first.val
            self.first = self.first.next

            if self.isEmpty():
                self.last = None

            return val

        else:
            print('The list is empty')

    def __str__(self):
        """
        Return a string representation of the queue.

        Returns:
            str: The string representation of the queue.
        """
        curr = self.first
        sequence = []
        while curr:
            sequence.append(str(curr.val))
            curr = curr.next
        return ' -> '.join(sequence)


# Example usage
if __name__ == "__main__":
    queue = Queue()
    
    # Enqueue various types of elements
    queue.enqueue(5)
    queue.enqueue("hello")
    queue.enqueue([1, 2, 3])
    queue.enqueue(3.14)
    queue.enqueue(True)
    
    # Print the queue
    print("Queue after enqueues:", queue)
    
    # Dequeue elements from the queue
    print("Dequeued:", queue.dequeue())
    print("Dequeued:", queue.dequeue())
    
    # Print the queue after dequeues
    print("Queue after dequeues:", queue)
    
    # Check if the queue is empty
    print("Is queue empty?", queue.isEmpty())
    
    # Dequeue remaining elements
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    
    # Try to dequeue from an empty queue
    print("Dequeued from empty queue:", queue.dequeue())
    
    # Check if the queue is empty again
    print("Is queue empty?", queue.isEmpty())