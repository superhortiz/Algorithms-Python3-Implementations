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

def quickSelect(a, k):
    """
    Select the k-th smallest element in the list using the Quickselect algorithm.

    Performance:
    - Average case: O(N)
    - Worst case: O(N^2) (rare, due to random shuffling)

    Args:
        a (list): The list of elements.
        k (int): The index (0-based) of the k-th smallest element to find.

    Returns:
        int: The k-th smallest element in the list.
    """
    random.shuffle(a)  # Shuffle the array to ensure average-case performance
    lo = 0
    hi = len(a) - 1
    
    while hi > lo:
        j = partition(a, lo, hi)
        if j < k:
            lo = j + 1
        elif j > k:
            hi = j - 1
        else:
            return a[k]
    return a[k]


# Example usage
if __name__ == "__main__":
    a = [10, 9, 6, 20, 7, 8, 13, 0, 15, 11, 19, 12, 1, 18, 4, 17, 2, 14, 16, 3, 5]
    k = 5
    print(a)
    value = quickSelect(a, k)
    print(f"{k}th smallest item =", value)