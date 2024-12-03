import random


def sort(a: list, lo: int, hi: int) -> None:
    """
    Sorts the array using the 3-way partitioning quicksort algorithm.

    Args:
        a (list): The list of elements to be sorted.
        lo (int): The lower index of the subarray.
        hi (int): The higher index of the subarray.

    Note:
        This function modifies the original list.
    """
    if hi <= lo:
        return

    # Initialize pointers for less than and greater than partitions
    less_than, greater_than = lo, hi
    
    # Choose the partitioning element (pivot)
    pivot = a[lo]

    # Initialize the current element pointer
    i = lo

    while i <= greater_than:
        if a[i] < pivot:
            # Element is less than pivot, swap with element at less_than and move both pointers
            a[less_than], a[i] = a[i], a[less_than]
            i += 1
            less_than += 1
        elif a[i] > pivot:
            # Element is greater than pivot, swap with element at greater_than and move greater_than pointer
            a[i], a[greater_than] = a[greater_than], a[i]
            greater_than -= 1
        else:
            # Element is equal to pivot, just move the current element pointer
            i += 1

    # Recursively sort the subarrays
    sort(a, lo, less_than - 1)
    sort(a, less_than + 1, hi)

def dijkstra_3way_partition(a: list) -> None:
    """
    Sort a list of elements in ascending order using 3-way partitioning quicksort algorithm,
    also known as the Dutch National Flag algorithm.

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

    # Shuffle the array to ensure average-case performance
    random.shuffle(a)
    lo = 0
    hi = len(a) - 1
    sort(a, lo, hi)
