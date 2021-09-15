import unittest
from calculator.mapper import unwrap_info


class MapperTestClass(unittest.TestCase):
    def setUp(self):
        self.text = 'RENE=MO10:00-12:00,MO18:00-22:00,TU10:00-12:00'

    def test_should_return_name_and_schedule_when_valid_text_is_provided(self):
        name, schedule = unwrap_info(self.text)
        expected_name = 'RENE'
        # This data structure needs refactoring, could be more simple
        expected_schedule = [
            ['MONDAY', (600, 720)],
            ['MONDAY', (1080, 1320)],
            ['TUESDAY', (600, 720)]
        ]
        self.assertEqual(expected_name, name)
        self.assertEqual(expected_schedule, schedule)

    def test_should_throw_exception_when_invalid_text_without_equal(self):
        edge_invalid_text = 'invalid'
        with self.assertRaises(ValueError):
            unwrap_info(edge_invalid_text)

    def test_should_throw_exception_when_invalid_text_with_more_equals(self):
        edge_invalid_text = 'i==n=d'
        with self.assertRaises(ValueError, msg='Invalid text was provided.'):
            unwrap_info(edge_invalid_text)

    def test_should_return_empty_when_name_and_schedule_not_defined(self):
        edge_invalid_text = '='
        with self.assertRaises(ValueError, msg='Name or schedule is empty.'):
            unwrap_info(edge_invalid_text)

    def test_should_throw_exception_when_invalid_schedule_format(self):
        edge_invalid_schedule = 'RENE=M12:00'
        with self.assertRaises(ValueError, msg='Invalid schedule format.'):
            unwrap_info(edge_invalid_schedule)

    def test_should_throw_exception_when_invalid_day(self):
        edge_invalid_day = 'RENE=HY10:00-12:00'
        with self.assertRaises(ValueError, msg='Invalid day.'):
            unwrap_info(edge_invalid_day)

    def test_should_throw_exception_when_worked_minutes_are_negative(self):
        edge_invalid_schedule = 'RENE=MO12:00-10:00'
        with self.assertRaises(ValueError, msg='Incorrect schedule values. Final hour is greater than initial.'):
            unwrap_info(edge_invalid_schedule)


if __name__ == '__main__':
    unittest.main()
