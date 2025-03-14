"""
Unit tests for start handlers module in project initialization

-------------------------------------------------------
Name                                Unit   Integ   Func
-------------------------------------------------------
_handle_start_dirs
_handle_start_backup                X
_handle_start_file
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
import stat

from src.handlers.handle_start import _handle_start_backup





def test_handle_start_backup_preserves_metadata(tmpdir):
    """
    Test that backup preserves file metadata using copy2.
    
    Parameters
    ----------
    tmpdir : pytest.fixture
        Temporary directory fixture
    """
    # Create test file with specific permissions
    test_file = tmpdir.join("test.txt")
    test_file.write("test content")
    os.chmod(str(test_file), stat.S_IRWXU)

    # Get original metadata
    orig_stat = os.stat(str(test_file))

    # Create output directory and backup
    output_dir = tmpdir.mkdir("backup")
    result = _handle_start_backup(
        str(test_file),
        str(output_dir)
    )

    # Check backup file metadata matches
    backup_path = output_dir.join("test.txt.bak")
    backup_stat = os.stat(str(backup_path))
    assert backup_stat.st_mode == orig_stat.st_mode
    assert result == 1
