from typing import Any, Iterator, List, Optional, Union

class BST:
    """
    A class representing a Binary Search Tree (BST) for efficient searching and insertion.

    Performance:
        Guarantee:
            - Search: O(N)
            - Insert: O(N)
            - Delete: O(N)

        Average Case:
            - Search: O(log N)
            - Insert: O(log N)
            - Delete: O(√N) (Other operations also become √N if deletion is allowed)

    Methods:
        add(val): Adds a new node with the given value, using the value as the key.
        ceiling(key): Finds the smallest key in the BST that is greater than or equal to the given key.
        floor(key): Finds the largest key in the BST that is less than or equal to the given key.
        max(): Finds the maximum key in the BST.
        min(): Finds the minimum key in the BST.
        print_tree(): Prints the BST in a structured format.
        rank(key): Returns the number of keys less than the given key in the BST.

    Special Methods:
        __bool__(): Checks if the BST is not empty.
        __contains__(key): Checks if a key is in the BST.
        __delitem__(key): Deletes the node with the given key from the BST.
        __getitem__(key): Gets the value associated with the given key or a range of keys.
        __iter__(): Returns an iterator for in-order traversal of the BST.
        __len__(): Gets the number of nodes in the BST.
        __setitem__(key, val): Sets the value for the given key in the BST.
        __repr__(): Returns a string representation of the BST.
        __reversed__(): Returns an iterator for reverse in-order traversal of the BST.
    """

    class TreeNode:
        """
        A class representing a node in the Binary Search Tree.

        Attributes:
            count (int): The size of the subtree rooted at this node.
            key (int): The key of the node.
            left (TreeNode): The left child of this node.
            right (TreeNode): The right child of this node.
            val (Any): The value associated with the key.
        """
        def __init__(self: 'TreeNode', key: int, val: Any, count: int) -> None:
            """
            Initializes a TreeNode.

            Args:
                count (int): The size of the subtree rooted at this node.
                key (int): The key of the node.
                val (Any): The value associated with the key.
            """
            self.key = key
            self.val = val
            self.count = count
            self.left = None
            self.right = None

    def __init__(self: 'BST') -> None:
        """
        Initializes an empty BST.
        """
        self.__root = None

    def __bool__(self: 'BST') -> bool:
        """
        Checks if the BST is not empty.

        Returns:
            bool: True if the tree is not empty, False otherwise.
        """
        return self.__root is not None

    def __len__(self: 'BST') -> int:
        """
        Gets the number of nodes in the BST.

        Returns:
            int: The total number of nodes in the tree.
        """
        return self._size(self.__root)

    def _size(self: 'BST', node: 'BST.TreeNode') -> int:
        """
        Returns the size of the subtree rooted at the given node.

        Args:
            node (BST.TreeNode): The root of the subtree.

        Returns:
            int: The total number of nodes in the subtree.
        """
        if node is None:
            return 0
        return node.count

    def __setitem__(self: 'BST', key: int, val: Any) -> None:
        """
        Sets the value for the given key in the BST.

        Args:
            key (int): The key of the node.
            val (Any): The value to be set for the key.

        Raises:
            ValueError: If 'key' is not an int type.
            ValueError: If 'val' is None.
        """
        if not isinstance(key, int):
            raise ValueError("The key must be a integer type.")

        if val is None:
            raise ValueError("ValueError: Invalid value.")

        # This handles the case the client sets the key.
        self.__root = self._add(self.__root, key, val)

    def add(self: 'BST', val: int) -> None:
        """
        Adds a new node with the given value, using the value as the key.

        Args:
            val (int): The value to be added as both key and value.

        Raises:
            ValueError: If 'key' is not an int type.
            ValueError: If 'val' is None.
        """
        if not isinstance(val, int):
            raise ValueError("The value must be a integer type.")

        # This handles the case the client does not provide a key.
        # Then we use key = value.
        self.__root = self._add(self.__root, val, val)

    def _add(self: 'BST', node: 'BST.TreeNode', key: int, val: Any) -> 'BST.TreeNode':
        """
        Helper method to add a new node to the BST.

        Args:
            node (BST.TreeNode): The root of the subtree.
            key (int): The key of the new node.
            val (Any): The value associated with the key.

        Returns:
            BST.TreeNode: The root of the subtree after insertion.
        """

        # End of the tree reached, return a new TreeNode
        if node is None:
            return self.TreeNode(key, val, 1)

        # Explore recursively the left child
        if key < node.key:
            node.left = self._add(node.left, key, val)

        # Explore recursively the right child
        elif key > node.key:
            node.right = self._add(node.right, key, val)

        # The key is already in the tree, ovewrite the value
        elif key == node.key:
            node.val = val

        # Update the count
        node.count = 1 + self._size(node.left) + self._size(node.right)

        # Return the corresponding link to the node
        return node

    def __getitem__(self: 'BST', key: Union[int, slice]) -> Union[Any, List[Any]]:
        """
        Gets the value associated with the given key or a range of keys.

        Args:
            key (Union[int, slice]): The key or slice of keys to retrieve.

        Returns:
            Union[Any, List[Any]]: The value associated with the key, or a list of values for the range of keys.

        Raises:
            KeyError: If the key is not found in the tree.
            TypeError: If the argument is not an int or slice.
        """
        # Case 1: Requesting a specific index
        if isinstance(key, int):
            node = self.__root

            # Iterate through the tree until the key is found
            while node:
                if key < node.key:
                    node = node.left
                elif key > node.key:
                    node = node.right
                elif key == node.key:
                    return node.val
            raise KeyError(f"Key {key} not found in the tree.")

        # Case 2: Requesting a slice
        elif isinstance(key, slice):

            # Adapt the slices to the size of the tree
            start, stop, step = key.indices(self.__len__())

            def range(node: 'BST.TreeNode', key_lo: int, key_hi: int, step: int) -> List[int]:
                """
                Helper generator to yield keys within the specified range.

                Args:
                    node (BST.TreeNode): The root of the subtree.
                    key_lo (int): The lower bound of the range.
                    key_hi (int): The upper bound of the range.
                    step (int): The step value for the range.

                Yields:
                    int: The keys within the specified range.
                """
                # End of the tree reached, return
                if node is None:
                    return

                # Explore recursively the left child
                if key_lo < node.key:
                    yield from range(node.left, key_lo, key_hi, step)

                # The key of the current node falls within the specified range
                if key_lo <= node.key and key_hi > node.key:

                    # Filter out the keys that do not match the specified step value
                    if (node.key - key_lo) % step == 0:
                        yield node.key

                # Explore recursively the right child
                if key_hi > node.key:
                    yield from range(node.right, key_lo, key_hi, step)

            return range(self.__root, start, stop, step)

        # Case 3: Invalid argument
        else:
            raise TypeError("Invalid argument.")

    def __contains__(self: 'BST', key: int) -> bool:
        """
        Checks if a key is in the BST.

        Args:
            key (int): The key to check for.

        Returns:
            bool: True if the key is in the BST, False otherwise.
        """

        node = self.__root

        # Go through all the tree looking for the key
        while node:
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            elif key == node.key:
                return True
        return False

    def __delitem__(self: 'BST', key: int) -> None:
        """
        Deletes the node with the given key from the BST.

        Args:
            key (int): The key of the node to delete.

        Raises:
            IndexError: If the key is not found in the BST.
        """
        if not self.__contains__(key):
            raise IndexError
        self.__root = self._delete(self.__root, key)

    def _delete_min(self: 'BST', node: 'BST.TreeNode') -> 'BST.TreeNode':
        """
        Helper method to delete the minimum node in the subtree.

        Args:
            node (BST.TreeNode): The root of the subtree.

        Returns:
            BST.TreeNode: The root of the subtree after deletion.
        """

        # We have reached the minimum value in the left link,
        # replace with the right link
        if node.left is None:
            return node.right

        # Move recursively to the left to find the minimum value
        node.left = self._delete_min(node.left)

        # After the deletion, update the count
        node.count = self._size(node.left) + self._size(node.right) + 1

        # Update the path to the root
        return node

    def _delete(self: 'BST', node: 'BST.TreeNode', key: int) -> 'BST.TreeNode':
        """
        Helper method to delete a node with the given key from the BST.

        Args:
            node (BST.TreeNode): The root of the subtree.
            key (int): The key of the node to delete.

        Returns:
            BST.TreeNode: The root of the subtree after deletion.
        """

        # Key not found, return
        if node is None:
            return None

        # Search for the key
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)

        # The key has been located
        else:
            # Case 1: There is just one child on the left
            if node.right is None:
                # Replace current node for its left child
                return node.left

            # Case 2: There is just one child on the right
            if node.left is None:
                # Replace current node for its right child
                return node.right

            # Case 3: There are 2 children
            # Keep a copy of the deleted node, to restore the links
            deleted_node = node

            # Replace the deleted node with its sucessor,
            # the minimum value in the right subtree
            node = self._min(deleted_node.right)

            # Delete the node from the right subtree, fix the links, and update the right link
            node.right = self._delete_min(deleted_node.right)

            # Update the left link
            node.left = deleted_node.left

        # After the deletion, update the count
        node.count = self._size(node.left) + self._size(node.right) + 1

        # Update the links upstream
        return node

    def __iter__(self: 'BST') -> Iterator[Any]:
        """
        Returns an iterator for in-order traversal of the BST.

        Yields:
            Any: The values of the nodes ordered by their key.
        """
        def in_order(node: 'BST.TreeNode')-> Iterator[Any]:
            """
            Helper generator for in-order traversal.

            Args:
                node (BST.TreeNode): The root of the subtree.

            Yields:
                Any: The values of the nodes in in-order.
            """
            # We have reached the leaf node
            if node is None:
                return

            # Recursively go to the left
            yield from in_order(node.left)

            # Return the current node
            yield node.val

            # Recursively go to the right
            yield from in_order(node.right)

        # Call the nested function
        return in_order(self.__root)

    def __reversed__(self: 'BST') -> Iterator[Any]:
        """
        Returns an iterator for reverse in-order traversal of the BST.

        Yields:
            Any: The values of the nodes in reverse in-order.
        """
        def reversed_order(node: 'BST.TreeNode')-> Iterator[Any]:
            """
            Helper generator for reverse in-order traversal.

            Args:
                node (BST.TreeNode): The root of the subtree.

            Yields:
                Any: The values of the nodes in reverse in-order.
            """
            # We have reached the leaf node
            if node is None:
                return

            # Recursively go to the right
            yield from reversed_order(node.right)

            # Return the current node
            yield node.val

            # Recursively go to the left
            yield from reversed_order(node.left)

        # Call the nested function
        return reversed_order(self.__root)

    def __repr__(self: 'BST') -> str:
        """
        Returns a string representation of the BST.

        Returns:
            str: A string representation of the BST.
        """
        return f"BST({list(self.__iter__())})"

    def ceiling(self: 'BST', key: int) -> int:
        """
        Finds the smallest key in the BST that is greater than or equal to the given key.

        Args:
            key (int): The key to find the ceiling for.

        Returns:
            int: The ceiling key, or None if no ceiling exists.
        """
        # Calls the private method
        node = self._ceiling(self.__root, key)

        # It means that there is no ceiling for the given key
        if node is None:
            return None

        # The ceiling is found, return the key
        return node.key

    def _ceiling(self: 'BST', node: 'BST.TreeNode', key: int):
        """
        Helper method to find the ceiling node in the BST.

        Args:
            node (BST.TreeNode): The root of the subtree.
            key (int): The key to find the ceiling for.

        Returns:
            BST.TreeNode: The ceiling node, or None if no ceiling exists.
        """
        # We have reached the end of the path without finding the ceiling
        if node is None:
            return None

        # Case 1: The ceiling of key is key
        if key == node.key:
            return node

        # Case 2: The ceiling of key is in the right subtree
        if key > node.key:
            return self._ceiling(node.right, key)

        # Case 3: The ceiling of key is in the left subtree if there is any k >= key in left subtree;
        # otherwise it is the key in the root.
        left_subtree_floor = self._ceiling(node.left, key)

        if left_subtree_floor is not None:
            return left_subtree_floor
        else:
            return node

    def floor(self: 'BST', key: int) -> int:
        """
        Finds the largest key in the BST that is less than or equal to the given key.

        Args:
            key (int): The key to find the floor for.

        Returns:
            int: The floor key, or None if no floor exists.
        """
        # Calls the private method
        node = self._floor(self.__root, key)

        # It means that there is no floor for the given key
        if node is None:
            return None

        # The floor is found, return the key
        return node.key

    def _floor(self: 'BST', node: 'BST.TreeNode', key: int):
        """
        Helper method to find the floor node in the BST.

        Args:
            node (BST.TreeNode): The root of the subtree.
            key (int): The key to find the floor for.

        Returns:
            BST.TreeNode: The floor node, or None if no floor exists.
        """
        # We have reached the end of the path without finding the floor
        if node is None:
            return None

        # Case 1: The floor of key is key
        if key == node.key:
            return node

        # Case 2: The floor of key is in the left subtree
        if key < node.key:
            return self._floor(node.left, key)

        # Case 3: The floor of key is in the right subtree if there is any k <= key in right subtree;
        # otherwise it is the key in the root.

        right_subtree_floor = self._floor(node.right, key)

        if right_subtree_floor is not None:
            return right_subtree_floor
        else:
            return node

    def max(self: 'BST') -> int:
        """
        Finds the maximum key in the BST.

        Returns:
            int: The maximum key in the BST.
        """
        return self._max(self.__root).key

    def _max(self: 'BST', node: 'BST.TreeNode') -> 'BST.TreeNode':
        """
        Helper method to find the node with the maximum key in the BST.

        Args:
            node (BST.TreeNode): The root of the subtree.

        Returns:
            BST.TreeNode: The node with the maximum key.
        """
        # Recursively go to the right until the end
        if node.right is None:
            return node
        return self._max(node.right)

    def min(self: 'BST') -> int:
        """
        Finds the minimum key in the BST.

        Returns:
            int: The minimum key in the BST.
        """
        return self._min(self.__root).key

    def _min(self: 'BST', node: 'BST.TreeNode') -> 'BST.TreeNode':
        """
        Helper method to find the node with the minimum key in the BST.

        Args:
            node (BST.TreeNode): The root of the subtree.

        Returns:
            BST.TreeNode: The node with the minimum key.
        """
        # Recursively go to the left until the end
        if node.left is None:
            return node
        return self._min(node.left)

    def print_tree(self: 'BST') -> None:
        """
        Prints the BST in a structured format.
        """
        self._print_tree(self.__root)

    def _print_tree(self: 'BST', node: 'BST.TreeNode' = None, level: int = 0, prefix: str = "Root: ") -> None:
        """
        Helper method to print the BST in a structured format.

        Args:
            node (BST.TreeNode): The root of the subtree.
            level (int): The current level in the tree (used for indentation).
            prefix (str): The prefix to print before the node value.
        """
        if node is not None:
            print(f"{' ' * (level * 4)}{prefix} {node.val}")
            if node.left:
                self._print_tree(node.left, level + 1, "L-->")
            if node.right:
                self._print_tree(node.right, level + 1, "R-->")

    def rank(self: 'BST', key: int) -> int:
        """
        Returns the number of keys less than the given key in the BST.

        Args:
            key (int): The key to find the rank for.

        Returns:
            int: The number of keys less than the given key.
        """
        return self._rank(key, self.__root)

    def _rank(self: 'BST', key: int, node: 'BST.TreeNode') -> int:
        """
        Helper method to return the number of keys less than the given key in the subtree rooted at the given node.

        Args:
            key (int): The key to find the rank for.
            node (BST.TreeNode): The root of the subtree.

        Returns:
            int: The number of keys less than the given key in the subtree.
        """

        if node is None:
            # We have reached the leaf node, there are no more node to compare
            return 0

        if key < node.key:
            # Recursively go to the left subtree, because all the keys in the left
            # are less than the current node's key
            return self._rank(key, node.left)

        elif key > node.key:
            # We add 1 for the current node plus the size of the left subtree.
            # Recursively go to the right subtree.
            return 1 + self._size(node.left) + self._rank(key, node.right)

        elif key == node.key:
            # Returns the size of the left subtree, because all those keys are less
            # than the current node's key
            return self._size(node.left)