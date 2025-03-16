"""
Integration tests for start handlers module in project initialization


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
| _handle_start_configs_proj         |       |   x   |       |
| _handle_start_configs              |       |       |       |
| _handle_start_readme               |       |       |       |
| _handle_start_template             |       |       |       |
| handle_start                       |       |       |       |
| ---------------------------------- | ----- | ----- | ----- |
| OTHERS                             | Unit  | Integ | Func  |
| ---------------------------------- | ----- | ----- | ----- |
| ConfigManager                      |       |   x   |       |
| ---------------------------------- | ----- | ----- | ----- |
"""

# Python Standard Library
import os
import tempfile

# Local
from src.config import ConfigManager
from src.handlers.handle_start import _handle_start_configs_proj











def test_handle_start_configs_proj():
    """Test _handle_start_configs_proj functionality with ConfigManager"""
    # Set up temporary directory and file
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create temporary config proj file
        proj_path = os.path.join(temp_dir, 'config_proj.py')

        initial_content = [
            "PROJ_TITLE='Original Title'\n",
            "OTHER_SETTING='value'\n"
        ]

        with open(proj_path, 'w', encoding='utf-8') as f:
            f.writelines(initial_content)

        # Test Case 1: No changes (default config matches file)
        config = ConfigManager()
        config.config = {
            'PROJ_TITLE': 'Original Title'
        }

        try:
            # Call function
            result = _handle_start_configs_proj(config, proj_path)
            
            # Verify return value
            assert result == 1

            # Read file after function call
            with open(proj_path, 'r', encoding='utf-8') as f:
                final_content = f.readlines()

            # Verify content remained unchanged
            assert final_content == initial_content

            # Test Case 2: Updated title
            config.config['PROJ_TITLE'] = 'New Project Title'
            
            # Call function again
            result = _handle_start_configs_proj(config, proj_path)
            
            # Verify return value
            assert result == 1

            # Read file after function call
            with open(proj_path, 'r', encoding='utf-8') as f:
                final_content = f.readlines()

            # Verify content was updated
            expected_content = [
                "PROJ_TITLE='New Project Title'\n",
                "OTHER_SETTING='value'\n"
            ]
            assert final_content == expected_content

        finally:
            pass
