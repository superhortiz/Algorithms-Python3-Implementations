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

def mergeBU(a):
    """
    Sort an array in ascending order using the bottom-up merge sort algorithm.

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
    sz = 1

    while sz < n:
        for lo in range(0, n - sz, sz + sz):
            merge(a, aux, lo, lo + sz - 1, min(lo + sz + sz - 1, n - 1))

        sz += sz


# Example usage
if __name__ == "__main__":
    data = [i for i in range(20, -1, -1)]

    print("Sorted Array in Ascending Order:")
    mergeBU(data)
    print(data)