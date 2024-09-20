import random
from matplotlib import pyplot as plt
from .kd_tree import KdTree, Point2D, RectHV


def demo() -> None:
    """
    Example usage of KdTree class.
    """

    help(KdTree)

    # Create an instance of KdTree
    kdt = KdTree()

    # Insert points
    points = [
    Point2D(0.1, 0.3), Point2D(0.5, 0.6), Point2D(0.8, 0.9), Point2D(0.4, 0.2),
    Point2D(0.1, 0.4), Point2D(0.7, 0.4), Point2D(0.3, 0.8), Point2D(0.6, 0.1),
    Point2D(0.9, 0.7), Point2D(0.2, 0.5), Point2D(0.5, 0.3), Point2D(0.8, 0.2)]

    for point in points:
        kdt.insert(point)

    # Check number of elements in the tree
    print("Number of elements in the tree = ", kdt.size)

    # Check if the tree contains a point
    p = Point2D(0.7, 0.2)
    print(f"Does the tree countain the point {p}? {kdt.contains(p)}")

    # Check nearest point
    point = Point2D(0.3, 0.35)
    print(f"Closest point to {point}: {kdt.nearest(point)}")

    # Check points inside a rectangle
    rect = RectHV(0.15, 0.15, 0.75, 0.75)
    pointsInRect = kdt.range(rect)
    print("Points inside the rectangle:", *[p for p in sorted(pointsInRect)])

    # Print a scheme of the tree
    kdt.print_tree()

    # Draw the elements
    rect.draw()
    plt.plot(point.x, point.y, 'x', color = 'red')
    kdt.draw()


if __name__ == "__main__":
    demo()