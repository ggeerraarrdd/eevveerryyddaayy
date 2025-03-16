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
| handle_start                       |       |       |       |
| ---------------------------------- | ----- | ----- | ----- |
| OTHERS                             | Unit  | Integ | Func  |
| ---------------------------------- | ----- | ----- | ----- |
| ---------------------------------- | ----- | ----- | ----- |
"""

# Python Standard Library
from unittest.mock import Mock, patch

# Local
from src.handlers.handle_start import handle_start










def test_handle_start():
    """Unit test for handle_start function"""
    # Setup
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
        mock_dirs.return_value = '/mock/backup/dir'

        # Execute
        result = handle_start(mock_config, package_changes)

        # Assert
        assert result == 1
        mock_dirs.assert_called_once()
        mock_files.assert_called_once_with('/mock/backup/dir')
        mock_date.assert_called_once_with(mock_config)
        mock_solutions.assert_called_once_with(mock_config)
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
        result = handle_start(mock_config, package_changes)

        # Assert
        assert result == 1
        mock_dirs.assert_called_once()
        mock_files.assert_called_once()
        mock_date.assert_called_once()
        mock_solutions.assert_called_once()
