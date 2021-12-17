import unittest
import os
from extention import get_extention

class Extention_test(unittest.TestCase):

    def setUp(self) -> None:
        self.dir = os.walk('C:/Users/User/OneDrive/Desktop/oop/test/')
        self.answer = {'dict.csv': 'csv', 'dict.xlsx': 'xlsx', 'Задачи.png': 'png'}

    def test_extention(self):
        self.assertEqual(get_extention(self.dir), self.answer)

if __name__ == '__main__':
    unittest.main()
