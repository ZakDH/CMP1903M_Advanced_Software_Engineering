import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime
import os

class KeyloggerTest(unittest.TestCase):
    def test_on_key_press(self):
        keylogger = Keylogger()

        # Mock the file object and patch the open() function to return the mock
        mock_file = MagicMock()
        with patch('builtins.open', return_value=mock_file) as mock_open:
            # Create a mock event object
            mock_event = MagicMock()
            mock_event.Key = 'A'
            mock_event.Ascii = 65

            # Call the on_key_press method
            keylogger.on_key_press(mock_event)

            # Assert that the file was opened with the correct path
            expected_log_file = f'{os.getcwd()}/{datetime.now().strftime("%d-%m-%Y|%H:%M")}.log'
            mock_open.assert_called_once_with(expected_log_file, 'a')

            # Assert that the correct content was written to the file
            mock_file.write.assert_called_once_with('A')
            
    def test_start(self):
        keylogger = Keylogger()

        # Mock the pyxhook module and the HookManager class
        mock_pyxhook = MagicMock()
        mock_hook_manager = MagicMock()
        mock_pyxhook.HookManager.return_value = mock_hook_manager

        # Patch the necessary modules
        with patch('pyxhook', mock_pyxhook), \
             patch('builtins.open'):
            keylogger.start()

            # Assert that the HookManager was created and configured correctly
            mock_hook_manager.KeyDown.assert_called_once_with(keylogger.on_key_press)
            mock_hook_manager.HookKeyboard.assert_called_once()
            mock_hook_manager.start.assert_called_once()    
                       
            
    @patch('pyxhook.print_err')
    def test_start_exception_handling(self, mock_print_err):
        keylogger = Keylogger()

        # Mock the pyxhook module and the HookManager class
        mock_pyxhook = MagicMock()
        mock_hook_manager = MagicMock()
        mock_hook_manager.start.side_effect = KeyboardInterrupt()
        mock_pyxhook.HookManager.return_value = mock_hook_manager

        # Patch the necessary modules
        with patch('pyxhook', mock_pyxhook), \
             patch('builtins.open'):
            keylogger.start()

            # Assert that the HookManager was canceled and the listener was closed
            mock_hook_manager.cancel.assert_called_once()
            mock_print_err.assert_not_called()
            
    @patch('pyxhook.print_err')
    def test_start_exception_handling_with_error(self, mock_print_err):
        keylogger = Keylogger()

        # Mock the pyxhook module and the HookManager class
        mock_pyxhook = MagicMock()
        mock_hook_manager = MagicMock()
        mock_hook_manager.start.side_effect = Exception('Some error')
        mock_pyxhook.HookManager.return_value = mock_hook_manager

        # Patch the necessary modules
        with patch('pyxhook', mock_pyxhook), \
             patch('builtins.open') as mock_open:
            keylogger.start()

            # Assert that the HookManager was canceled and the error message was written to the file
            mock_hook_manager.cancel.assert_called_once()
            mock_print_err.assert_called_once()
            mock_open.assert_called_once()
            mock_open.return_value.write.assert_called_once()

if __name__ == "__main__":
    unittest.main()
