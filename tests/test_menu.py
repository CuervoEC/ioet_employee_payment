import unittest
from calculator import menu
from unittest.mock import patch


@patch('platform.system')
@patch('os.system')
class TestMenuClass(unittest.TestCase):

    def test_should_call_os_when_linux(self, mock_os_system, mock_platform_system):
        # set up
        os_name = 'Linux'
        # mock return
        mock_platform_system.return_value = os_name
        mock_os_system.return_value = ''
        # action
        menu.clear_os_type()
        # expected result
        mock_platform_system.assert_called_once_with()
        mock_os_system.assert_called_once_with('clear')

    def test_should_call_os_when_windows(self, mock_os_system, mock_platform_system):
        # set up
        os_name = 'Windows'
        # mock return
        mock_platform_system.return_value = os_name
        mock_os_system.return_value = ''
        # action
        menu.clear_os_type()
        # expected result
        mock_platform_system.assert_called_once_with()
        mock_os_system.assert_called_once_with('cls')


if __name__ == '__main__':
    unittest.main()
