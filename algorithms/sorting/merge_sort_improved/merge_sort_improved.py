from algorithms.sorting.insertion_sort.insertion_sort import _insertion_sort


def merge(a: list, aux: list, lo: int, mid: int, hi: int) -> None:
    """
    Merge two sorted subarrays into a single sorted subarray.

    Args:
        a (list): The original array containing the subarrays to be merged.
        aux (list): An auxiliary array used for merging.
        lo (int): The starting index of the first subarray.
        mid (int): The ending index of the first subarray.
        hi (int): The ending index of the second subarray.

    Note:
        This function modifies the original lists a and aux.
    """
    for i in range(lo, hi + 1, 1):
        aux[i] = a[i] # Auxiliar copy of the array

    i, j = lo, mid + 1

    for k in range(lo, hi + 1, 1): # Merge
        if i > mid:  # First half get exhausted
            a[k] = aux[j]
            j += 1
        elif j > hi: # Second half get exhausted
            a[k] = aux[i]
            i += 1
        elif aux[j] < aux[i]:
            a[k] = aux[j]
            j += 1
        else:
            a[k] = aux[i]
            i += 1

def sort(a: list, aux: list, lo: int, hi: int) -> None:
    """
    Recursively sort the array using merge sort with improvements.

    Improvements:
        Use insertion sort for small subarrays (cutoff ~ 7 items).
        Stop if the array is already sorted.

    Args:
        a (list): The array to be sorted.
        aux (list): An auxiliary array used for merging.
        lo (int): The starting index of the subarray to be sorted.
        hi (int): The ending index of the subarray to be sorted.

    Note:
        This function modifies the original lists a and aux.
    """

    # Improvement 1: Use insertion sort for small subarrays. Cutoff ~ 7 items
    cutoff = 7
    if hi <= lo + cutoff - 1:
        _insertion_sort(a, lo, hi)
        return

    mid = lo + (hi - lo) // 2
    sort(a, aux, lo, mid)
    sort(a, aux, mid + 1, hi)

    # Improvement 2: Stop if already sorted
    if a[mid] <= a[mid + 1]:
        return

    merge(a, aux, lo, mid, hi)

def merge_sort_improved(a: list) -> None:
    """
    Sort an array in ascending order using the merge sort algorithm with improvements.

    Improvements:
        Use insertion sort for small subarrays (cutoff ~ 7 items).
        Stop if the array is already sorted.

    Performance:
        Time Complexity: O(N log N) in the best, average, and worst case.
        Space Complexity: O(N) due to the auxiliary array.

    Args:
        a (list): The array to be sorted.

    Raises:
        ValueError: If the argument is not a list.

    Note:
        Merge Sort is a stable sorting algorithm.
        This function modifies the original list.
    """
    if not isinstance(a, list):
        raise ValueError("ValueError: Input must be a list.")

    n = len(a)
    aux = [0 for i in range(n)]
    sort(a, aux, 0, n - 1)
