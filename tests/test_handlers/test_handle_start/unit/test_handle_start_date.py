"""
Unit tests for start handlers module in project initialization


| START HANDLERS                     | Unit  | Integ | Func  |
| ---------------------------------- | ----- | ----- | ----- |
| _handle_start_dirs                 |       |       |       |
| _handle_start_backup               |       |       |       |
| _handle_start_file                 |       |       |       |
| _handle_start_files                |       |       |       |
| _handle_start_date                 |   x   |       |       |
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
from datetime import datetime

# Local
from src.handlers.handle_start import _handle_start_date










def test_handle_start_date(tmpdir, mocker):
    """Test updating project start date in config file"""
    # Setup mock config
    mock_config = mocker.Mock()
    mock_config.get.return_value = 'config'

    # Create test config file
    config_dir = tmpdir.mkdir("config")
    config_file = config_dir.join("config_proj.py")
    config_file.write("PROJ_START=''\n")

    # Mock ROOT_DIR and HYPHEN
    mocker.patch('src.handlers.handle_start.ROOT_DIR', str(tmpdir))
    mocker.patch('src.handlers.handle_start.HYPHEN', '\u2011')

    # Mock datetime to return fixed date
    mock_date = datetime(2025, 1, 1)
    mock_datetime = mocker.patch('src.handlers.handle_start.datetime')
    mock_datetime.now.return_value = mock_date

    # Call function
    result = _handle_start_date(mock_config)

    # Verify config.get was called
    mock_config.get.assert_called_once_with('CONFIG_DIR')

    # Verify file was updated with correct date format
    updated_content = config_file.read()
    assert "PROJ_START='2025\u201101\u201101'" in updated_content

    # Verify no regular hyphens are used
    assert "-'" not in updated_content
    assert "\u2013" not in updated_content  # en dash
    assert "\u2014" not in updated_content  # em dash

    # Verify success
    assert result == 1
