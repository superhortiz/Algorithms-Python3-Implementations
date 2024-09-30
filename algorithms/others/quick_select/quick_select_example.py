import random
from algorithms import quick_select


def demo():
    """
    Example usage
    """
    help(quick_select)
    a = [10, 9, 6, 20, 7, 8, 13, 0, 15, 11, 19, 12, 1, 18, 4, 17, 2, 14, 16, 3, 5]
    k = 5
    print("Example 1.")
    print("Array:", a)
    value = quick_select(a, k)
    print(f"{k}th smallest item =", value)

    random.shuffle(a)
    k = 7
    print("\nExample 2.")
    print("Array:", a)
    value = quick_select(a, k)
    print(f"{k}th smallest item =", value)

    random.shuffle(a)
    k = 12
    print("\nExample 3.")
    print("Array:", a)
    value = quick_select(a, k)
    print(f"{k}th smallest item =", value)

if __name__ == "__main__":
    demo()