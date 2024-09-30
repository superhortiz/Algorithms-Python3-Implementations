from data_structures import Stack


def demo():
    """
    Example usage of Stack data structure
    """
    stack = Stack()
    
    # Push various types of elements onto the stack
    stack.push(5)
    stack.push("hello")
    stack.push([1, 2, 3])
    stack.push(3.14)
    stack.push(True)
    
    # Print the stack
    print("Stack after pushes:", stack)
    print("Stack after pushes:", repr(stack))
    print("Size of the stack =", len(stack))

    # Iterate over elements
    for i, item in enumerate(stack):
        print(f"Item {i}:", item)
    
    # Pop elements from the stack
    print("Popped:", stack.pop())
    print("Popped:", stack.pop())
    
    # Print the stack after pops
    print("Stack after pops:", stack)
    
    # Check if the stack is empty
    print("Does the stack have elements?", bool(stack))  # Output: True
    
    # Pop remaining elements
    stack.pop()
    stack.pop()
    stack.pop()
    
    # Try to pop from an empty stack
    try:
        print("Popped from empty stack:", stack.pop())

    except Exception as e:
        print("Try to remove elements from an empty stack:", e)

    # Check if the stack is empty again
    print("Does the stack have elements?", bool(stack))  # Output: False

    # Construct a stack using the alternative constructor
    stack2 = Stack.from_list([True, 3.14, [1, 2, 3], 'hello', 5])
    print("Using the alternative constructor:", stack2)

    # Check contains method
    item = 3.14
    print(f"Is the item {item} in the stack: {stack2}?", item in stack2)
    
    item = 3.1
    print(f"Is the item {item} in the stack: {stack2}?", item in stack2)

    # Check get item method using index
    index = 0
    print(f"Get the item in the index [{index}]:", stack2[index])
    index = -1
    print(f"Get the item in the index [{index}]:", stack2[index])

    # Check get item method using slice
    s = slice(0, 3, 1)
    print(f"Get the items in the [{s}]:", stack2[s])

    # Check reversed
    print("Reversed stack:", list(reversed(stack2)))


if __name__ == "__main__":
    demo()