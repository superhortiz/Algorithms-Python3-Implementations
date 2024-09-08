class LinkedStack:
    """
    A stack implementation using a singly linked list.

    Methods:
        isEmpty(): Checks if the stack is empty.
        push(val): Pushes a value onto the stack.
        pop(): Pops a value from the stack.
        __str__(): Returns a string representation of the stack.
    """

    def __init__(self):
        """
        Initialize an empty stack.
        """
        self.first = None

    class Node:
        """
        A node in the linked list.

        Attributes:
            val: The value of the node.
            next (Node): The next node in the linked list.
        """
        def __init__(self, val = 0, next = None):
            self.val = val
            self.next = next

    def isEmpty(self):
        """
        Check if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return self.first is None

    def push(self, val):
        """
        Push a value onto the stack.

        Args:
            val: The value to be pushed onto the stack.
        """
        new_node = LinkedStack.Node(val, next = self.first)
        self.first = new_node

    def pop(self):
        """
        Pop a value from the stack.

        Returns:
            val: The value popped from the stack.
            None: If the stack is empty.
        """
        if not self.isEmpty():
            val = self.first.val
            self.first = self.first.next
            return val
        else:
            print('The list is empty')

    def __str__(self):
        """
        Return a string representation of the stack.

        Returns:
            str: The string representation of the stack.
        """
        curr = self.first
        sequence = []
        while curr:
            sequence.append(str(curr.val))
            curr = curr.next
        return ' -> '.join(sequence)


# Example usage
if __name__ == "__main__":
    stack = LinkedStack()
    
    # Push various types of elements onto the stack
    stack.push(5)
    stack.push("hello")
    stack.push([1, 2, 3])
    stack.push(3.14)
    stack.push(True)
    
    # Print the stack
    print("Stack after pushes:", stack)
    
    # Pop elements from the stack
    print("Popped:", stack.pop())
    print("Popped:", stack.pop())
    
    # Print the stack after pops
    print("Stack after pops:", stack)
    
    # Check if the stack is empty
    print("Is stack empty?", stack.isEmpty())  # Output: False
    
    # Pop remaining elements
    stack.pop()
    stack.pop()
    stack.pop()
    
    # Try to pop from an empty stack
    print("Popped from empty stack:", stack.pop())  # Output: The list is empty
    
    # Check if the stack is empty again
    print("Is stack empty?", stack.isEmpty())  # Output: True