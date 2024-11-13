import unittest
import math
from functions import *

class TestGeometryFunctions(unittest.TestCase):

    def test_AreaCircle(self):
        self.assertAlmostEqual(AreaCircle(6), 113.0973, places=4)
        self.assertAlmostEqual(AreaCircle(1), math.pi, places=4)

    def test_PerimeterCircle(self):
        self.assertAlmostEqual(PerimeterCircle(6), 37.6991, places=4)
        self.assertAlmostEqual(PerimeterCircle(1), 2 * math.pi, places=4)

    def test_AreaRectangle(self):
        self.assertEqual(AreaRectangle(5, 10), 50)
        self.assertEqual(AreaRectangle(7, 3), 21)

    def test_PerimeterRectangle(self):
        self.assertEqual(PerimeterRectangle(5, 10), 30)
        self.assertEqual(PerimeterRectangle(7, 3), 20)

    def test_AreaTriangle(self):
        self.assertEqual(AreaTriangle(5, 4), 10)
        self.assertEqual(AreaTriangle(7, 3), 10.5)

    def test_PerimeterTriangle(self):
        self.assertEqual(PerimeterTriangle(7, 7, 7), 21)
        self.assertEqual(PerimeterTriangle(3, 4, 5), 12)

    def test_AreaSquare(self):
        self.assertEqual(AreaSquare(5), 25)
        self.assertEqual(AreaSquare(10), 100)

    def test_PerimeterSquare(self):
        self.assertEqual(PerimeterSquare(5), 20)
        self.assertEqual(PerimeterSquare(10), 40)

    
    
    
    def test_AreaCircle_zero(self):
        with self.assertRaises(ValueError):
            AreaCircle(0)

    def test_PerimeterCircle_zero(self):
        with self.assertRaises(ValueError):
            PerimeterCircle(0)

    def test_AreaRectangle_zero(self):
        with self.assertRaises(ValueError):
            AreaRectangle(0, 10)
            AreaRectangle(5, 0)

    def test_PerimeterRectangle_zero(self):
        with self.assertRaises(ValueError):
            PerimeterRectangle(0, 10)
            PerimeterRectangle(10, 0)

    def test_AreaTriangle_zero(self):
        with self.assertRaises(ValueError):
            AreaTriangle(0, 4)
            AreaTriangle(5, 0)

    def test_PerimeterTriangle_zero(self):
        with self.assertRaises(ValueError):
            PerimeterTriangle(0, 7, 7)
            PerimeterTriangle(7, 0, 7)
            PerimeterTriangle(7, 7, 0)

    def test_AreaSquare_zero(self):
        with self.assertRaises(ValueError):
            AreaSquare(0)

    def test_PerimeterSquare_zero(self):
        with self.assertRaises(ValueError):
            PerimeterSquare(0)

    
    
    
    
    def test_AreaCircle_negative(self):
        with self.assertRaises(ValueError):
            AreaCircle(-5)

    def test_AreaCircle_string(self):
        with self.assertRaises(ValueError):
            AreaCircle("a")

    def test_PerimeterCircle_negative(self):
        with self.assertRaises(ValueError):
            PerimeterCircle(-5)

    def test_PerimeterCircle_string(self):
        with self.assertRaises(ValueError):
            PerimeterCircle("a")

    def test_AreaRectangle_negative(self):
        with self.assertRaises(ValueError):
            AreaRectangle(-5, 10)
            AreaRectangle(5, -10)

    def test_AreaRectangle_string(self):
        with self.assertRaises(ValueError):
            AreaRectangle("a", 10)
            AreaRectangle(5, "a")

    def test_PerimeterRectangle_negative(self):
        with self.assertRaises(ValueError):
            PerimeterRectangle(-5, 10)
            PerimeterRectangle(10, -5)

    def test_AreaTriangle_negative(self):
        with self.assertRaises(ValueError):
            AreaTriangle(5, -10)
            AreaTriangle(-10, 5)

    def test_PerimeterTriangle_negative(self):
        with self.assertRaises(ValueError):
            PerimeterTriangle(7, -7, 7)
            PerimeterTriangle(-7, 7, 7)
            PerimeterTriangle(7, 7, -7)

    def test_PerimeterTriangle_string(self):
        with self.assertRaises(ValueError):
            PerimeterTriangle("a", -7, 7)
            PerimeterTriangle(-7, "a", 7)
            PerimeterTriangle(7, 7, "a")

    def test_AreaSquare_negative(self):
        with self.assertRaises(ValueError):
            AreaSquare(-5)

    def test_AreaSquare_string(self):
        with self.assertRaises(ValueError):
            AreaSquare("a")

    def test_PerimeterSquare_negative(self):
        with self.assertRaises(ValueError):
            PerimeterSquare(-5)

    def test_PerimeterSquare_string(self):
        with self.assertRaises(ValueError):
            PerimeterSquare("a")

if __name__ == '__main__':
    unittest.main()
