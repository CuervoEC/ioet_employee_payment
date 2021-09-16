from calculator.reader import read_file
import unittest


class LoaderTestClass(unittest.TestCase):

    def test_should_return_data_checking_type(self):
        self.assertTrue(type(read_file('test_data.txt')) == list)


if __name__ == '__main__':
    unittest.main()
