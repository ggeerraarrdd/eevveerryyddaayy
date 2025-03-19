"""
TD
"""

from unittest.mock import Mock, patch
from datetime import datetime

from src.handlers.handle_runs import _handle_runs_prep











def test_handle_runs_preps():
    """
    TD
    """
    # Setup
    mock_config = Mock()
    mock_config.get.side_effect = lambda x: {
        'SEQ_SPARSE': 1
    }[x]

    mock_package = Mock()

    mock_data = {'title': 'test_title'}
    mock_today = datetime(2025, 3, 15)

    with patch('src.handlers.handle_runs._handle_runs_prep_seq') as mock_prep_seq, \
        patch('src.handlers.handle_runs._handle_runs_prep_file') as mock_prep_file, \
        patch('src.handlers.handle_runs._handle_runs_prep_index') as mock_prep_index, \
        patch('src.handlers.handle_runs._handle_runs_prep_package') as mock_prep_package:

        mock_prep_seq.return_value = ('full_str', 'main_str', 'last_main', 'next_main')
        mock_prep_file.return_value = 'test_filename'

        # Execute function
        result = _handle_runs_prep(mock_config, mock_package, mock_data, mock_today)

        # Verify results
        assert result == 1

        # Verify mock calls
        mock_prep_seq.assert_called_once_with(mock_config, mock_today)
        mock_prep_file.assert_called_once_with('test_title', 'full_str')
        mock_prep_index.assert_called_once_with(mock_config, 'last_main', 'next_main')
        mock_prep_package.assert_called_once_with(
            mock_package, 'main_str', 'full_str', mock_data, 'test_filename'
        )
        mock_config.get.assert_called_once_with('SEQ_SPARSE')
