"""
TD
"""

from datetime import datetime
from unittest.mock import Mock, patch

from src.handlers.handle_runs import _handle_runs_prep_seq










def test_handle_runs_prep_seq_empty_dir():
    """Test sequence generation with empty directory"""
    mock_config = Mock()
    mock_config.get.side_effect = {
        'PROJ_START': '2025-03-14',
        'SEQ_NOTATION': 0,
        'SOLUTIONS_DIR': '/fake/path'
    }.get

    test_date = datetime(2025, 3, 15)

    with patch('os.scandir') as mock_scandir:
        mock_scandir.return_value.__enter__.return_value = []

        result = _handle_runs_prep_seq(mock_config, test_date)

        assert result[0] == '001_01'  # full sequence
        assert result[1] == '001'     # main sequence
        assert result[2] is None      # last main
        assert result[3] is None      # next main

        mock_scandir.assert_called_once_with('/fake/path')


def test_handle_runs_prep_seq_nonempty_dir():
    """Test sequence generation with existing files"""
    hyphen = '\u2011'
    mock_config = Mock()
    mock_config.get.side_effect = {
        'PROJ_START': f'2025{hyphen}03{hyphen}14',
        'SEQ_NOTATION': 0,
        'SOLUTIONS_DIR': '/fake/path'
    }.get

    test_date = datetime(2025, 3, 15)

    mock_file1 = Mock()
    mock_file1.name = '001_01_test.md'
    mock_file2 = Mock()
    mock_file2.name = '001_02_test.md'

    with patch('os.scandir') as mock_scandir:
        mock_scandir.return_value.__enter__.return_value = [mock_file1, mock_file2]

        result = _handle_runs_prep_seq(mock_config, test_date)

        assert result[0] == '002_01'  # full sequence
        assert result[1] == '002'     # main sequence
        assert result[2] == 1         # last main
        assert result[3] == 2         # next main

        mock_scandir.assert_called_once_with('/fake/path')


def test_handle_runs_prep_seq_calls_correct_function():
    """Test that the correct sequence function is called based on directory state"""
    hyphen = '\u2011'
    mock_config = Mock()
    mock_config.get.side_effect = {
        'PROJ_START': f'2025{hyphen}03{hyphen}14',
        'SEQ_NOTATION': 0,
        'SOLUTIONS_DIR': '/fake/path'
    }.get

    test_date = datetime(2025, 3, 15)
    mock_file = Mock()
    mock_file.name = '001_01_test.md'

    with patch('os.scandir') as mock_scandir, \
         patch('src.handlers.handle_runs._handle_runs_prep_seq_files') as mock_prep_files, \
         patch('src.handlers.handle_runs._handle_runs_prep_seq_no_files') as mock_prep_no_files:

        # Test with files present
        mock_scandir.return_value.__enter__.return_value = [mock_file]
        _handle_runs_prep_seq(mock_config, test_date)

        mock_prep_files.assert_called_once()
        mock_prep_no_files.assert_not_called()

        # Reset mocks
        mock_prep_files.reset_mock()
        mock_prep_no_files.reset_mock()

        # Test with empty directory
        mock_scandir.return_value.__enter__.return_value = []
        _handle_runs_prep_seq(mock_config, test_date)

        mock_prep_files.assert_not_called()
        mock_prep_no_files.assert_called_once()
