import unittest
from main import show_result
from unittest.mock import patch


# patch before tests definition
@patch('calculator.calc.calculate_salary')
@patch('calculator.mapper.unwrap_info')
@patch('calculator.loader.load_file')
class TestMainClass(unittest.TestCase):

    def test_should_show_result(self, mock_load_file, mock_unwrap_info, mock_calculate_salary):
        # set up
        data = [
            'RENE=MO10:00-11:00'
        ]
        file_name = 'data.txt'
        # mock return
        mock_load_file.return_value = data
        mock_unwrap_info.return_value = 'RENE', []
        mock_calculate_salary.return_value = 50
        # action
        show_result(file_name)
        # expected result
        mock_load_file.assert_called_once_with(file_name)
        mock_unwrap_info.assert_called_once_with(data[0])
        mock_calculate_salary.assert_called_once_with([])


if __name__ == '__main__':
    unittest.main()
