import unittest
from extention2 import get_extention

class TestExtensions(unittest.TestCase):
    def setUp(self) -> None:
        self.succesful_data = ["help.docx", "koka.txt", "main.pdf", "test.txt", "test1.csv"]
        self.succesful = ['docx', 'txt', 'pdf', 'txt', 'csv']
        self.wrong_data = ["help.docx", "koka", "main.pdf", "test.txt", "test1.csv"]

    def test_succesful(self):
        self.assertEqual(get_extention(self.succesful_data), self.succesful)

    def test_wrong(self):
        with self.assertRaises(EOFError) as context:
            get_extention(self.wrong_data)


if __name__ == '__main__':
    unittest.main()