"""
Unit tests for start handlers module in project initialization


| START HANDLERS                     | Unit  | Integ | Func  |
| ---------------------------------- | ----- | ----- | ----- |
| _handle_start_dirs                 |       |       |       |
| _handle_start_backup               |       |       |       |
| _handle_start_file                 |       |       |       |
| _handle_start_files                |       |       |       |
| _handle_start_date                 |       |       |       |
| _handle_start_solutions            |       |       |       |
| _handle_start_configs_form         |       |       |       |
| _handle_start_configs_index        |   x   |       |       |
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
import tempfile
from unittest.mock import Mock, MagicMock

# Local
from src.handlers.handle_start import _handle_start_configs_index










def test_handle_start_configs_index():
    """Test _handle_start_configs_index functionality using mock"""
    # Set up temporary directory and file
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create temporary config index file
        index_path = os.path.join(temp_dir, 'config_index.py')

        initial_content = [
            "NB=0\n",
            "NB_NAME='old_name'\n", 
            "SEQ_NOTATION=0\n",
            "SEQ_SPARSE=0\n",
        ]

        with open(index_path, 'w', encoding='utf-8') as f:
            f.writelines(initial_content)

        # Create mock config
        mock_config = Mock()
        mock_config.get = MagicMock(side_effect=lambda x: {
            'NB': 1,
            'NB_NAME': 'new_name',
            'SEQ_NOTATION': 1,
            'SEQ_SPARSE': 1
        }[x])

        try:
            # Call function
            result = _handle_start_configs_index(mock_config, index_path)

            # Verify return value
            assert result == 1

            # Verify mock was called correctly
            mock_config.get.assert_any_call('NB')
            mock_config.get.assert_any_call('NB_NAME')
            mock_config.get.assert_any_call('SEQ_NOTATION')
            mock_config.get.assert_any_call('SEQ_SPARSE')

            # Read file after function call
            with open(index_path, 'r', encoding='utf-8') as f:
                final_content = f.readlines()

            # Verify content was updated with new values
            expected_content = [
                "NB=1\n",
                "NB_NAME='new_name'\n",
                "SEQ_NOTATION=1\n",
                "SEQ_SPARSE=1\n"
            ]
            assert final_content == expected_content

        finally:
            pass
