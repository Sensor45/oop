import unittest

from sumdigit import get_sum

class TestDirFiles(unittest.TestCase):
    def setUp(self) -> None:
        self.number = 35732
        self.answer = 20

    def test_dirfiles(self):
        self.assertEqual(get_sum(self.number), self.answer)

if __name__ == '__main__':
    unittest.main()