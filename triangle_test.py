"""Module for classifying triangles and testing with unittest."""

import unittest


def classify_triangle(a, b, c):
    """
    Classify a triangle given side lengths a, b, and c.

    Returns:
        str: One of the following:
            - "NotATriangle" if inputs don't form a valid triangle.
            - "Equilateral" if all sides are equal.
            - "Isosceles" if two sides are equal.
            - "Scalene" if all sides are different.
            - May append " Right" if the triangle is also right-angled.
    """
    # Check if the sides make a triangle
    if a + b <= c or a + c <= b or b + c <= a:
        return "NotATriangle"

    # Determine type
    if a == b == c:
        triangle_type = "Equilateral"
    elif a == b or b == c or a == c:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"

    # Check for right triangle
    sides = sorted([a, b, c])
    if abs(sides[0] ** 2 + sides[1] ** 2 - sides[2] ** 2) < 1e-6:
        triangle_type += " Right"

    return triangle_type


class TriangleTest(unittest.TestCase):
    """Unit tests for the classify_triangle function."""

    def test_equilateral(self):
        """Test if a triangle is equilateral."""
        self.assertEqual(classify_triangle(3, 3, 3), "Equilateral")

    def test_isosceles(self):
        """Test if a triangle is isosceles."""
        self.assertEqual(classify_triangle(5, 5, 3), "Isosceles")
        self.assertEqual(classify_triangle(5, 3, 5), "Isosceles")
        self.assertEqual(classify_triangle(3, 5, 5), "Isosceles")

    def test_scalene(self):
        """Test if a triangle is scalene."""
        self.assertEqual(classify_triangle(4, 5, 6), "Scalene")

    def test_right_triangle(self):
        """Test right triangles (scalene right, isosceles right)."""
        self.assertEqual(classify_triangle(3, 4, 5), "Scalene Right")
        self.assertEqual(classify_triangle(5, 12, 13), "Scalene Right")
        self.assertEqual(classify_triangle(1, 1, 2 ** 0.5), "Isosceles Right")

    def test_not_a_triangle(self):
        """Test invalid triangles that fail the triangle inequality."""
        self.assertEqual(classify_triangle(1, 2, 3), "NotATriangle")
        self.assertEqual(classify_triangle(0, 0, 0), "NotATriangle")
        self.assertEqual(classify_triangle(1, 10, 12), "NotATriangle")


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
