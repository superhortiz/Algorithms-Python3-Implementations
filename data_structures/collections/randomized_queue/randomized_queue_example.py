from .randomized_queue import RandomizedQueue

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
    print("Size of the queue =", random_queue.size)
    print("randomized queue after additions:", random_queue)
    print("randomized queue after additions:", repr(random_queue))

    # Iterate over the elements of the randomized queue
    for i, item in enumerate(random_queue):
        print(f"Item {i}: {item}")

    # Check methods
    print(f"random_queue is empty? {random_queue.is_empty()}")
    print(f"Size = {random_queue.size}")
    print(f"Show a random element: {random_queue.sample()}")
    print(f"Remove a random element: {random_queue.dequeue()}")
    print(f"Size = {random_queue.size}")
    print(f"Remove a random element: {random_queue.dequeue()}")
    print(f"Size = {random_queue.size}")

    # Use the alternative constructor
    random_queue2 = RandomizedQueue.from_list([5, 4, 3, 2, 1])
    print("Using alternative constructor:", random_queue2)
    print("Size =", random_queue2.size)

    # Try to change immutable attribute
    try:
        random_queue2.size = 2
    except Exception as e:
        print(e)


if __name__ == "__main__":
    demo()