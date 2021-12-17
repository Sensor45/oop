import unittest
from lesson4 import Triangle


class TestTriangle(unittest.TestCase):

    def test_valid_values(self):
        triangle=Triangle(a=22, b=44, c=24, h=50)
        triangle_area =triangle.calc_area()
        self.assertEqual(triangle_area, 550)

    def test_negative_numbers(self):
        triangle = Triangle(a=-22, b=44, c=24, h=50)
        triangle_area = triangle.calc_area()

        self.assertEqual(triangle_area, 0.5)

if __name__ == '__main__':
    unittest.main()

