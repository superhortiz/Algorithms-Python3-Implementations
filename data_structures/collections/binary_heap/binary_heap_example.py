from data_structures import BinaryHeap


def demo():
    """
    Example usage of the binary heap implementation (max-heap)
    """
    heap = BinaryHeap()

    # Try to remove an element from an empty heap
    try:
        heap.del_max()

    except Exception as e:
        print("Try to remove an element from an empty heap:", e)
    
    # Try to obtain an element from an empty heap
    try:
        heap.peek_max()
        
    except Exception as e:
        print("Try to obtain an element from an empty heap:", e)

    # Insert elements into the heap
    heap.insert(10)
    heap.insert(20)
    heap.insert(5)
    heap.insert(30)
    heap.insert(15)
    heap.insert(6)
    heap.insert(35)
    heap.insert(45)
    
    # Print the heap
    print("Heap after inserts:", heap)  # Output: 30, 15, 5, 10, 20
    
    # Delete the maximum element
    print("Deleted max element:", heap.del_max())  # Output: 30
    
    # Print the heap after deletion
    print("Heap after deleting max:", heap)  # Output: 20, 15, 5, 10

    # Check iterator
    for i, item in enumerate(heap):
        print(f"Item {i}:", item)

    # Check contains method
    item = 20
    print(f"Is the item ({item}) in the heap?", item in heap)
    item = 2
    print(f"Is the item ({item}) in the heap?", item in heap)

    # Check getitem method
    index = 3
    print(f"Element in the index {index}:", heap[index])
    index = -1
    print(f"Element in the index {index}:", heap[index])


if __name__ == "__main__":
    demo()