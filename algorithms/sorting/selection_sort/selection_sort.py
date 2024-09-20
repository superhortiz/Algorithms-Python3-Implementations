def selection_sort(data: list) -> None:
    """
    Sort a list of elements in ascending order using the selection sort algorithm.

    Performance:
        Comparisons: O(N^2/2) in the worst case.
        Exchanges: O(N) in the worst case.

    Args:
        data (list): The list of elements to be sorted.

    Raises:
        ValueError: If the argument is not a list.
        
    Note:
        This function modifies the original list.
    """
    if not isinstance(data, list):
        raise ValueError("ValueError: Input must be a list.")

    n = len(data)

    for i in range(n):
        min_index = i

        # Find the minimum element in the remaining unsorted array
        for j in range(i + 1, n):
            if data[j] < data[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        data[i], data[min_index] = data[min_index], data[i]