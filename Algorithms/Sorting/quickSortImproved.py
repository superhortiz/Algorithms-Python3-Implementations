import random

def medianOf3(a, b, c, arr):
    """
    Return the index of the median of three elements in the array.

    Args:
        a (int): The index of the first element.
        b (int): The index of the second element.
        c (int): The index of the third element.
        arr (list): The list of elements.

    Returns:
        int: The index of the median element.
    """
    if (arr[a] - arr[b]) * (arr[c] - arr[a]) >= 0:
        return a
    elif (arr[b] - arr[a]) * (arr[c] - arr[b]) >= 0:
        return b
    else:
        return c

def insertionSort(a, lo, hi):
    """
    Sort a subarray using the insertion sort algorithm.

    Args:
        a (list): The list of elements to be sorted.
        lo (int): The lower index of the subarray.
        hi (int): The higher index of the subarray.
    """
    for i in range(lo, hi + 1):
        for j in range(i, lo, -1):
            if a[j] < a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]
            else:
                break

def partition(a, lo, hi):
    """
    Partition the subarray a[lo..hi] so that a[lo..j-1] <= a[j] <= a[j+1..hi] and return the index j.

    Args:
        a (list): The list of elements to be partitioned.
        lo (int): The lower index of the subarray.
        hi (int): The higher index of the subarray.

    Returns:
        int: The index of the pivot element after partitioning.
    """
    i, j = lo + 1, hi

    while True:
        while a[i] < a[lo]:
            i += 1
            if i == hi: break
        while a[j] > a[lo]:
            j -= 1
            if j == lo: break
        if i >= j: break
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    a[lo], a[j] = a[j], a[lo]
    return j

def sort(a, lo, hi):
    """
    Recursively sort the subarray a[lo..hi] using the Quicksort algorithm with improvements.

    Args:
        a (list): The list of elements to be sorted.
        lo (int): The lower index of the subarray.
        hi (int): The higher index of the subarray.
    """
    cutoff = 3  # Improvement 1: Use insertion sort for small subarrays (recommended = 10)
    if hi <= lo + cutoff - 1:
        insertionSort(a, lo, hi)
        return

    m = medianOf3(lo, lo + (hi - lo) // 2, hi, a) # Improvement 2: Estimate true median by taking median of sample (recommended = 3 items)
    a[lo], a[m] = a[m], a[lo]

    j = partition(a, lo, hi)
    sort(a, lo, j - 1)
    sort(a, j + 1, hi)

def quickSort(a):
    """
    Sort a list of elements in ascending order using the Quicksort algorithm with improvements.

    Performance:
    - Average case: O(N log N)
    - Worst case: O(N^2) (rare, due to random shuffling)

    Args:
        a (list): The list of elements to be sorted.
    """
    random.shuffle(a)
    lo = 0
    hi = len(a) - 1
    sort(a, lo, hi)


# Example usage
if __name__ == "__main__":
    a = [10, 9, 6, 20, 7, 8, 13, 0, 15, 11, 19, 12, 1, 18, 4, 17, 2, 14, 16, 3, 5]
    print(a)
    print("Sorted Array in Ascending Order:")
    quickSort(a)
    print(a)