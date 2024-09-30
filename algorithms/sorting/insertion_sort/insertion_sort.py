def _insertion_sort(data: list, lo: int, hi: int) -> None:
    """
    Sort a sublist of elements in ascending order using the insertion sort algorithm.

    Args:
        data (list): The list of elements to be sorted.
        lo (int): The starting index of the sublist to be sorted.
        hi (int): The ending index of the sublist to be sorted.

    Note:
        This function modifies the original list.
    """
    for i in range(lo, hi + 1):
        for j in range(i, lo, -1):
            if data[j] < data[j - 1]:
                data[j], data[j - 1] = data[j - 1], data[j]
            else:
                break

def insertion_sort(data: list) -> None:
    """
    Sort a list of elements in ascending order using the insertion sort algorithm.

    Performance:
        Comparisons: ~N^2/4 in the worst case.
        Exchanges: ~N^2/4 in the worst case.

    Args:
        data (list): The list of elements to be sorted.

    Raises:
        ValueError: If the argument is not a list.

    Note:
        This function modifies the original list.
    """
    if not isinstance(data, list):
        raise ValueError("ValueError: Input must be a list.")

    _insertion_sort(data, 0, len(data) - 1)
