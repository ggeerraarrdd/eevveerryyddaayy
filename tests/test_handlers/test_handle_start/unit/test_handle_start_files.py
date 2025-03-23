"""
Unit tests for start handlers module in project initialization


| START HANDLERS                     | Unit  | Integ | Func  |
| ---------------------------------- | ----- | ----- | ----- |
| _handle_start_dirs                 |       |       |       |
| _handle_start_backup               |       |       |       |
| _handle_start_file                 |       |       |       |
| _handle_start_files                |   x   |       |       |
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

# Local
from src.handlers.handle_start import _handle_start_files










def test_handle_start_files(tmpdir, mocker):
    """Test handling of all project files"""
    # Mock root_dir and bak_dir
    mock_root_dir = str(tmpdir)
    mock_bak_dir = str(tmpdir.mkdir("backup"))

    # Mock _handle_start_file
    mock_handle_start_file = mocker.patch('src.handlers.handle_start._handle_start_file')

    # Execute
    result = _handle_start_files(mock_root_dir, mock_bak_dir)

    # Assert expected return value
    assert result == 1

    # Assert _handle_start_file handle the required number of files
    # Currently: 6
    assert mock_handle_start_file.call_count == 6

    # Assert specific call
    mock_handle_start_file.assert_any_call(
        mock_root_dir,
        'README.md',
        mock_bak_dir,
        os.path.join(mock_root_dir, 'docs'),
        'README.md'
    )
