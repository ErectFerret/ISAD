import unittest
from main import identify_shape

class TestShapeIdentifier(unittest.TestCase):
    def test_triangle(self):
        self.assertEqual(identify_shape(3), "Triangle")

    def test_square(self):
        self.assertEqual(identify_shape(4), "Square")

    def test_pentagon(self):
        self.assertEqual(identify_shape(5), "Pentagon")

    def test_hexagon(self):
        self.assertEqual(identify_shape(6), "Hexagon")

    def test_heptagon(self):
        self.assertEqual(identify_shape(7), "Heptagon")

    def test_invalid_input(self):
        self.assertEqual(identify_shape(2), "Invalid input: Polygon must have at least 3 sides")

if __name__ == "__main__":
    unittest.main()
