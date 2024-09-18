from data_structures.stack import Stack

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
    print("Size of the stack =", stack.size)

    # Iterate over elements
    for i, item in enumerate(stack):
        print(f"Item {i}:", item)
    
    # Pop elements from the stack
    print("Popped:", stack.pop())
    print("Popped:", stack.pop())
    
    # Print the stack after pops
    print("Stack after pops:", stack)
    
    # Check if the stack is empty
    print("Is stack empty?", stack.is_empty())  # Output: False
    
    # Pop remaining elements
    stack.pop()
    stack.pop()
    stack.pop()
    
    # Try to pop from an empty stack
    try:
        print("Popped from empty stack:", stack.pop())
    except Exception as e:
        print("Error:", e)
    
    # Check if the stack is empty again
    print("Is stack empty?", stack.is_empty())  # Output: True

    # Try to modifiy immutable attribute size
    try:
        stack.size = 5

    except AttributeError as e:
        print("Error:", e)
        print("Size of the stack =", stack.size)

    # Construct a stack using the alternative constructor
    stack2 = Stack.from_list([True, 3.14, [1, 2, 3], 'hello', 5])
    print("Using the alternative constructor:", stack2)


if __name__ == "__main__":
    demo()