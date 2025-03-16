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
| _handle_start_configs_index        |       |   x   |       |
| _handle_start_configs_proj         |       |       |       |
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
from src.handlers.handle_start import _handle_start_configs_index










def test_handle_start_configs_index():
    """Test _handle_start_configs_index functionality for both default and updated values"""
    # Set up temporary directory and file
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create temporary config index file
        index_path = os.path.join(temp_dir, 'config_index.py')

        initial_content = [
            "NB=0\n",
            "NB_NAME='old_name'\n", 
            "SEQ_NOTATION=0\n",
            "SEQ_SPARSE=0\n"
        ]

        with open(index_path, 'w', encoding='utf-8') as f:
            f.writelines(initial_content)

        try:
            # Test case 1: Default values (no changes)
            config = ConfigManager()
            config.config = {
                'NB': 0,
                'NB_NAME': 'old_name',
                'SEQ_NOTATION': 0,
                'SEQ_SPARSE': 0
            }

            result = _handle_start_configs_index(config, index_path)
            assert result == 1

            with open(index_path, 'r', encoding='utf-8') as f:
                final_content = f.readlines()
            assert final_content == initial_content

            # Test case 2: All values updated
            config.config = {
                'NB': 1,
                'NB_NAME': 'new_name',
                'SEQ_NOTATION': 1,
                'SEQ_SPARSE': 1
            }

            result = _handle_start_configs_index(config, index_path)
            assert result == 1

            with open(index_path, 'r', encoding='utf-8') as f:
                final_content = f.readlines()

            expected_content = [
                "NB=1\n",
                "NB_NAME='new_name'\n",
                "SEQ_NOTATION=1\n",
                "SEQ_SPARSE=1\n",
            ]
            assert final_content == expected_content

        finally:
            pass