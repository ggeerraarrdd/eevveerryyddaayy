"""
Unit tests for start handlers module in project initialization

-------------------------------------------------------
Name                                Unit   Integ   Func
-------------------------------------------------------
_handle_start_dirs
_handle_start_backup                
_handle_start_file                  X
_handle_start_files
_handle_start_date
_handle_start_solutions         
_handle_start_configs_form
_handle_start_configs_index
_handle_start_configs_proj
_handle_start_configs
_handle_start_readme
_handle_start_template
handle_start
-------------------------------------------------------

"""

import os

from src.handlers.handle_start import _handle_start_file










def test_handle_start_file(tmpdir, mocker):
    """Test individual file handling operations"""
    # Setup test directories and files
    input_dir = tmpdir.mkdir("input")
    output_dir = tmpdir.mkdir("output")
    bak_dir = tmpdir.mkdir("backup")

    # Create test file
    test_file = input_dir.join("test.txt")
    test_file.write("test content")

    # Mock _handle_start_backup to avoid testing its implementation
    mock_backup = mocker.patch('src.handlers.handle_start._handle_start_backup')

    result = _handle_start_file(
        str(input_dir),
        "test.txt",
        str(bak_dir),
        str(output_dir),
        "test_new.txt"
    )

    # Verify backup was called
    mock_backup.assert_called_once()

    # Verify file was copied to output
    assert os.path.exists(os.path.join(str(output_dir), "test_new.txt"))

    # Verify original file was removed
    assert not os.path.exists(str(test_file))

    assert result == 1
