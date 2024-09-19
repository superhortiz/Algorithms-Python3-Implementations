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
    lt, gt = lo, hi
    
    # Choose the partitioning element (pivot)
    v = a[lo]

    # Initialize the current element pointer
    i = lo

    while i <= gt:
        if a[i] < v:
            # Element is less than pivot, swap with element at lt and move both pointers
            a[lt], a[i] = a[i], a[lt]
            i += 1
            lt += 1
        elif a[i] > v:
            # Element is greater than pivot, swap with element at gt and move gt pointer
            a[i], a[gt] = a[gt], a[i]
            gt -= 1
        else:
            # Element is equal to pivot, just move the current element pointer
            i += 1

    # Recursively sort the subarrays
    sort(a, lo, lt - 1)
    sort(a, lt + 1, hi)

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
