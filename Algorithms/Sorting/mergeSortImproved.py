def insertionSort(a, lo, hi):
    """
    Sort a sublist of elements in ascending order using the insertion sort algorithm.

    Args:
        a (list): The list of elements to be sorted.
        lo (int): The starting index of the sublist to be sorted.
        hi (int): The ending index of the sublist to be sorted.

    Returns:
        None
    """
    for i in range(lo, hi + 1, 1):
        for j in range(i, 0, -1):
            if a[j] < a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]
            else:
                break

def merge(a, aux, lo, mid, hi):
    """
    Merge two sorted subarrays into a single sorted subarray.

    Args:
        a (list): The original array containing the subarrays to be merged.
        aux (list): An auxiliary array used for merging.
        lo (int): The starting index of the first subarray.
        mid (int): The ending index of the first subarray.
        hi (int): The ending index of the second subarray.

    Returns:
        None
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

def sort(a, aux, lo, hi):
    """
    Recursively sort the array using merge sort with improvements.

    Improvements:
    1. Use insertion sort for small subarrays (cutoff ~ 7 items).
    2. Stop if the array is already sorted.

    Args:
        a (list): The array to be sorted.
        aux (list): An auxiliary array used for merging.
        lo (int): The starting index of the subarray to be sorted.
        hi (int): The ending index of the subarray to be sorted.

    Returns:
        None
    """
    cutoff = 4
    if hi <= lo + cutoff - 1: # Improvement 1: Use insertion sort for small subarrays. Cutoff ~ 7 items
        insertionSort(a, lo, hi)
        return

    mid = lo + (hi - lo) // 2
    sort(a, aux, lo, mid)
    sort(a, aux, mid + 1, hi)

    if a[mid] <= a[mid + 1]: # Improvement 2: Stop if already sorted
        return

    merge(a, aux, lo, mid, hi)

def mergeSort(a):
    """
    Sort an array in ascending order using the merge sort algorithm with improvements.

    Performance:
    - Time Complexity: O(N log N) in the best, average, and worst case.
    - Space Complexity: O(N) due to the auxiliary array.

    Args:
        a (list): The array to be sorted.

    Returns:
        None
    """
    n = len(a)
    aux = [0 for i in range(n)]
    sort(a, aux, 0, n - 1)


# Example usage
if __name__ == "__main__":
    data = [i for i in range(20, -1, -1)]

    print("Sorted Array in Ascending Order:")
    mergeSort(data)
    print(data)