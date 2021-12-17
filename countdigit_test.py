import unittest

from countdigit import count_digit

class Countdigit_test(unittest.TestCase):

    def setUp(self) -> None:
        self.num_list = [1, 1, 3, 2, 1, 3, 4]
        self.answer = {1:3, 2:1, 3:2, 4:1}

    def test_countdigit(self):

        self.assertEqual(count_digit(self.num_list), self.answer)

if __name__ == '__main__':
    unittest.main()
