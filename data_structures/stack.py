from typing import Any, Generator, List, Optional

class Stack:
    """
    A stack implementation using a singly linked list.

    Attributes:
        size (int): number of items in the stack.

    Methods:
        is_empty(): Checks if the stack is empty.
        push(val): Pushes a value onto the stack.
        pop(): Pops a value from the stack.
        from_list(elements): Alternative constructor, creates a Stack instance from a list.

    Special Methods:
        __repr__(): Returns a string representation of the stack.
        __str__(): Return a string representation of the stack.
        __iter__(): Generator function to iterate over the stack elements.
    """

    class Node:
        """
        Represents a node in the linked list.
        
        Args:
            val (Any): The value stored in the node.
            next (Optional[Node]): Reference to the next node.

        Attributes:
            val (Any): The value stored in the node.
            next (Optional[Node]): Reference to the next node.
        """
        def __init__(self: 'Node', val: Any, next: 'Node' = None) -> None:
            self.val: Any = val
            self.next: 'Node' = next

    class StackEmptyError(Exception):
        """
        Custom exception to be raised when attempting to access an element
        from an empty stack.

        Attributes:
            message (str): Custom message for empty stack.
        """
        def __init__(self: 'StackEmptyError', message: str = "StackEmptyError: The stack is empty.") -> None:
            """
            Initialize the exception.
            """
            self.message: str = message
        
        def __str__(self: 'StackEmptyError') -> str:
            """
            Returns the exception message.
            """
            return self.message

    def __init__(self: 'Stack') -> None:
        """
        Initialize an empty stack.
        """
        self.__first: Node = None
        self.__size: int = 0

    @property
    def size(self: 'Stack') -> int:
        """
        Returns the number of items in the stack.

        This attribute is read-only and cannot be modified directly.

        Returns:
            int: The number of items in the stack.
        """
        return self.__size

    @size.setter
    def size(self: 'Stack', *args, **kwargs) -> None:
        """
        Raises AttributeError to prevent modification.

        The size attribute is updated internally by add and remove operations.
        Attempting to set it directly will raise an AttributeError.

        Raises:
            AttributeError: Always raised to prevent modification.
        """
        raise AttributeError("This attribute is immutable")

    def is_empty(self: 'Stack') -> bool:
        """
        Check if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return self.__first is None

    def push(self: 'Stack', val: Any) -> None:
        """
        Push a value onto the stack.

        Args:
            val (Any): The value to be pushed onto the stack.

        Raises:
            ValueError: If the val is None.
        """
        if val is None:
            raise ValueError
            
        new_node = self.Node(val, next = self.__first)
        self.__first = new_node
        self.__size += 1

    def pop(self: 'Stack') -> Any:
        """
        Pop a value from the stack.

        Returns:
            val (Any): The value popped from the stack.

        Raises:
            StackEmptyError: If the stack is empty.
        """
        if self.is_empty():
            raise self.StackEmptyError()

        val = self.__first.val
        self.__first = self.__first.next
        self.__size -= 1
        return val

    @classmethod
    def from_list(cls: 'Stack', elements: List[Any]) -> 'Stack':
        """
        Alternative constructor, creates a Stack instance from a list.

        Args:
            elements (List[Any]): List of elements to create a stack.

        Returns:
            stack (Stack): Returns the created instance of Stack.
        """
        stack = cls()
        for element in reversed(elements):
            stack.push(element)
        return stack

    def __repr__(self: 'Stack') -> str:
        """
        Returns a string representation of the stack.

        Returns:
            str: The string representation of the stack.
        """
        sequence = [item for item in self]
        return f"{self.__class__.__name__}.from_list({sequence})"

    def __str__(self: 'Stack') -> str:
        """
        Return a string representation of the stack.

        Returns:
            str: The string representation of the stack.
        """
        curr = self.__first
        sequence = []
        while curr:
            sequence.append(str(curr.val))
            curr = curr.next
        return ' -> '.join(sequence)

    def __iter__(self) -> Generator[Any, None, None]:
        """
        Generator function to iterate over the stack elements.
        
        Yields:
            Any: Value of the current node.
        """
        current = self.__first
        while current:
            yield current.val
            current = current.next