import random
from algorithms.sorting.insertion_sort import __insertion_sort

def median_of_3(a: int, b: int, c: int, arr: list) -> int:
    """
    Return the index of the median of three elements in the array.
    This functions helps to estimate the true median of the array,
    which improves the performance of Quick Sort.

    Args:
        a (int): The index of the first element.
        b (int): The index of the second element.
        c (int): The index of the third element.
        arr (list): The list of elements.

    Returns:
        index (int): The index of the median element.
    """
    if (arr[a] - arr[b]) * (arr[c] - arr[a]) >= 0:
        return a
    elif (arr[b] - arr[a]) * (arr[c] - arr[b]) >= 0:
        return b
    else:
        return c

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

    # Improvement 1: Use insertion sort for small subarrays (recommended = 10)
    cutoff = 10
    if hi <= lo + cutoff - 1:
        __insertion_sort(a, lo, hi)
        return

    # Improvement 2: Estimate true median by taking median of sample (recommended = 3 items)
    m = median_of_3(lo, lo + (hi - lo) // 2, hi, a)
    a[lo], a[m] = a[m], a[lo]

    j = partition(a, lo, hi)
    sort(a, lo, j - 1)
    sort(a, j + 1, hi)

def quick_sort_improved(a: list) -> None:
    """
    Sort a list of elements in ascending order using the Quick Sort algorithm with improvements.

    Improvements:
        Use insertion sort for small subarrays (recommended = 10).
        Estimate true median by taking median of sample (recommended = 3 items).

    Performance:
        Average case: O(N log N)
        Worst case: O(N^2) (rare, due to random shuffling)

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
    sort(a, lo, hi)
