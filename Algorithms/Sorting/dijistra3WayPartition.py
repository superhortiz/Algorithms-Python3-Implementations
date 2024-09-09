import random

def sort(a, lo, hi):
    """
    Sorts the array using the 3-way partitioning quicksort algorithm.

    Args:
        a (list): The list of elements to be sorted.
        lo (int): The lower index of the subarray.
        hi (int): The higher index of the subarray.
    """
    if hi <= lo:
        return

    lt, gt = lo, hi  # Initialize pointers for less than and greater than partitions
    v = a[lo]  # Choose the partitioning element (pivot)
    i = lo  # Initialize the current element pointer

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

def dijistra3WayPartition(a):
    """
    Shuffles the array and sorts it using the 3-way partitioning quicksort algorithm.

    Args:
        a (list): The list of elements to be sorted.
    """
    random.shuffle(a)  # Shuffle the array to ensure average-case performance
    lo = 0
    hi = len(a) - 1
    sort(a, lo, hi)


# Example usage
if __name__ == "__main__":
    a = [1, 2, 1, 0, 1, 0, 1, 2, 0, 1, 2, 0, 1, 2, 1, 0, 2, 0, 1, 2]
    print(a)
    print("Sorted Array in Ascending Order:")
    dijistra3WayPartition(a)
    print(a)