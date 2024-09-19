import random
from algorithms.sorting.quick_sort_improved import quick_sort_improved

def demo() -> None:
    """
    Example usage
    """
    help(quick_sort_improved)
    print("Example 1.")
    print("Array before ordering:")
    data = [random.randint(-20, 20) for _ in range(20)]
    print(data)
    print("Sorted Array in Ascending Order:")
    quick_sort_improved(data)
    print(data)

    print("\nExample 2.")
    print("Array before ordering:")
    data = [random.randint(-20, 20) for i in range(20)]
    print(data)
    print("Sorted Array in Ascending Order:")
    quick_sort_improved(data)
    print(data)

if __name__ == "__main__":
    demo()