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
| _handle_start_configs              |   X   |       |       |
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
from src.handlers.handle_start import _handle_start_configs










def test_handle_start_configs():
    """Test _handle_start_configs with mocked dependencies"""
    # Create mock ConfigManager
    mock_config = Mock()
    mock_config.get.side_effect = lambda x: {
        'CONFIG_DIR': 'config',
        'SITE_OPTIONS': ['site1', 'site2', 'site3'],
        'NB': 0,
        'NB_NAME': 'old_name',
        'SEQ_NOTATION': 0,
        'SEQ_SPARSE': 0,
        'PROJ_TITLE': 'Old Title'
    }[x]

    # Mock the helper functions
    with patch('src.handlers.handle_start._handle_start_configs_form') as mock_form, \
         patch('src.handlers.handle_start._handle_start_configs_index') as mock_index, \
         patch('src.handlers.handle_start._handle_start_configs_proj') as mock_proj, \
         patch('os.path.join') as mock_join:

        # Configure mock os.path.join to return predictable paths
        mock_join.side_effect = lambda *args: '/'.join(args)

        # Configure helper function mocks to return 1
        mock_form.return_value = 1
        mock_index.return_value = 1
        mock_proj.return_value = 1

        # Test with custom root_dir
        custom_root = '/custom/root'
        result = _handle_start_configs(mock_config, root_dir=custom_root)

        # Verify return value
        assert result == 1

        # Verify each helper function was called once with correct arguments
        mock_form.assert_called_once()
        mock_index.assert_called_once()
        mock_proj.assert_called_once()

        # Verify config.get was called for CONFIG_DIR
        mock_config.get.assert_any_call('CONFIG_DIR')

        # Verify correct paths were constructed
        expected_calls = [
            (custom_root, 'config', 'config_form.py'),
            (custom_root, 'config', 'config_index.py'),
            (custom_root, 'config', 'config_proj.py')
        ]
        assert mock_join.call_count == 3
        for expected, actual in zip(expected_calls, mock_join.call_args_list):
            assert expected == actual[0]
