def insertionSort(data, lo, hi):
    """
    Sort a sublist of elements in ascending order using the insertion sort algorithm.

    Performance:
    - Comparisons: ~N^2/4 in the worst case
    - Exchanges: ~N^2/4 in the worst case

    Args:
        data (list): The list of elements to be sorted.
        lo (int): The starting index of the sublist to be sorted.
        hi (int): The ending index of the sublist to be sorted.

    Returns:
        list: The sorted list.
    """
    for i in range(lo, hi + 1):
        for j in range(i, lo, -1):
            if data[j] < data[j - 1]:
                data[j], data[j - 1] = data[j - 1], data[j]
            else:
                break


# Example usage
if __name__ == "__main__":
    data = [8, 1, 3, 7, 5, 6, 4, 1]

    print("Sorted Array in Ascending Order:")
    insertionSort(data, 0, len(data) - 1)
    print(data)