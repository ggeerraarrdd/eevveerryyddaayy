"""
Unit tests for start handlers module in project initialization


| START HANDLERS                     | Unit  | Integ | Func  |
| ---------------------------------- | ----- | ----- | ----- |
| _handle_start_dirs                 |       |       |       |
| _handle_start_backup               |       |       |       |
| _handle_start_file                 |       |       |       |
| _handle_start_files                |       |       |       |
| _handle_start_date                 |       |       |       |
| _handle_start_solutions            |       |       |       |
| _handle_start_configs_form         |       |       |       |
| _handle_start_configs_index        |       |       |       |
| _handle_start_configs_proj         |       |       |       |
| _handle_start_configs              |       |       |       |
| _handle_start_readme               |       |       |       |
| _handle_start_template             |       |       |       |
| handle_start_main                  |       |       |       |
| ---------------------------------- | ----- | ----- | ----- |
| OTHERS                             | Unit  | Integ | Func  |
| ---------------------------------- | ----- | ----- | ----- |
| ---------------------------------- | ----- | ----- | ----- |
"""

# Python Standard Library
import os
from unittest.mock import Mock, patch

# Local
from src.handlers.handle_start import handle_start_main










def test_handle_start(tmpdir):
    """Unit test for handle_start function"""
    # Set up
    mock_root_dir = str(tmpdir)
    mock_bak_dir = str(tmpdir.mkdir("backup"))
    mock_hyphen = '\u2011'

    # Set up config and package_changes
    mock_config = Mock(spec='ConfigManager')
    package_changes = {'PROJ_TITLE': 'Test Project'}

    # Mock all dependent functions
    with patch('src.handlers.handle_start._handle_start_dirs') as mock_dirs, \
         patch('src.handlers.handle_start._handle_start_files') as mock_files, \
         patch('src.handlers.handle_start._handle_start_date') as mock_date, \
         patch('src.handlers.handle_start._handle_start_solutions') as mock_solutions, \
         patch('src.handlers.handle_start._handle_start_configs') as mock_configs, \
         patch('src.handlers.handle_start._handle_start_readme') as mock_readme, \
         patch('src.handlers.handle_start._handle_start_template') as mock_template:

        # Setup mock return value
        mock_dirs.return_value = os.path.join(mock_root_dir, mock_bak_dir)

        # Execute
        result = handle_start_main(mock_config, package_changes, mock_root_dir)

        # Assert
        assert result == 1
        mock_dirs.assert_called_once_with(mock_root_dir)
        mock_files.assert_called_once_with(mock_root_dir, mock_bak_dir)
        mock_date.assert_called_once_with(mock_config, mock_root_dir, mock_hyphen)
        mock_solutions.assert_called_once_with(mock_config, mock_root_dir)
        mock_configs.assert_called_once_with(mock_config)
        mock_readme.assert_called_once_with(mock_config, package_changes)
        mock_template.assert_called_once_with(mock_config, package_changes)


def test_handle_start_no_changes():
    """Unit test for handle_start with empty package_changes"""
    # Setup
    mock_config = Mock(spec='ConfigManager')
    package_changes = {}

    # Mock dependent functions
    with patch('src.handlers.handle_start._handle_start_dirs') as mock_dirs, \
         patch('src.handlers.handle_start._handle_start_files') as mock_files, \
         patch('src.handlers.handle_start._handle_start_date') as mock_date, \
         patch('src.handlers.handle_start._handle_start_solutions') as mock_solutions:

        # Execute
        result = handle_start_main(mock_config, package_changes)

        # Assert
        assert result == 1
        mock_dirs.assert_called_once()
        mock_files.assert_called_once()
        mock_date.assert_called_once()
        mock_solutions.assert_called_once()
