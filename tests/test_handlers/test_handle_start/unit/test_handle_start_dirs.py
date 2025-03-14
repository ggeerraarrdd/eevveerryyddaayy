"""
Unit tests for start handlers module in project initialization
-------------------------------------------------------
Name                                Unit   Integ   Func
-------------------------------------------------------
_handle_start_dirs                  X
_handle_start_backup                
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
from datetime import datetime

from src.handlers.handle_start import _handle_start_dirs










def test_handle_start_dirs(tmpdir, mocker):
    """
    Test creation of backup directory for project initialization files.
    
    Parameters
    ----------
    tmpdir : pytest.fixture
        Temporary directory fixture
    mocker : pytest.fixture
        Pytest mocker fixture
    """
    # Mock ROOT_DIR to use temporary directory
    mock_root = str(tmpdir)
    mocker.patch('src.handlers.handle_start.ROOT_DIR', mock_root)

    # Mock datetime to return fixed date
    mock_date = datetime(2025, 3, 13)
    mocker.patch('src.handlers.handle_start.datetime',
                 mocker.Mock(now=lambda: mock_date))

    # Call function
    result = _handle_start_dirs()

    # Check expected path was created
    expected_path = os.path.join(
        mock_root,
        'assets', 
        'start',
        '2025-03-13_start_bak'
    )

    assert result == expected_path
    assert os.path.exists(expected_path)
    assert os.path.isdir(expected_path)
