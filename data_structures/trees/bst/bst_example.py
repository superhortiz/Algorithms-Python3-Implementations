from data_structures import BST


def demo() -> None:
    # Create an empty BST
    bst = BST()

    # Insert values
    bst.add(4)
    bst.add(2)
    bst.add(6)
    bst.add(1)
    bst.add(3)
    bst.add(5)
    bst.add(7)
    bst.add(8)
    bst[9] = 9

    # Graphic representation
    bst.print_tree()

    # Checking methods
    key = 8
    print(f"Does the tree countain the key {key}?", key in bst)
    print(f"Value in the key {key}?", bst[key])
    print("Minimum key in the tree:", bst.min())
    print("Maximum key in the tree:", bst.max())
    print("Number of elements in the tree:", len(bst))

    # Iterate over the BST
    for i, item in enumerate(bst):
        print(f"Item {i+1}:", item)

    # Iterate over the BST in reversed order
    print("In reversed order")
    for i, item in enumerate(reversed(bst)):
        print(f"Item {len(bst) - i}:", item)

    # Check contains method
    item = 3
    print(f"Is the item {item} in the BST?", item in bst)
    item = 3.5
    print(f"Is the item {item} in the BST?", item in bst)

    # Check rank method
    key = 3
    print(f"Number of keys less than {key} in the BST:", bst.rank(key))

    # Check ceiling and floor
    n = 5.5
    print(f"Ceiling of {n}:", bst.ceiling(n))
    print(f"Floor of {n}:",bst.floor(n))

    # Check get item method
    key = 2
    print(f"Get item in the key {key}:", bst[2])
    key = slice(1, 6, 2)
    print(f"Get item in the key {key}:", list(bst[key]))

    # Check delete item method
    key = 5
    del bst[key]
    print(f"Tree after deleting the element in key {key}:", bst)
    print("Number of elements in the tree:", len(bst))


if __name__ == "__main__":
    demo()