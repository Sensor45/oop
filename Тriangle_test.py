import unittest
from Triangle import TriangleChecker

class TriangleChecker_test(unittest.TestCase):

    def test_valid_positive(self):
        triangle1 = TriangleChecker(5, 5, 5)
        self.assertEqual(triangle1.is_triangle(), "Ура, можно построить треугольник!")

    def test_str(self):
        triangle3 = TriangleChecker(a='r', b='r', c='t')
        self.assertEqual(triangle3.is_triangle(), "Нужно вводить только числа!")

    def test_valid_negative(self):
        triangle2 = TriangleChecker(a=-5, b=-5, c=-5)
        self.assertEqual(triangle2.is_triangle(), "С отрицательными числами ничего не выйдет!")

    def test_valid_values(self):
        triangle4 = TriangleChecker(a=5, b=200, c=5)
        self.assertEqual(triangle4.is_triangle(), "Жаль, но из этого треугольник не сделать")

if __name__ == '__main__':
    unittest.main()

