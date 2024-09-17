import random

def shuffle(a):
    """
    Shuffle the array using the Knuth (or Fisher-Yates) shuffle algorithm.

    Args:
        a (list): The list of elements to be shuffled.

    Returns:
        None
    """
    n = len(a)

    for i in range(n):
        # Generate a random index from 0 to i
        random_index = random.randint(0, i)

        # Swap the current element with the element at the random index
        a[i], a[random_index] = a[random_index], a[i]

def main():
    """
    Example usage
    """
    a = [i for i in range(10)]
    print("Original array:  ", a)

    shuffle(a)
    print("Knuth shuffle:   ", a)  


if __name__ == "__main__":
    main()
