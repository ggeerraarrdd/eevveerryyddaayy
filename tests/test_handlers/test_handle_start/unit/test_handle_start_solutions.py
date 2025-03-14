"""
Unit tests for start handlers module in project initialization

------------------------------------------------------
Name                            Unit   Integ   Func
------------------------------------------------------
_handle_start_dirs
_handle_start_backup
_handle_start_file
_handle_start_files
_handle_start_date
_handle_start_solutions         X
_handle_start_configs_form
_handle_start_configs_index
_handle_start_configs_proj
_handle_start_configs
_handle_start_readme
_handle_start_template
handle_start
------------------------------------------------------

"""

import os
import shutil

from src.handlers.handle_start import _handle_start_solutions










def test_handle_start_solutions(tmpdir, mocker):
    """Test creating solutions directory"""
    # Setup mock config
    mock_config = mocker.Mock()
    mock_config.get.return_value = 'solutions'

    # Mock ROOT_DIR to use temp directory
    mocker.patch('src.handlers.handle_start.ROOT_DIR', str(tmpdir))

    # Test successful directory creation
    result = _handle_start_solutions(mock_config)

    # Verify config.get was called
    mock_config.get.assert_called_once_with('SOLUTIONS_DIR')

    # Verify directory was created
    solutions_dir = os.path.join(str(tmpdir), 'solutions')
    assert os.path.exists(solutions_dir)
    assert result == 1

    # Test directory already exists
    result = _handle_start_solutions(mock_config)
    assert result == 1

    # Test failure scenario
    shutil.rmtree(solutions_dir)  # Remove existing directory
    mocker.patch('os.makedirs', side_effect=OSError)
    result = _handle_start_solutions(mock_config)
    assert result == 0
