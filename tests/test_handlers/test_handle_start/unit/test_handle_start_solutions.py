"""
Unit tests for start handlers module in project initialization


| START HANDLERS                     | Unit  | Integ | Func  |
| ---------------------------------- | ----- | ----- | ----- |
| _handle_start_dirs                 |       |       |       |
| _handle_start_backup               |       |       |       |
| _handle_start_file                 |       |       |       |
| _handle_start_files                |       |       |       |
| _handle_start_date                 |       |       |       |
| _handle_start_solutions            |   x   |       |       |
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
import os
import shutil

# Local
from src.handlers.handle_start import _handle_start_solutions










def test_handle_start_solutions(tmpdir, mocker):
    """Test creating solutions directory"""
    # Mock root_dir
    mock_root_dir = str(tmpdir)

    # Setup mock config
    mock_config = mocker.Mock()
    mock_config.get.return_value = 'solutions'

    # Test 1
    result = _handle_start_solutions(mock_config, mock_root_dir)
    # Verify config.get was called
    mock_config.get.assert_called_once_with('SOLUTIONS_DIR')
    # Verify directory was created
    solutions_dir = os.path.join(str(tmpdir), 'solutions')
    assert os.path.exists(solutions_dir)
    assert result == 1

    # Test 2
    result = _handle_start_solutions(mock_config, mock_root_dir)
    # Verify directory already exists
    assert result == 1

    # Test 3
    shutil.rmtree(solutions_dir)  # Remove existing directory
    mocker.patch('os.makedirs', side_effect=OSError)
    result = _handle_start_solutions(mock_config, mock_root_dir)
    # Verify failure scenario
    assert result == 0
