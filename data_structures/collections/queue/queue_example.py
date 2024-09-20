from .queue import Queue

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
    
    # Dequeue elements from the queue
    print("Dequeued:", queue.dequeue())
    print("Dequeued:", queue.dequeue())
    
    # Print the queue after dequeues
    print("Queue after dequeues:", queue)
    
    # Check if the queue is empty
    print("Is queue empty?", queue.is_empty())
    
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
    print("Is queue empty?", queue.is_empty())

    # Use the alternative constructor
    queue2 = Queue.from_list([5, 'hello', [1, 2, 3], 3.14, True])
    print("Use the alternative constructor:", queue2)


if __name__ == "__main__":
    demo()