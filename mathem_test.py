import unittest
from mathem import Mathem


class Mathem_test(unittest.TestCase):

    def test_addition(self):
        mathem = Mathem(10, 2)
        self.assertEqual(mathem.addition(), 12)

    def test_substruction(self):
        mathem = Mathem(10, 2)
        self.assertEqual(mathem.substruction(), 8)

    def test_multiplication(self):
        mathem = Mathem(10, 2)
        self.assertEqual(mathem.multiplication(), 20)

    def test_division(self):
        mathem = Mathem(10, 2)
        self.assertEqual(mathem.division(), 5.0)


if __name__ == '__main__':
    unittest.main()
