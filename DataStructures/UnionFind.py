class UnionFind:
    """
    A weighted quick union data structure with path compression.

    Methods:
        root(i): Finds the root of the component containing site i.
        connected(p, q): Checks if sites p and q are in the same component.
        union(p, q): Merges the components containing sites p and q.
    """

    def __init__(self, n):
        """
        Initializes a Weighted Quick Union data structure.

        Args:
            n (int): The number of sites in the system.
        """
        # Initialize the id array: Each site is initially its own root.
        self.id = [i for i in range(n)]
        self.size = [1] * (n) # Initialize component sizes

    def root(self, i):
        """
        Finds the root (representative) of the component containing site i.

        Args:
            i (int): Site index.

        Returns:
            int: Root of the component.
        """

        # Chase parent pointers until reach root (path compression)
        while self.id[i] != i:
            # Path compression: Flatten the tree by updating parent pointers
            self.id[i] = self.id[self.id[i]]
            i = self.id[i]

        return i

    def connected(self, p, q):
        """
        Checks if sites p and q are in the same component.

        Args:
            p (int): Site index.
            q (int): Site index.

        Returns:
            bool: True if p and q are connected, False otherwise.
        """

        return self.root(p) == self.root(q)

    def union(self, p, q):
        """
        Merges the components containing sites p and q.

        Args:
            p (int): Site index.
            q (int): Site index.
        """

        # Change root of p to point to root of q (weighted union)
        i = self.root(p)
        j = self.root(q)

        if i == j:
            return

        if self.size[i] < self.size[j]:
            self.id[i] = j
            self.size[j] += self.size[i]

        else:
            self.id[j] = i
            self.size[i] += self.size[j]


# Example usage
if __name__ == "__main__":
    # Initialize a union-find structure with 10 sites (0 through 9)
    uf = UnionFind(10)
    
    # Perform some union operations
    uf.union(4, 3)
    uf.union(3, 8)
    uf.union(6, 5)
    uf.union(9, 4)
    uf.union(2, 1)
    
    # Check if certain sites are connected
    print("1 and 2 connected:", uf.connected(1, 2))  # Output: True
    print("1 and 9 connected:", uf.connected(1, 9))  # Output: False
    
    # Perform more union operations
    uf.union(5, 0)
    uf.union(7, 2)
    uf.union(6, 1)
    uf.union(7, 3)
    
    # Check if certain sites are connected after more unions
    print("1 and 9 connected:", uf.connected(1, 9))  # Output: True