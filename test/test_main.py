import unittest
from main import show_result
import loader
import employee_mapper
from unittest.mock import patch


class TestMainClass(unittest.TestCase):
    def test_should_call_load_file(self):
        data = []
        file_name = 'data.txt'
        with patch.object(loader, 'load_file', return_value=data) as mock_load_file:
            show_result(file_name)
        mock_load_file.assert_called_once_with(file_name)

    @patch('employee_mapper.unwrap_info')
    @patch('loader.load_file')
    def test_should_show_result(self, load_file, unwrap_info):
        data = [
            'RENE=MO10:00-11:00'
        ]
        load_file.return_value = data
        unwrap_info.return_value = 'RENE', []
        file_name = 'data.txt'
        show_result(file_name)
        load_file.assert_called_once_with(file_name)
        unwrap_info.assert_called_once_with(data[0])


if __name__ == '__main__':
    unittest.main()
