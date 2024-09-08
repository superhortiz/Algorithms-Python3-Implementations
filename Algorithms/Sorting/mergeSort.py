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

    i, j = lo, mid + 1  # Pointers for the first and second halves of the array

    for k in range(lo, hi + 1, 1): # Merge
        if i > mid:  # First half get exhausted
            a[k] = aux[j]
            j += 1  # Update pointer
        elif j > hi: # Second half get exhausted
            a[k] = aux[i]
            i += 1  # Update pointer
        elif aux[j] < aux[i]:
            a[k] = aux[j]
            j += 1  # Update pointer
        else:
            a[k] = aux[i]
            i += 1  # Update pointer

def sort(a, aux, lo, hi):
    """
    Recursively sort the array using merge sort.

    Args:
        a (list): The array to be sorted.
        aux (list): An auxiliary array used for merging.
        lo (int): The starting index of the subarray to be sorted.
        hi (int): The ending index of the subarray to be sorted.

    Returns:
        None
    """
    if hi <= lo:
        return

    mid = lo + (hi - lo) // 2
    sort(a, aux, lo, mid)
    sort(a, aux, mid + 1, hi)
    merge(a, aux, lo, mid, hi)

def mergeSort(a):
    """
    Sort an array in ascending order using the merge sort algorithm.

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