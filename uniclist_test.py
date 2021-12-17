import unittest
from uniclist import get_uniclist

class Uniclist_test(unittest.TestCase):

    def setUp(self) -> None:
        self.unic_list = [1, 2, 3, 4, 5]
        self.notunic_list = [1, 2, 3, 3, 2]
        self.unic_answer = 'Все элементы уникальны'
        self.notunic_answer = 'Есть одинаковые'

    def test_extention(self):
        self.assertEqual(get_uniclist(self.unic_list), self.unic_answer)
        self.assertEqual(get_uniclist(self.notunic_list), self.notunic_answer)

if __name__ == '__main__':
    unittest.main()