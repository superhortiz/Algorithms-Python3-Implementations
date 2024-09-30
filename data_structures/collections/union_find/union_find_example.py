from data_structures import UnionFind


def demo() -> None:
    """
    Example usage of Union Find structure
    """

    # Initialize a union-find structure with 10 sites (0 through 9)
    uf = UnionFind(10)
    print("Connected components before union operations", uf)
    print("Number of connected components:", len(uf))
    for i, component in enumerate(uf):
        print(f"Component {i}:", component)

    # Perform some union operations
    uf.union(4, 3)
    uf.union(3, 8)
    uf.union(6, 5)
    uf.union(9, 4)
    uf.union(2, 1)
    print("Connected components after union operations", uf)
    print("Number of connected components:", len(uf))
    print("Slice of the list components:", uf[0:2])

    for i, component in enumerate(uf):
        print(f"Component {i}:", component)

    # Check if certain sites are connected
    print("1 and 2 connected:", uf.connected(1, 2))  # Output: True
    print("1 and 9 connected:", uf.connected(1, 9))  # Output: False

    # Perform more union operations
    uf.union(5, 0)
    uf.union(7, 2)
    uf.union(6, 1)
    uf.union(7, 3)
    print("Connected components after union operations", uf)
    print("Number of connected components:", len(uf))
    for i, component in enumerate(uf):
        print(f"Component {i}:", component)

    # Check if certain sites are connected after more unions
    print("1 and 9 connected:", uf.connected(1, 9))  # Output: True


if __name__ == "__main__":
    demo()