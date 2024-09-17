from typing import Optional, Any

class Deque:
    """
    A double-ended queue (deque) implementation using a doubly linked list.

    Methods:
        is_empty(): Checks if the deque is empty.
        size(): Returns the number of items in the deque.
        add_first(val): Adds a value to the front of the deque.
        add_last(val): Adds a value to the back of the deque.
        remove_first(): Removes and returns the value from the front of the deque.
        remove_last(): Removes and returns the value from the back of the deque.
        iterator(): Returns an iterator for the deque.
        __str__(): Returns a string representation of the deque.
        reversed(): Returns a string representation of the deque in reversed order.
    """
    def __init__(self) -> None:
        """
        Initializes an empty deque.
        """
        self.first = None
        self.last = None
        self.size = 0

    class Node:
        def __init__(self, val: Any, next: Optional['Node'] = None, prev: Optional['Node'] = None) -> None:
            """
            Represents a node in the doubly linked list.

            Args:
                val (Any): The value stored in the node.
                next (Optional[Node]): Reference to the next node.
                prev (Optional[Node]): Reference to the previous node.
            """
            self.val = val
            self.next = next
            self.prev = prev

    def is_empty(self) -> bool:
        """
        Checks if the deque is empty.

        Returns:
            bool: True if the deque is empty, False otherwise.
        """
        return self.first is None

    def size(self) -> int:
        """
        Returns the number of items in the deque.

        Returns:
            int: The number of items.
        """
        return self.size

    def add_first(self, val: Any) -> None:
        """
        Adds an item to the front of the deque.

        Args:
            val (Any): The item to be added.

        Raises:
            ValueError: If the input item is None.
        """
        self.size += 1
        if self.is_empty():
            self.first = self.last = self.Node(val)
        else:
            new_node = self.Node(val, next = self.first)
            self.first.prev = new_node
            self.first = new_node

    def add_last(self, val: Any) -> None:
        """
        Adds an item to the back of the deque.

        Args:
            val (Any): The item to be added.

        Raises:
            ValueError: If the input item is None.
        """
        self.size += 1
        if self.is_empty():
            self.first = self.last = self.Node(val)
        else:
            new_node = self.Node(val, prev = self.last)
            self.last.next = new_node
            self.last = new_node

    def remove_first(self) -> Any:
        """
        Removes and returns the item from the front of the deque.

        Returns:
            Any: The removed item.

        Raises:
            IndexError: If the deque is empty.
        """
        if self.is_empty():
            print('The list is empty')
        else:
            self.size -= 1
            item = self.first.val
            self.first = self.first.next
            if self.first is None:
                self.last = None
            else:
                self.first.prev = None
            return item

    def remove_last(self) -> Any:
        """
        Removes and returns the item from the back of the deque.

        Returns:
            Any: The removed item.

        Raises:
            IndexError: If the deque is empty.
        """
        if self.is_empty():
            print('The list is empty')
        else:
            self.size -= 1
            item = self.last.val
            self.last = self.last.prev
            if self.last is None:
                self.first = None
            else:
                self.last.next = None
            return item

    def __str__(self) -> str:
        """
        Returns a string representation of the deque.

        Returns:
            str: A string showing the items in the deque.
        """
        curr = self.first
        sequence = []
        while curr:
            sequence.append(str(curr.val))
            curr = curr.next
        return ' <-> '.join(sequence)

    def reversed(self) -> str:
        """
        Returns a string representation of the deque in reverse order.

        Returns:
            str: A string showing the items in reverse order.
        """
        curr = self.last
        sequence = []
        while curr:
            sequence.append(str(curr.val))
            curr = curr.prev
        return ' <-> '.join(sequence)

    def __iter__(self) -> 'Deque':
        """
        Initializes the iterator by setting the current node to the first node.

        Returns:
            Deque: The iterator object itself.
        """
        self.curr = self.first
        return self

    def __next__(self) -> Any:
        """
        Returns the next item in the deque during iteration.

        Returns:
            Any: The value of the current node.

        Raises:
            StopIteration: If the end of the deque is reached.
        """
        if self.curr is None:
            raise StopIteration
        item = self.curr.val
        self.curr = self.curr.next
        return item

def main():
    """
    Example usage
    """
    deque = Deque()
    
    # Add items to the deque
    deque.add_first(5)
    deque.add_last("hello")
    deque.add_first([1, 2, 3])
    deque.add_last(100)
    deque.add_first(True)
    
    # Print the deque
    print("Deque after additions:", deque)
    
    # Print the deque in reversed order
    print("Deque in reversed order:", deque.reversed())

    # Iterate over the elements of the deque
    for item in deque:
        print("Item:", item)
    
    # Remove items from the deque
    print("Removed from front:", deque.remove_first())
    print("Removed from back:", deque.remove_last())
    
    # Print the deque after removals
    print("Deque after removals:", deque)
    
    # Check if the deque is empty
    print("Is deque empty?", deque.is_empty())
    
    # Remove remaining items
    deque.remove_first()
    deque.remove_last()
    deque.remove_first()
    
    # Try to remove from an empty deque
    try:
        print("Removed from empty deque:", deque.remove_first())
    except IndexError as e:
        print(e)  # Output: remove_first from empty deque
    
    # Check if the deque is empty again
    print("Is deque empty?", deque.is_empty())


if __name__ == "__main__":
    main()
