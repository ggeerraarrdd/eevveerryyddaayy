"""
TD
"""

import importlib
import os
from unittest.mock import patch










def test_handle_start_root_dir_no_fallback():
    """
    Test that ROOT_DIR falls back to ROOT_DIR_2 when ROOT_DIR_1/src doesn't exist
    """
    with patch('src.config.ROOT_DIR_1', 'fake/path/1'), \
         patch('src.config.ROOT_DIR_2', 'fake/path/2'), \
         patch('os.path.exists') as mock_exists:

        mock_exists.return_value = True

        # Import utils_runs after setting up the patches
        import src.handlers.handle_start  # pylint: disable=import-outside-toplevel
        importlib.reload(src.handlers.handle_start)

        assert src.handlers.handle_start.ROOT_DIR == 'fake/path/1'
        mock_exists.assert_called_once_with(os.path.join('fake/path/1', 'src'))


def test_handle_start_root_dir_with_fallback():
    """
    Test that ROOT_DIR falls back to ROOT_DIR_2 when ROOT_DIR_1/src doesn't exist
    """
    with patch('src.config.ROOT_DIR_1', 'fake/path/1'), \
         patch('src.config.ROOT_DIR_2', 'fake/path/2'), \
         patch('os.path.exists') as mock_exists:

        mock_exists.return_value = False

        # Import utils_runs after setting up the patches
        import src.handlers.handle_start   # pylint: disable=import-outside-toplevel
        importlib.reload(src.handlers.handle_start)

        assert src.handlers.handle_start.ROOT_DIR == 'fake/path/2'
        mock_exists.assert_called_once_with(os.path.join('fake/path/1', 'src'))
