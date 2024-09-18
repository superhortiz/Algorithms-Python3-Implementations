from collections import defaultdict

class UnionFind:
    """
    A weighted quick union data structure with path compression.

    Methods:
        root(i): Finds the root of the component containing site i.
        connected(p, q): Checks if sites p and q are in the same component.
        union(p, q): Merges the components containing sites p and q.
    """

    def __init__(self: 'UnionFind', n: int) -> None:
        """
        Initializes a Weighted Quick Union data structure.

        Args:
            n (int): The number of sites in the system.

        Raises:
            ValueError: If the n is None.
        """
        if n is None:
            raise ValueError

        # Initialize the id array: Each site is initially its own root.
        self.__id = list(range(n))
        self.__size = [1] * (n) # Initialize component sizes

    @property
    def count(self: 'UnionFind') -> int:
        """
        Returns the number of connected components.

        This attribute is read-only and cannot be modified directly.

        Returns:
            int: The number of connected components.
        """
        self._count = len(self.__components())
        return self._count
    
    @count.setter
    def count(self: 'UnionFind', *args, **kwargs) -> None:
        """
        Raises AttributeError to prevent modification.

        The size attribute is updated internally by add and remove operations.
        Attempting to set it directly will raise an AttributeError.

        Raises:
            AttributeError: Always raised to prevent modification.
        """
        raise AttributeError("This attribute is immutable")

    def __components(self: 'UnionFind') -> list:
        """
        Returns the connected components in the Union Find structure.

        Returns:
            components (list): A dictionary where keys are roots and values are sets of connected sites.
        """
        components = defaultdict(set)
        for i, index in enumerate(self.__id):
            root = self.__root(i)
            components[root].add(i)

        return list(components.values())

    def __root(self: 'UnionFind', i: int) -> int:
        """
        Finds the root (representative) of the component containing site i.

        Args:
            i (int): Site index.

        Returns:
            i (int): Root of the component.
        """

        # Chase parent pointers until reach root (path compression)
        while self.__id[i] != i:
            # Path compression: Flatten the tree by updating parent pointers
            self.__id[i] = self.__id[self.__id[i]]
            i = self.__id[i]

        return i

    def connected(self: 'UnionFind', p: int, q: int) -> bool:
        """
        Checks if sites p and q are in the same component.

        Args:
            p (int): Site index.
            q (int): Site index.

        Returns:
            bool: True if p and q are connected, False otherwise.

        Raises:
            ValueError: If the value of p or q is None.
            IndexError: IF the value of p or q is out of the range
        """
        if p is None or q is None:
            raise ValueError

        if not 0 <= p <= len(self.__size) or not 0 <= q <= len(self.__size):
            raise IndexError

        return self.__root(p) == self.__root(q)

    def union(self: 'UnionFind', p: int, q: int) -> None:
        """
        Merges the components containing sites p and q.

        Args:
            p (int): Site index.
            q (int): Site index.

        Raises:
            ValueError: If the value of p or q is None.
            IndexError: IF the value of p or q is out of the range
        """
        if p is None or q is None:
            raise ValueError

        if not 0 <= p <= len(self.__size) or not 0 <= q <= len(self.__size):
            raise IndexError

        # Change root of p to point to root of q (weighted union)
        i = self.__root(p)
        j = self.__root(q)

        if i == j:
            return

        if self.__size[i] < self.__size[j]:
            self.__id[i] = j
            self.__size[j] += self.__size[i]

        else:
            self.__id[j] = i
            self.__size[i] += self.__size[j]

    def __str__(self: 'UnionFind') -> str:
        """
        Returns a string representation of connected components in the
        Union Find structure.

        Returns:
            str: A string showing the connected components.
        """
        return f"{self.__components()}"