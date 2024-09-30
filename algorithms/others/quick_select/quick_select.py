import random


def partition(a: list, lo: int, hi: int) -> int:
    """
    Partition the subarray a[lo..hi] so that a[lo..j-1] <= a[j] <= a[j+1..hi] and return the index j.
    Pivot choice: The first element of the subarray.

    Args:
        a (list): The list of elements to be partitioned.
        lo (int): The lower index of the subarray.
        hi (int): The higher index of the subarray.

    Returns:
        j (int): The index of the pivot element after partitioning.
    """
    i, j = lo + 1, hi  # Initialize pointers

    while True:
        # Move i to the right as long as elements are less than the pivot
        while a[i] < a[lo]:
            if i == hi:
                break
            i += 1

        # Move j to the left as long as elements are greater than the pivot
        while a[j] > a[lo]:
            if j == lo:
                break
            j -= 1

        # If pointers cross, partitioning is done
        if i >= j:
            break

        # Swap elements at i and j
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    # Swap pivot element with element at j
    a[lo], a[j] = a[j], a[lo]

    return j

def quick_select(a: list, k: int) -> int:
    """
    Select the k-th smallest element in the list using the Quickselect algorithm.

    Performance:
        Average case: O(N)
        Worst case: O(N^2) (rare, due to random shuffling)

    Args:
        a (list): The list of elements.
        k (int): The k-th smallest element to find.

    Raises:
        ValueError: If the argument is not a list.
        ValueError: If the argument is an empty list.
        ValueError: If the argument is a not valid index.

    Returns:
        int: The k-th smallest element in the list.
    """

    if not isinstance(a, list):
        raise ValueError("ValueError: Input must be a list.")

    if len(a) == 0:
        raise ValueError("ValueError: The list is empty.")

    if k < 1 or k > len(a):
        raise ValueError("ValueError: Invalid index.")

    # To transform in zero-based index
    k -= 1

    # Shuffle the array to ensure average-case performance
    random.shuffle(a)
    lo = 0
    hi = len(a) - 1
    
    while hi > lo:
        j = partition(a, lo, hi)
        if j < k:
            lo = j + 1
        elif j > k:
            hi = j - 1
        else:
            return a[k]
    return a[k]
    