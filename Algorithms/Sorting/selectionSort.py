def selectionSort(data):
    """
    Sort a list of elements in ascending order using the selection sort algorithm.

    Performance:
    - Comparisons: O(N^2/2) in the worst case
    - Exchanges: O(N) in the worst case

    Args:
        data (list): The list of elements to be sorted.

    Returns:
        list: The sorted list.
    """
    n = len(data)

    for i in range(n):
        min_index = i

        # Find the minimum element in the remaining unsorted array
        for j in range(i + 1, n):
            if data[j] < data[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        data[i], data[min_index] = data[min_index], data[i]

    return data


# Example usage
if __name__ == "__main__":
    data = [8, 1, 3, 7, 5, 6, 4, 1]

    print("Sorted Array in Ascending Order:")
    print(selectionSort(data))