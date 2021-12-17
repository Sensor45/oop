import unittest
from Soda import Soda


class TestSoda(unittest.TestCase):

    def test_valid_no_tasty(self):
        self.soda = Soda('')
        self.assertEqual(self.soda.show_my_drink(), 'Обычная газировка')

    def test_valid_add_tasty(self):
        self.soda = Soda('клубника')
        self.assertEqual(self.soda.show_my_drink(), 'Газировка и клубника')

if __name__ == '__main__':
    unittest.main()
