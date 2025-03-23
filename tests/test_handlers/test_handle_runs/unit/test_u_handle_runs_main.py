"""
TD
"""

from datetime import datetime
from unittest.mock import Mock, patch

from src.handlers.handle_runs import handle_runs_main










def test_handle_runs_main():
    """
    TD
    """
    mock_config = Mock()
    mock_package = Mock()
    test_data = {'nb': None}
    test_today = datetime(2025, 3, 23)
    test_is_cols_width_changed = True

    mock_package.get_dictionary.side_effect = [
        {'some': 'package_data'},  # Match the expected value in assertion
        {'width': 'data'}         # Second call return value
    ]

    with patch('src.handlers.handle_runs.clean_strings') as mock_clean_strings, \
         patch('src.handlers.handle_runs._handle_runs_prep') as mock_handle_runs_prep, \
         patch('src.handlers.handle_runs._handle_runs_implement_file') as mock_implement_file, \
         patch('src.handlers.handle_runs._handle_runs_implement_config') as mock_implement_config, \
         patch('src.handlers.handle_runs._handle_runs_implement_index') as mock_implement_index, \
         patch('src.handlers.handle_runs._handle_runs_close') as mock_handle_runs_close:

        mock_clean_strings.return_value = test_data
        mock_implement_config.return_value = test_is_cols_width_changed

        result = handle_runs_main(mock_config,
                                  mock_package,
                                  test_data,
                                  test_today)

        mock_clean_strings.assert_called_once_with(test_data)
        mock_handle_runs_prep.assert_called_once_with(mock_config, mock_package, test_data, test_today)
        mock_implement_file.assert_called_once_with(mock_config, {'some': 'package_data'})
        mock_implement_config.assert_called_once_with(mock_config, mock_package)
        mock_implement_index.assert_called_once_with(mock_config, mock_package, test_is_cols_width_changed)
        mock_handle_runs_close.assert_called_once_with(mock_config, {'width': 'data'})

        assert result == 1
