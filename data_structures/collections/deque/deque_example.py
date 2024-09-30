from data_structures import Deque


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
    print("Size deque =", len(deque))
    
    # Iterate over the elements of the deque
    for i, item in enumerate(deque):
        print(f"Item {i}:", item)
    
    # Remove items from the deque
    print("Removed from front:", deque.remove_first())
    print("Removed from back:", deque.remove_last())
    
    # Print the deque after removals
    print("Deque after removals:", deque)
    
    # Check if the deque is empty
    print("Does the deque have more elements?", bool(deque))

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
    print("Does the deque have more elements?", bool(deque))

    # Create a deque using the alternative constructor
    deque2 = Deque.from_list(['True', '[1, 2, 3]', '5', 'hello', '100'])
    print("Create a deque using alternative constructor:", deque2)

    # Check contains method
    item = 100
    print(f"Is the item {item} in the deque: {deque2}?", item in deque2)
    
    item = 101
    print(f"Is the item {item} in the deque: {deque2}?", item in deque2)

    # Check get item method using index
    index = 0
    print(f"Get the item in the index [{index}]:", deque2[index])
    index = -1
    print(f"Get the item in the index [{index}]:", deque2[index])

    # Check get item method using slice
    s = slice(0, 3, 1)
    print(f"Get the items in the [{s}]:", deque2[s])

    # Check reversed
    print("Reversed deque:", list(reversed(deque2)))



if __name__ == "__main__":
    demo()