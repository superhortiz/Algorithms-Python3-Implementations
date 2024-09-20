from matplotlib import pyplot as plt

class Point2D:
    """
    A class to represent a point in 2D space.
    
    Attributes:
        x (float): The x-coordinate of the point.
        y (float): The y-coordinate of the point.

    Methods:
        distance_squared_to(that): Calculate the squared Euclidean distance to another point.
        distance_to(that): Calculate the Euclidean distance to another point.
        draw(): Draws the point represented by this object on a matplotlib plot.

    Special Methods:
        __eq__(): Check if this point is equal to another point.
        __lt__(): Check if this point is less than another point.
        __repr__(): Return a string representation of the point.
        __str__(): Return a string representation of the point.
    """

    def __init__(self: 'Point2D', x: float, y: float) -> None:
        """
        Initialize the Point2D object with x and y coordinates.

        Args:
            x (float): The x-coordinate of the point.
            y (float): The y-coordinate of the point.

        Raises:
            ValueError: If x or y are not valid values.
        """
        if not isinstance(x, float) or not isinstance(y, float):
            raise ValueError("Coordinates must be numbers (float).")

        self.__x = x
        self.__y = y

    @property
    def x(self: 'Point2D') -> float:
        """
        Get the x-coordinate of the point.

        Returns:
            float: The x-coordinate of the point.
        """
        return self.__x

    @property
    def y(self: 'Point2D') -> float:
        """
        Get the y-coordinate of the point.

        Returns:
            float: The y-coordinate of the point.
        """
        return self.__y

    def distance_to(self: 'Point2D', that: 'Point2D') -> float:
        """
        Calculate the Euclidean distance to another point.

        Args:
            that (Point2D): Another point to which the distance is calculated.

        Returns:
            float: The Euclidean distance to the other point.

        Raises:
            ValueError: If 'that' is not a Point2D object.
        """
        if not isinstance(that, Point2D):
            raise ValueError("Argument must be a Point2D object.")

        return self.distance_squared_to(that) ** 0.5

    def distance_squared_to(self: 'Point2D', that: 'Point2D') -> float:
        """
        Calculate the squared Euclidean distance to another point.

        Args:
            that (Point2D): Another point to which the squared distance is calculated.

        Returns:
            float: The squared Euclidean distance to the other point.

        Raises:
            ValueError: If 'that' is not a Point2D object.
        """
        if not isinstance(that, Point2D):
            raise ValueError("Argument must be a Point2D object.")

        return (self.x - that.x) ** 2 + (self.y - that.y) ** 2

    def draw(self: 'Point2D') -> None:
        """
        Draws the point represented by this object on a matplotlib plot.
        The point is plotted as a black circle.
        """
        plt.plot(self.x, self.y, 'o', color = 'black')

    def __eq__(self: 'Point2D', that: 'Point2D') -> bool:
        """
        Check if this point is equal to another point.

        Args:
            that (Point2D): Another point to compare with.

        Returns:
            bool: True if the points are equal, False otherwise.

        Raises:
            ValueError: If 'that' is not a Point2D object.
        """
        if not isinstance(that, Point2D):
            raise ValueError("Argument must be a Point2D object.")

        return self.x == that.x and self.y == that.y

    def __lt__(self: 'Point2D', that: 'Point2D') -> bool:
        """
        Check if this point is less than another point.

        Args:
            that (Point2D): Another point to compare with.

        Returns:
            bool: True if this point is less than the other point, False otherwise.

        Raises:
            ValueError: If 'that' is not a Point2D object.
        """
        if not isinstance(that, Point2D):
            raise ValueError("Argument must be a Point2D object.")

        if self.x != that.x:
            return self.x < that.x

        return self.y < that.y

    def __repr__(self: 'Point2D') -> str:
        """
        Return a string representation of the point.

        Returns:
            str: A string representation of the point in the format Point2D(x, y).
        """
        return f"{__class__.__name__}({self.x}, {self.y})"

    def __str__(self: 'Point2D') -> str:
        """
        Return a string representation of the point.

        Returns:
            str: A string representation of the point in the format (x, y).
        """
        return f"({self.x}, {self.y})"


class RectHV:
    """
    Represents a 2D axis-aligned rectangle with coordinates (xmin, ymin) and (xmax, ymax).

    Attributes:
        xmin (float): The minimum x-coordinate.
        ymin (float): The minimum y-coordinate.
        xmax (float): The maximum x-coordinate.
        ymax (float): The maximum y-coordinate.

    Methods:
        contains(point): Checks if the rectangle contains a given point.
        distance_squared_to(point): Computes the square of the Euclidean distance from the rectangle to a point.
        distance_to(point): Computes the Euclidean distance from the rectangle to a point.
        draw(): Draws the rectangle represented by this object on a matplotlib plot.
        intersects(that): Checks if the rectangle intersects with another rectangle.

    Special Methods:
        __eq__(that): Checks if this rectangle is equal to another rectangle.
        __repr__(): Returns a string representation of the rectangle.
        __str__(): Returns a string representation of the rectangle.
    """

    def __init__(self: 'RectHV', xmin: float, ymin: float, xmax: float, ymax: float) -> None:
        """
        Initializes a new rectangle with the specified coordinates.
        
        Args:
            xmin (float): The minimum x-coordinate.
            ymin (float): The minimum y-coordinate.
            xmax (float): The maximum x-coordinate.
            ymax (float): The maximum y-coordinate.
        
        Raises:
            ValueError: If x or y are not valid values.
            ValueError: If xmax < xmin or ymax < ymin.
        """
        if not isinstance(xmin, float) or not isinstance(ymin, float) or not isinstance(xmax, float) or not isinstance(ymax, float):
            raise ValueError("Coordinates must be numbers (float).")

        if xmax < xmin or ymax < ymin:
            raise ValueError("Invalid arguments: xmax must be >= xmin and ymax must be >= ymin.")

        self.__xmin = xmin
        self.__ymin = ymin
        self.__xmax = xmax
        self.__ymax = ymax

    @property
    def xmin(self: 'RectHV') -> float:
        """
        Returns the minimum x-coordinate of the rectangle.
        
        Returns:
            float: The minimum x-coordinate.
        """
        return self.__xmin

    @property
    def ymin(self: 'RectHV') -> float:
        """
        Returns the minimum y-coordinate of the rectangle.
        
        Returns:
            float: The minimum y-coordinate.
        """
        return self.__ymin

    @property
    def xmax(self: 'RectHV') -> float:
        """
        Returns the maximum x-coordinate of the rectangle.
        
        Returns:
            float: The maximum x-coordinate.
        """
        return self.__xmax

    @property
    def ymax(self: 'RectHV') -> float:
        """
        Returns the maximum y-coordinate of the rectangle.
        
        Returns:
            float: The maximum y-coordinate.
        """
        return self.__ymax

    def contains(self: 'RectHV', point: 'Point2D') -> bool:
        """
        Checks if the rectangle contains a given point.
        
        Args:
            point (Point2D): The point to check.
        
        Returns:
            bool: True if the rectangle contains the point, False otherwise.

        Raises:
            ValueError: If 'point' is not a Point2D object.
        """
        if not isinstance(point, Point2D):
            raise ValueError("Argument must be a Point2D object.")

        return self.xmin <= point.x <= self.xmax and self.ymin <= point.y <= self.ymax

    def intersects(self: 'RectHV', that: 'RectHV') -> bool:
        """
        Checks if the rectangle intersects with another rectangle.
        
        Args:
            that (RectHV): The other rectangle to check.
        
        Returns:
            bool: True if the rectangles intersect, False otherwise.

        Raises:
            ValueError: If 'that' is not a RectHV object.
        """
        if not isinstance(that, RectHV):
            raise ValueError("Argument must be a RectHV object.")

        return self.xmax >= that.xmin and self.xmin <= that.xmax and self.ymax >= that.ymin and self.ymin <= that.ymax

    def distance_to(self: 'RectHV', point: 'Point2D') -> float:
        """
        Computes the Euclidean distance from the rectangle to a point.
        
        Args:
            point (Point2D): The point to compute the distance to.
        
        Returns:
            float: The Euclidean distance to the point.

        Raises:
            ValueError: If 'point' is not a Point2D object.
        """
        if not isinstance(point, Point2D):
            raise ValueError("Argument must be a Point2D object.")

        return self.distance_squared_to(point) ** 0.5

    def distance_squared_to(self: 'RectHV', point: 'Point2D') -> float:
        """
        Computes the square of the Euclidean distance from the rectangle to a point.
        
        Args:
            point (Point2D): The point to compute the distance to.
        
        Returns:
            float: The square of the Euclidean distance to the point.

        Raises:
            ValueError: If 'point' is not a Point2D object.
        """
        if not isinstance(point, Point2D):
            raise ValueError("Argument must be a Point2D object.")

        dx, dy = 0, 0

        if point.x > self.xmax:
            dx = point.x - self.xmax
        elif point.x < self.xmin:
            dx = self.xmin - point.x
        if point.y > self.ymax:
            dy = point.y - self.ymax
        elif point.y < self.ymin:
            dy = self.ymin - point.y

        return dx ** 2 + dy ** 2

    def draw(self: 'RectHV') -> None:
        """
        Draws the rectangle represented by this object on a matplotlib plot.
        The rectangle is plotted using green lines.
        """
        x = [self.xmin, self.xmax, self.xmax, self.xmin, self.xmin]
        y = [self.ymin, self.ymin, self.ymax, self.ymax, self.ymin]

        plt.plot(x, y, 'g-')

    def __eq__(self: 'RectHV', that: 'RectHV') -> bool:
        """
        Checks if this rectangle is equal to another rectangle.
        
        Args:
            that (RectHV): The other rectangle to compare.
        
        Returns:
            bool: True if the rectangles are equal, False otherwise.

        Raises:
            ValueError: If 'that' is not a RectHV object.
        """
        if not isinstance(that, RectHV):
            raise ValueError("Argument must be a RectHV object.")

        return self.xmin == that.xmin and self.xmax == that.xmax and self.ymin == that.ymin and self.ymax == that.ymax

    def __repr__(self: 'RectHV') -> str:
        """
        Returns a string representation of the rectangle.

        Returns:
            str: The string representation of the rectangle.
        """
        return f"{__class__.__name__}({self.xmin}, {self.xmax}, {self.ymin}, {self.ymax})"

    def __str__(self: 'RectHV') -> str:
        """
        Returns a string representation of the rectangle.

        Returns:
            str: The string representation of the rectangle.
        """
        return f"[{self.xmin}, {self.xmax}] x [{self.ymin}, {self.ymax}]"


class KdTree:
    """
    A class representing a 2-dimensional k-d tree (KdTree) for organizing points in a 2D space.

    Expected Performance:
        Insertion: O(log N) on average, where N is the number of points, assuming the tree is balanced.
        Contains: O(log N) on average, due to the binary search nature of the tree.
        Nearest Neighbor Search:
            - Typical case: O(log N).
            - Worst case (even if the tree is balanced): O(N).
        Range Search:
            - Typical case: O(R + log N), where R is the number of points in the range.
            - Worst case (assuming the tree is balanced): O(R + √N).

    Attributes:
        size (int): The number of nodes in the 2D KdTree.

    Methods:
        contains(point): Checks if a point exists in the 2D KdTree.
        draw(): Draw the 2D KdTree.
        insert(point): Inserts a new point into the 2D KdTree.
        is_empty(): Checks if the 2D KdTree is empty.
        nearest(point): Finds the nearest neighbor to a given point in the 2D KdTree.
        print_tree(): Print the 2D KdTree in a structured format.
        range(rect): Finds all points in the 2D KdTree that lie within a given rectangle.
    """

    # The searching space represents the rectangular bounds within which points are searched.
    SEARCHING_SPACE = RectHV(0., 0., 1., 1.)

    class TreeNode:
        """
        A class representing a node in the 2D KdTree.

        Attributes:
            count (int): The size of the subtree rooted at this node.
            left (TreeNode): The left child of this node.
            right (TreeNode): The right child of this node.
            point (Point2D): The 2-dimensional point stored in this node.
        """
        
        def __init__(self, point: 'Point2D', count: int) -> None:
            """
            Initialize a TreeNode.

            Args:
                point (Point2D): The 2-dimensional point stored in this node.
                count (int): The size of the subtree rooted at this node.
            """
            self.count = count
            self.left = None
            self.right = None
            self.point = point

    def __init__(self: 'KdTree') -> None:
        """
        Initialize an empty 2D KdTree.
        """
        self.__root = None

    @property
    def size(self: 'KdTree') -> int:
        """
        Get the number of nodes in the 2D KdTree.

        Returns:
            int: The total number of nodes in the tree.
        """
        return self.__size(self.__root)

    def __size(self: 'KdTree', x: TreeNode) -> int:
        """
        Gets the number of nodes in the 2D KdTree.

        Returns:
            int: The total number of nodes in the tree.
        """
        if x is None:
            return 0

        return x.count

    def is_empty(self: 'KdTree') -> bool:
        """
        Checks if the 2D KdTree is empty.

        Returns:
            bool: True if the tree is empty, False otherwise.
        """
        return self.__root is None

    def insert(self: 'KdTree', point: Point2D) -> None:
        """
        Inserts a new point into the 2D KdTree.

        Args:
            point (Point2D): The 2-dimensional point to be inserted.

        Raises:
            ValueError: If 'point' is not a Point2D object.
        """
        if not isinstance(point, Point2D):
            raise ValueError("Argument must be a Point2D object.")

        self.__root = self.__insert(self.__root, point, level = 0)

    def __insert(self: 'KdTree', node: TreeNode, newPoint: Point2D, level: int) -> TreeNode:
        """
        Recursively inserts a new point into the subtree rooted at the given node.

        Args:
            node (TreeNode): The root of the subtree.
            newPoint (Point2D): The 2-dimensional point to be inserted.
            level (int): The current level in the tree.

        Returns:
            TreeNode: The updated subtree root.
        """
        if node is None:
            return self.TreeNode(newPoint, 1)

        if level % 2 == 0:
            key = newPoint.x
            keyNode = node.point.x
            secondKey = newPoint.y
            secondKeyNode = node.point.y

        else:
            key = newPoint.y
            keyNode = node.point.y
            secondKey = newPoint.x
            secondKeyNode = node.point.x

        if key < keyNode or (key == keyNode and secondKey != secondKeyNode):
            node.left = self.__insert(node.left, newPoint, level + 1)
        elif key > keyNode:
            node.right = self.__insert(node.right, newPoint, level + 1)
        elif key == keyNode and secondKey == secondKeyNode:
            node.point = point

        node.count = 1 + self.__size(node.left) + self.__size(node.right)
        return node

    def contains(self: 'KdTree', point: Point2D) -> bool:
        """
        Checks if a point exists in the 2D KdTree.

        Args:
            point (Point2D): The 2-dimensional point to be checked.

        Returns:
            bool: True if the point exists in the tree, False otherwise.

        Raises:
            ValueError: If 'point' is not a Point2D object.
        """
        if not isinstance(point, Point2D):
            raise ValueError("Argument must be a Point2D object.")

        return not self.__get(point) is None

    def __get(self: 'KdTree', point: Point2D) -> Point2D:
        """
        Retrieves a point from the 2D KdTree.

        Args:
            point (Point2D): The 2-dimensional point to be retrieved.

        Returns:
            Point2D: The point if found, None otherwise.
        """
        node = self.__root
        level = 0

        while node:
            if level % 2 == 0:
                key = point.x
                keyNode = node.point.x
                secondKey = point.y
                secondKeyNode = node.point.y
            else:
                key = point.y
                keyNode = node.point.y
                secondKey = point.x
                secondKeyNode = node.point.x

            if key < keyNode or (key == keyNode and secondKey != secondKeyNode):
                node = node.left
            elif key > keyNode:
                node = node.right
            elif key == keyNode and secondKey == secondKeyNode:
                return node.point
            level += 1

        return None

    def draw(self: 'KdTree') -> None:
        """
        Draws the 2D KdTree.

        Sets up the plot limits and initiates the recursive drawing process.
        """
        plt.xlim(0, 1)
        plt.ylim(0, 1)
        self.__draw(self.__root, 0, KdTree.SEARCHING_SPACE)
        plt.show()

    def __draw(self: 'KdTree', node: TreeNode, level: int, curr: RectHV) -> None:
        """
        Recursively draws the 2D KdTree.

        Args:
            node (TreeNode): The current node in the tree.
            level (int): The current level in the tree.
            curr (RectHV): The current rectangle representing the node's region.
        """
        if node is None:
            return

        node.point.draw()
        x, y = node.point.x, node.point.y

        if level % 2 == 0:
            curr_left = RectHV(curr.xmin, curr.ymin, x, curr.ymax)
            curr_right = RectHV(x, curr.ymin, curr.xmax, curr.ymax)
            plt.plot([x, x], [curr.ymin, curr.ymax], 'r-')

        else:
            curr_left = RectHV(curr.xmin, curr.ymin, curr.xmax, y)
            curr_right = RectHV(curr.xmin, y, curr.xmax, curr.ymax)
            plt.plot([curr.xmin, curr.xmax], [y, y], 'b-')

        self.__draw(node.left, level + 1, curr_left)
        self.__draw(node.right, level + 1, curr_right)

    def range(self: 'KdTree', rect: RectHV) -> list:
        """
        Finds all points in the 2D KdTree that lie within a given rectangle.

        Args:
            rect (RectHV): The rectangle to search within.

        Returns:
            list: A list of points within the given rectangle.

        Raises:
            ValueError: If 'that' is not a RectHV object.
        """
        if not isinstance(rect, RectHV):
            raise ValueError("Argument must be a RectHV object.")

        inside_rec = []
        self.__range(self.__root, rect, inside_rec, 0, KdTree.SEARCHING_SPACE)
        return inside_rec

    def __range(self: 'KdTree', node: TreeNode, rect: RectHV, inside_rec: list, level: int, curr: RectHV) -> None:
        """
        Recursively finds all points in the subtree rooted at the given node that lie within a given rectangle.

        Args:
            node (TreeNode): The current node in the tree.
            rect (RectHV): The rectangle to search within.
            inside_rec (list): The list to store points found within the rectangle.
            level (int): The current level in the tree.
            curr (RectHV): The current rectangle representing the node's region.

        Note:
            It modifies the list 'inside_rec'.
        """
        if node is None:
            return

        if rect.contains(node.point):
            inside_rec.append(node.point)

        x, y = node.point.x, node.point.y

        if level % 2 == 0:
            curr_left = RectHV(curr.xmin, curr.ymin, x, curr.ymax)
            curr_right = RectHV(x, curr.ymin, curr.xmax, curr.ymax)

        else:
            curr_left = RectHV(curr.xmin, curr.ymin, curr.xmax, y)
            curr_right = RectHV(curr.xmin, y, curr.xmax, curr.ymax)

        if rect.intersects(curr_left):
            self.__range(node.left, rect, inside_rec, level + 1, curr_left)
        
        if rect.intersects(curr_right):
            self.__range(node.right, rect, inside_rec, level + 1, curr_right)

    def nearest(self: 'KdTree', point: Point2D) -> Point2D:
        """
        Finds the nearest neighbor to a given point in the 2D KdTree.

        Args:
            point (Point2D): The 2-dimensional point to find the nearest neighbor for.

        Returns:
            Point2D: The nearest point in the tree to the given point.

        Raises:
            ValueError: If 'point' is not a Point2D object.
        """
        if not isinstance(point, Point2D):
            raise ValueError("Argument must be a Point2D object.")

        if self.is_empty():
            return None

        champion = [self.__root.point]
        self.__nearest(self.__root, point, 0, KdTree.SEARCHING_SPACE, champion)
        return champion[0]

    def __nearest(self: 'KdTree', node: TreeNode, p: Point2D, level: int, curr: RectHV, champion: list) -> None:
        """
        Recursively finds the nearest neighbor to a given point in the subtree rooted at the given node.

        Args:
            node (TreeNode): The current node in the tree.
            p (Point2D): The point to find the nearest neighbor for.
            level (int): The current level in the tree.
            curr (RectHV): The current rectangle representing the node's region.
            champion (list): A list containing the current nearest point.

        Note:
            It modifies the list 'champion'.
        """
        if node is None or champion[0].distance_squared_to(p) < curr.distance_squared_to(p):
            return  # Prune strategy

        if p.distance_squared_to(node.point) < p.distance_squared_to(champion[0]):
            champion[0] = node.point

        x, y = node.point.x, node.point.y

        if level % 2 == 0:
            curr_left = RectHV(curr.xmin, curr.ymin, x, curr.ymax)
            curr_right = RectHV(x, curr.ymin, curr.xmax, curr.ymax)

        else:
            curr_left = RectHV(curr.xmin, curr.ymin, curr.xmax, y)
            curr_right = RectHV(curr.xmin, y, curr.xmax, curr.ymax)

        go_left = False

        if curr_left.contains(p):
            go_left = True
        elif curr_right.contains(p):
            go_left = False
        elif curr_left.distance_squared_to(p) < curr_right.distance_squared_to(p):
            go_left = True
        else:
            go_left = False

        if go_left:
            self.__nearest(node.left, p, level + 1, curr_left, champion)
            self.__nearest(node.right, p, level + 1, curr_right, champion)

        else:
            self.__nearest(node.right, p, level + 1, curr_right, champion)
            self.__nearest(node.left, p, level + 1, curr_left, champion)

    def print_tree(self: 'KdTree') -> None:
        """
        Prints the 2D KdTree in a structured format.
        """
        self.__print_tree(self.__root)

    def __print_tree(self: 'KdTree', node: TreeNode = None, level: int = 0, prefix: str = "Root: ") -> None:
        """
        Recursively prints the 2D KdTree in a structured format.

        Args:
            node (TreeNode): The current node in the tree.
            level (int): The current level in the tree.
            prefix (str): The prefix to print before the node's point.
        """
        if node is not None:
            print(" " * (level * 4) + prefix + f"({node.point})")
            if node.left:
                self.__print_tree(node.left, level + 1, "L--- ")
            if node.right:
                self.__print_tree(node.right, level + 1, "R--- ")
