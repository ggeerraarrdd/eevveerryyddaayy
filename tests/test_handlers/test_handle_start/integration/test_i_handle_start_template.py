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
| _handle_start_configs_proj         |       |       |       |
| _handle_start_configs              |       |       |       |
| _handle_start_readme               |       |       |       |
| _handle_start_template             |       |   x   |       |
| handle_start_main                       |       |       |       |
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
from src.handlers.handle_start import _handle_start_template










def test_handle_start_template():
    """Test _handle_start_template functionality"""
    # Set up temporary directory and file
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create temporary solution template file
        template_dir = os.path.join(temp_dir, 'templates')
        os.makedirs(template_dir)
        solution_path = os.path.join(template_dir, 'solution.txt')

        # Create mock template content
        initial_content = [
            "# Old Title \\#{{ seq_full }}\n",  # Line 0
            "Some content\n" 
        ] + ["Other content\n"] * 28 + [  # Lines 1-28
            "<!-- ## Old NB Name\n",  # Line 29
            "Content\n",              # Line 30
            "More content\n",         # Line 31
            "-->\n"                   # Line 32
        ]

        with open(solution_path, 'w', encoding='utf-8') as f:
            f.writelines(initial_content)

        # Initialize config
        config = ConfigManager()
        config.config = {
            'TEMPLATES_DIR': 'templates',
            'PROJ_TITLE': 'New Title',
            'NB_NAME': 'New NB Name'
        }

        # Test cases
        test_cases = [
            # Test title change only
            {
                'changes': {'PROJ_TITLE': True},
                'expected_lines': {
                    0: "# New Title \\#{{ seq_full }}\n"
                }
            },
            # Test NB changes only
            {
                'changes': {'NB': True, 'NB_NAME': True},
                'expected_lines': {
                    29: "## New NB Name\n",
                    32: "\n",
                }
            },
            # Test both changes
            {
                'changes': {'PROJ_TITLE': True, 'NB': True, 'NB_NAME': True},
                'expected_lines': {
                    0: "# New Title \\#{{ seq_full }}\n",
                    29: "## New NB Name\n",
                    32: "\n"
                }
            }
        ]

        for case in test_cases:
            try:
                # Call function
                result = _handle_start_template(config, case['changes'], temp_dir)

                # Verify return value
                assert result == 1

                # Read file after function call
                with open(solution_path, 'r', encoding='utf-8') as f:
                    final_content = f.readlines()

                # Verify expected changes
                for line_num, expected_content in case['expected_lines'].items():
                    assert final_content[line_num] == expected_content

                # Verify other lines remained unchanged
                for i, line in enumerate(initial_content):
                    if i not in case['expected_lines']:
                        assert final_content[i] == line

            finally:
                # Reset file content for next test case
                with open(solution_path, 'w', encoding='utf-8') as f:
                    f.writelines(initial_content)
