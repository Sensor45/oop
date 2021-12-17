import unittest
import os
from dirfiles import get_dirfiles

class TestDirFiles(unittest.TestCase):
    def setUp(self) -> None:
        self.dir = os.walk('C:/Users/User/OneDrive/Desktop/oop/test/')
        self.answer = ['dict.csv', 'dict.xlsx', 'Задачи.png']

    def test_dirfiles(self):
        self.assertEqual(get_dirfiles(self.dir), self.answer)

if __name__ == '__main__':
    unittest.main()