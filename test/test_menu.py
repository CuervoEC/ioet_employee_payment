import os
import platform
import unittest
import menu
from unittest.mock import patch


class TestMenuClass(unittest.TestCase):

    def test_should_call_os_when_linux(self):
        os_name = 'Linux'
        with patch.object(platform, 'system', return_value=os_name) as mock_platform_system:
            with patch.object(os, 'system', return_value='') as mock_os_system:
                menu.clear_os_type()
        mock_platform_system.assert_called_once_with()
        mock_os_system.assert_called_once_with('clear')

    def test_should_call_os_when_windows(self):
        os_name = 'Windows'
        with patch.object(platform, 'system', return_value=os_name) as mock_platform_system:
            with patch.object(os, 'system', return_value='') as mock_os_system:
                menu.clear_os_type()
        mock_platform_system.assert_called_once_with()
        mock_os_system.assert_called_once_with('cls')


if __name__ == '__main__':
    unittest.main()
