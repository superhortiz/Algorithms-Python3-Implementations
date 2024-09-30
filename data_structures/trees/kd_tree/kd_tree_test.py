import unittest
import random
from data_structures import KdTree, Point2D, RectHV


class TestKdTree(unittest.TestCase):

    def setUp(self):
        """Set up common test variables."""
        self.kd_tree = KdTree()

    def test_insert_single_point(self):
        """Test inserting a single point."""
        self.kd_tree.insert(Point2D(0.5, 0.5))
        self.assertEqual(len(self.kd_tree), 1)

    def test_insert_multiple_points(self):
        """Test inserting multiple points."""
        points = [Point2D(0.5, 0.5), Point2D(0.2, 0.3), Point2D(0.8, 0.9)]
        for point in points:
            self.kd_tree.insert(point)
        self.assertEqual(len(self.kd_tree), len(points))

    def test_contains_existing_point(self):
        """Test checking if an existing point is in the tree."""
        point = Point2D(0.5, 0.5)
        self.kd_tree.insert(point)
        self.assertTrue(point in self.kd_tree)

    def test_contains_non_existing_point(self):
        """Test checking if a non-existing point is in the tree."""
        point = Point2D(0.5, 0.5)
        self.kd_tree.insert(point)
        self.assertFalse(Point2D(0.6, 0.6) in self.kd_tree)

    def test_range_search_empty_tree(self):
        """Test range search on an empty tree."""
        rect = RectHV(0.1, 0.1, 0.6, 0.6)
        points = self.kd_tree.range(rect)
        self.assertEqual(len(points), 0)

    def test_range_search_single_point(self):
        """Test range search with a single point in the tree."""
        point = Point2D(0.5, 0.5)
        self.kd_tree.insert(point)
        rect = RectHV(0.4, 0.4, 0.6, 0.6)
        points = self.kd_tree.range(rect)
        self.assertEqual(len(points), 1)

    def test_range_search_multiple_points(self):
        """Test range search with multiple points in the tree."""
        points = [Point2D(0.5, 0.5), Point2D(0.2, 0.3), Point2D(0.8, 0.9)]
        for point in points:
            self.kd_tree.insert(point)
        rect = RectHV(0.1, 0.1, 0.6, 0.6)
        found_points = self.kd_tree.range(rect)
        self.assertEqual(len(found_points), 2)

    def test_nearest_neighbor_empty_tree(self):
        """Test nearest neighbor search on an empty tree."""
        point = Point2D(0.5, 0.5)
        self.assertIsNone(self.kd_tree.nearest(point))

    def test_nearest_neighbor_single_point(self):
        """Test nearest neighbor search with a single point in the tree."""
        point = Point2D(0.5, 0.5)
        self.kd_tree.insert(point)
        query_point = Point2D(0.4, 0.4)
        nearest = self.kd_tree.nearest(query_point)
        self.assertEqual(nearest, point)

    def test_nearest_neighbor_multiple_points(self):
        """Test nearest neighbor search with multiple points in the tree."""
        points = [Point2D(0.5, 0.5), Point2D(0.2, 0.3), Point2D(0.8, 0.9)]
        for point in points:
            self.kd_tree.insert(point)
        query_point = Point2D(0.4, 0.4)
        nearest = self.kd_tree.nearest(query_point)
        self.assertIsNotNone(nearest)

    def test_large_random_insertions(self):
        """Test inserting a large number of random points."""
        num_points = 1000
        points = [Point2D(random.random(), random.random()) for _ in range(num_points)]
        for point in points:
            self.kd_tree.insert(point)
        self.assertEqual(len(self.kd_tree), num_points)

    def test_large_random_range_search(self):
        """Test range search with a large number of random points."""
        num_points = 1000
        points = [Point2D(random.random(), random.random()) for _ in range(num_points)]
        for point in points:
            self.kd_tree.insert(point)
        rect = RectHV(0.2, 0.2, 0.8, 0.8)
        found_points = self.kd_tree.range(rect)
        self.assertGreater(len(found_points), 0)

    def test_large_random_nearest_neighbor(self):
        """Test nearest neighbor search with a large number of random points."""
        num_points = 1000
        points = [Point2D(random.random(), random.random()) for _ in range(num_points)]
        for point in points:
            self.kd_tree.insert(point)
        query_point = Point2D(random.random(), random.random())
        nearest = self.kd_tree.nearest(query_point)
        self.assertIsNotNone(nearest)

    def test_distance_calculation(self):
        """Test distance calculation between two points."""
        point1 = Point2D(0.5, 0.5)
        point2 = Point2D(0.6, 0.6)
        self.assertAlmostEqual(point1.distance_squared_to(point2), 0.02)


if __name__ == '__main__':
    unittest.main()
