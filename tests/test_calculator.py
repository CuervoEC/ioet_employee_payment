import unittest
from calculator.calc import calculate_salary


class CalculatorTestClass(unittest.TestCase):
    def setUp(self):
        # 'MO10:00-12:00,TH12:00-14:00,SU20:00-21:00'
        self.schedule = [
            ['MONDAY', (600, 720)],
            ['THURSDAY', (720, 840)],
            ['SUNDAY', (1200, 1260)]
        ]

    def test_should_calculate_salary_when_worked_weekday_schedule(self):
        self.assertEqual(91.67, calculate_salary([['MONDAY', (100, 320)]]))
        self.assertEqual(228.33, calculate_salary([['TUESDAY', (100, 720)]]))
        self.assertEqual(391.67, calculate_salary([['TUESDAY', (100, 1300)]]))
        self.assertEqual(100, calculate_salary([['THURSDAY', (600, 1000)]]))
        self.assertEqual(226.67, calculate_salary([['THURSDAY', (600, 1400)]]))
        self.assertEqual(100, calculate_salary([['THURSDAY', (1100, 1400)]]))

    def test_should_calculate_salary_when_worked_weekend_schedule(self):
        self.assertEqual(110, calculate_salary([['SATURDAY', (100, 320)]]))
        self.assertEqual(280, calculate_salary([['SATURDAY', (100, 720)]]))
        self.assertEqual(491.67, calculate_salary([['SATURDAY', (100, 1300)]]))
        self.assertEqual(133.33, calculate_salary([['SUNDAY', (600, 1000)]]))
        self.assertEqual(293.33, calculate_salary([['SUNDAY', (600, 1400)]]))
        self.assertEqual(125, calculate_salary([['SUNDAY', (1100, 1400)]]))

    def test_should_calculate_salary(self):
        self.assertEqual(85, calculate_salary(self.schedule))


if __name__ == '__main__':
    unittest.main()
