def shell_sort(data: list) -> None:
    """
    Sort a list of elements in ascending order using the shell sort algorithm.

    Performance:
        Comparisons: Depends on the gap sequence; typically better than O(N^2).
        Exchanges: Depends on the gap sequence; typically better than O(N^2).

    Gap sequence:
        Hibbard's sequence (3x + 1).

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
    h = 1

    while h < n / 3:

        # First, we estimate the biggest h we need
        h = h * 3 + 1

    while h >= 1:
        for i in range(h, n):
            for j in range(i, h - 1, - h):

                # The limit is h-1, then when we check data[j] < data[j - h], data[h] < data[0] is the last to check
                if data[j] < data[j - h]:
                    data[j], data[j - h] = data[j - h], data[j]

        # Reduce h to refine the sorting
        h = h // 3
