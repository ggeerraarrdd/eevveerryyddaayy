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
| handle_start                       |       |       |       |
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
    # Mock _handle_start_file to avoid actual file operations
    mock_handle_file = mocker.patch('src.handlers.handle_start._handle_start_file')

    # Mock ROOT_DIR
    mock_root = str(tmpdir)
    mocker.patch('src.handlers.handle_start.ROOT_DIR', mock_root)

    bak_dir = str(tmpdir.mkdir("backup"))

    result = _handle_start_files(bak_dir)

    # Verify _handle_start_file was called for each expected file
    assert mock_handle_file.call_count == 6  # Number of files handled

    # Verify specific calls if needed
    mock_handle_file.assert_any_call(
        mock_root,
        'README.md',
        bak_dir,
        os.path.join(mock_root, 'docs'),
        'README.md'
    )

    assert result == 1
