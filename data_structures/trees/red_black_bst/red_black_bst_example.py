from data_structures import RedBlackBST


def demo() -> None:
    # Create an empty red_black_bst
    red_black_bst = RedBlackBST()

    # Insert values using add method
    for i in range(100):
        red_black_bst.add(i)

    # Insert values using setitem method
    red_black_bst[9] = 9

    # Graphic representation
    print("Graphic representation of the Red-Black BST:")
    red_black_bst.print_tree()

    print("\nGraphic representation of the Red-Black BST as a 2-3 Tree:")
    red_black_bst.print_tree_balanced()

    # Checking methods
    key = 8
    print(f"Does the tree countain the key {key}?", key in red_black_bst)
    print(f"Value in the key {key}?", red_black_bst[key])
    print("Minimum key in the tree:", red_black_bst.min())
    print("Maximum key in the tree:", red_black_bst.max())
    print("Number of elements in the tree:", len(red_black_bst))

    # Iterate over the red_black_bst
    for i, item in enumerate(red_black_bst):
        print(f"Item {i}:", item)

    # Iterate over the red_black_bst in reversed order
    print("\nIn reversed order")
    for i, item in enumerate(reversed(red_black_bst)):
        print(f"Item {len(red_black_bst) - i - 1}:", item)

    # Check contains method
    item = 3
    print(f"Is the item {item} in the red_black_bst?", item in red_black_bst)
    item = 3.5
    print(f"Is the item {item} in the red_black_bst?", item in red_black_bst)

    # Check rank method
    key = 3
    print(f"Number of keys less than {key} in the red_black_bst:", red_black_bst.rank(key))

    # Check ceiling and floor
    n = 5.5
    print(f"Ceiling of {n}:", red_black_bst.ceiling(n))
    print(f"Floor of {n}:",red_black_bst.floor(n))

    # Check get item method
    key = 2
    print(f"Get item in the key {key}:", red_black_bst[2])
    key = slice(1, 6, 2)
    print(f"Get item in the key {key}:", list(red_black_bst[key]))

    # Delete several values, min and max
    for _ in range(20):
        red_black_bst.delete_min()
        red_black_bst.delete_max()

    # Check delete item method
    key = 35
    del red_black_bst[key]
    key = 50
    del red_black_bst[key]
    key = 65
    del red_black_bst[key]
    print(f"Tree after deleting the element in key {key}:", red_black_bst)
    print("Number of elements in the tree:", len(red_black_bst))
    red_black_bst.print_tree_balanced()


if __name__ == "__main__":
    demo()