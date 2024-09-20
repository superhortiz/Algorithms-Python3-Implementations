from .shuffle import shuffle

def demo() -> None:
    """
    Example usage
    """
    help(shuffle)

    print("Example 1.")
    a = [i for i in range(10)]
    print("Original array:  ", a)

    shuffle(a)
    print("Knuth shuffle:   ", a)  

    print("\nExample 2.")
    a = [i for i in range(30)]
    print("Original array:  ", a)

    shuffle(a)
    print("Knuth shuffle:   ", a) 


if __name__ == "__main__":
    demo()