import random
from algorithms import Heapsort


def demo() -> None:
    """
    Example usage
    """
    help(Heapsort)
    print("Example 1.")
    print("Array before ordering:")
    data = [random.randint(-20, 20) for _ in range(20)]
    print(data)
    print("Sorted Array in Ascending Order:")
    Heapsort(data)
    print(data)

    print("\nExample 2.")
    print("Array before ordering:")
    data = [random.randint(-20, 20) for i in range(20)]
    print(data)
    print("Sorted Array in Ascending Order:")
    Heapsort(data)
    print(data)

if __name__ == "__main__":
    demo()