from data_structures import RandomizedQueue


def demo():
    """
    Example usage of RandomizedQueue data structure
    """
    random_queue = RandomizedQueue()

    # Try to remove en element from an empty list
    try:
        random_queue.dequeue()
    except Exception as e:
        print(e)
        
    # Enqueue elements
    random_queue.enqueue(5)
    random_queue.enqueue(4)
    random_queue.enqueue(3)
    random_queue.enqueue(2)
    random_queue.enqueue(1)
    print("Size of the queue =", len(random_queue))
    print("randomized queue after additions:", random_queue)
    print("randomized queue after additions:", repr(random_queue))

    # Iterate over the elements of the randomized queue
    for i, item in enumerate(random_queue):
        print(f"Item {i}: {item}")

    # Check methods
    print("Does the queue have elements?", bool(random_queue))
    print("Size =", len(random_queue))
    print("Show a random element:", random_queue.sample())
    print("Remove a random element:", random_queue.dequeue())
    print("Size =", len(random_queue))
    print("Remove a random element:", random_queue.dequeue())
    print("Size =", len(random_queue))

    # Use the alternative constructor
    random_queue2 = RandomizedQueue.from_list([5, 4, 3, 2, 1])
    print("Using alternative constructor:", random_queue2)
    print("Size =", len(random_queue))


if __name__ == "__main__":
    demo()