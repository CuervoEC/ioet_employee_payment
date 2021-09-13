from loader import loader
import unittest


class CalculatorTestClass(unittest.TestCase):

    def test_when_worked_weekday_schedule(self):
        self.assertTrue(type(loader('test_data.txt')) == list)


if __name__ == '__main__':
    unittest.main()
