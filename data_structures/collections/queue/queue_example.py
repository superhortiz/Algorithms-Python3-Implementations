from data_structures import Queue


def demo():
    """
    Example usage of Queue data structure
    """
    queue = Queue()
    
    # Enqueue various types of elements
    queue.enqueue(5)
    queue.enqueue("hello")
    queue.enqueue([1, 2, 3])
    queue.enqueue(3.14)
    queue.enqueue(True)
    
    # Print the queue
    print("Queue after enqueues:", queue)
    print("Queue after enqueues:", repr(queue))

    # Iterate over the queue
    for i, item in enumerate(queue):
        print(f"Item {i}:", item)

    # Print size
    print("Size =", len(queue))
    
    # Dequeue elements from the queue
    print("Dequeued:", queue.dequeue())
    print("Dequeued:", queue.dequeue())
    
    # Print the queue after dequeues
    print("Queue after dequeues:", queue)
    
    # Check if the queue is empty
    print("Does the queue have elements?", bool(queue))
    
    # Dequeue remaining elements
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    
    # Try to dequeue from an empty queue
    try:
        print("Dequeued from empty queue:", queue.dequeue())
    except Exception as e:
        print(e)
    
    # Check if the queue is empty again
    print("Does the queue have elements?", bool(queue))

    # Use the alternative constructor
    queue2 = Queue.from_list([5, 'hello', [1, 2, 3], 3.14, True])
    print("Using the alternative constructor:", queue2)

    # Check contains method
    item = 3.14
    print(f"Is the item {item} in the queue: {queue2}?", item in queue2)
    
    item = 3.1
    print(f"Is the item {item} in the queue: {queue2}?", item in queue2)

    # Check get item method using index
    index = 0
    print(f"Get the item in the index [{index}]:", queue2[index])
    index = -1
    print(f"Get the item in the index [{index}]:", queue2[index])

    # Check get item method using slice
    s = slice(0, 3, 1)
    print(f"Get the items in the [{s}]:", queue2[s])

    # Check reversed
    print("Reversed queue:", list(reversed(queue2)))


if __name__ == "__main__":
    demo()