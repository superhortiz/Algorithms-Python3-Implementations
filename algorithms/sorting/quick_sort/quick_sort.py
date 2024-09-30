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

def sort(a: list, lo: int, hi: int) -> None:
    """
    Recursively sort the subarray a[lo..hi] using the Quicksort algorithm.

    Args:
        a (list): The list of elements to be sorted.
        lo (int): The lower index of the subarray.
        hi (int): The higher index of the subarray.

    Note:
        This function modifies the original list.
    """

    # Base case: if the subarray has one or no elements, it's already sorted
    if hi <= lo:
        return

    # Partition the array and get the pivot index
    j = partition(a, lo, hi)

    # Recursively sort the left and right subarrays
    sort(a, lo, j - 1)
    sort(a, j + 1, hi)

def quick_sort(a: list) -> None:
    """
    Sort a list of elements in ascending order using the Quicksort algorithm.

    Performance:
        Average case: O(N log N).
        Worst case: O(N^2) (rare, due to random shuffling).

    Args:
        a (list): The list of elements to be sorted.

    Raises:
        ValueError: If the argument is not a list.

    Note:
        Quick Sort is a not stable sorting algorithm.
        This function modifies the original list.
    """

    if not isinstance(a, list):
        raise ValueError("ValueError: Input must be a list.")

    # Shuffle the array to guarantee performance
    random.shuffle(a)
    lo = 0
    hi = len(a) - 1

    # Sort the entire array
    sort(a, lo, hi)
