import random

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
    i, j = lo + 1, hi  # Initialize pointers

    while True:
        # Move i to the right as long as elements are less than the pivot
        while a[i] < a[lo]:
            i += 1
            if i == hi:
                break

        # Move j to the left as long as elements are greater than the pivot
        while a[j] > a[lo]:
            j -= 1
            if j == lo:
                break

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

def sort(a, lo, hi):
    """
    Recursively sort the subarray a[lo..hi] using the Quicksort algorithm.

    Args:
        a (list): The list of elements to be sorted.
        lo (int): The lower index of the subarray.
        hi (int): The higher index of the subarray.
    """

    # Base case: if the subarray has one or no elements, it's already sorted
    if hi <= lo:
        return

    # Partition the array and get the pivot index
    j = partition(a, lo, hi)

    # Recursively sort the left and right subarrays
    sort(a, lo, j - 1)
    sort(a, j + 1, hi)

def quickSort(a):
    """
    Sort a list of elements in ascending order using the Quicksort algorithm.

    Performance:
    - Average case: O(N log N)
    - Worst case: O(N^2) (rare, due to random shuffling)

    Args:
        a (list): The list of elements to be sorted.
    """

    # Shuffle the array to guarantee performance
    random.shuffle(a)
    lo = 0
    hi = len(a) - 1

    # Sort the entire array
    sort(a, lo, hi)


# Example usage
if __name__ == "__main__":
    a = [10, 9, 6, 20, 7, 8, 13, 0, 15, 11, 19, 12, 1, 18, 4, 17, 2, 14, 16, 3, 5]
    print(a)
    print("Sorted Array in Ascending Order:")
    quickSort(a)
    print(a)