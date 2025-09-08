import unittest

# Classify a triangle
def classify_triangle(a, b, c):
    
    # Checking is the sides make a triangle
    if a + b <= c or a + c <= b or b + c <= a:
        return "NotATriangle"

    # Determining if the triangle is a equilateral, isosceles, or scalene triangle
    if a == b == c:
        triangle_type = "Equilateral"  
    elif a == b or b == c or a == c:
        triangle_type = "Isosceles"    
    else:
        triangle_type = "Scalene"    

    # Determine if the traingle is a right traingle
    sides = sorted([a, b, c]) 
    if abs(sides[0]**2 + sides[1]**2 - sides[2]**2) < 1e-6:
        triangle_type += " Right"  

    return triangle_type


class TriangleTest(unittest.TestCase):

    # Testing if equilateral triangle
    def test_equilateral(self):
        self.assertEqual(classify_triangle(3, 3, 3), "Equilateral")

    # Test if isosceles triangle
    def test_isosceles(self):
        self.assertEqual(classify_triangle(5, 5, 3), "Isosceles")
        self.assertEqual(classify_triangle(5, 3, 5), "Isosceles")
        self.assertEqual(classify_triangle(3, 5, 5), "Isosceles")

    # Test if scalene triangle
    def test_scalene(self):
        self.assertEqual(classify_triangle(4, 5, 6), "Scalene")

    # Test if right triangle (Scalene Right or Isosceles Right)
    def test_right_triangle(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Scalene Right")
        self.assertEqual(classify_triangle(5, 12, 13), "Scalene Right")
        self.assertEqual(classify_triangle(1, 1, 2**0.5), "Isosceles Right")

    # Test invalid triangles that do not satisfy triangle inequality
    def test_not_a_triangle(self):
        self.assertEqual(classify_triangle(1, 2, 3), "NotATriangle")
        self.assertEqual(classify_triangle(0, 0, 0), "NotATriangle")
        self.assertEqual(classify_triangle(1, 10, 12), "NotATriangle")

#Running test
if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)



