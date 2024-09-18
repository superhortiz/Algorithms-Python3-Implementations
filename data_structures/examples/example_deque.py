from data_structures.deque import Deque

def demo() -> None:
    """
    Example usage of Deque data structure
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
    print("Deque after additions:", repr(deque))
    
    # Iterate over the elements of the deque
    for i, item in enumerate(deque):
        print(f"Item {i}:", item)
    
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
    except Exception as e:
        print(e)  # Output: remove_first from empty deque
    
    # Check if the deque is empty again
    print("Is deque empty?", deque.is_empty())

    try:
        deque.size = 4
    except AttributeError as e:
        print(e)

    # Create a deque using the alternative constructor
    deque2 = Deque.from_list(['True', '[1, 2, 3]', '5', 'hello', '100'])
    print("Create a deque using alternative constructor:", deque2)


if __name__ == "__main__":
    demo()