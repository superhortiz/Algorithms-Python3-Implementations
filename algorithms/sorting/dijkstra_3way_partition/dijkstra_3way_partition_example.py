import random
from .dijkstra_3way_partition import dijkstra_3way_partition

def demo() -> None:
    """
    Example usage
    """
    help(dijkstra_3way_partition)
    print("Example 1.")
    print("Array before ordering:")
    data = [random.randint(-20, 20) for _ in range(20)]
    print(data)
    print("Sorted Array in Ascending Order:")
    dijkstra_3way_partition(data)
    print(data)

    print("\nExample 2.")
    print("Array before ordering:")
    data = [random.randint(-20, 20) for i in range(20)]
    print(data)
    print("Sorted Array in Ascending Order:")
    dijkstra_3way_partition(data)
    print(data)

if __name__ == "__main__":
    demo()