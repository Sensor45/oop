import unittest
from velocity import calculate_average_velocity

class velocity_test(unittest.TestCase):

    def setUp(self) -> None:
        self.answer = 250.0

    def test_velocity(self):
        self.assertEqual(calculate_average_velocity(100, 200, 300, 400), self.answer)
        self.assertEqual(calculate_average_velocity(100, 200, 300, 400, '222', '3333'), self.answer)

if __name__ == '__main__':
    unittest.main()