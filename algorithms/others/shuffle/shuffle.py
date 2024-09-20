import random

def shuffle(a: list) -> None:
    """
    Shuffle the array using the Knuth (or Fisher-Yates) shuffle algorithm.

    Performance:
        Time complexity: O(N)
        Space complexity: O(1)

    Args:
        a (list): The list of elements to be shuffled.

    Raises:
        ValueError: If the argument is not a list.

    Note:
        This function modifies the original list.
    """
    if not isinstance(a, list):
        raise ValueError("ValueError: Input must be a list.")

    n = len(a)

    for i in range(n):
        # Generate a random index from 0 to i
        random_index = random.randint(0, i)

        # Swap the current element with the element at the random index
        a[i], a[random_index] = a[random_index], a[i]
