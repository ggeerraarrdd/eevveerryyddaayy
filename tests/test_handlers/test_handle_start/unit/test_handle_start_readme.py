"""
Unit tests for start handlers module in project initialization

-------------------------------------------------------
Name                                Unit   Integ   Func
-------------------------------------------------------
_handle_start_dirs
_handle_start_backup                
_handle_start_file
_handle_start_files
_handle_start_date
_handle_start_solutions         
_handle_start_configs_form
_handle_start_configs_index
_handle_start_configs_proj
_handle_start_configs
_handle_start_readme                X
_handle_start_template
handle_start
-------------------------------------------------------

"""

import os
import tempfile

from src.config import ConfigManager
from src.handlers.handle_start import _handle_start_readme










def test_handle_start_readme_default():
    """Test _handle_start_readme functionality with default configs"""
    # Set up temporary directory and file
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create temporary README.md
        readme_path = os.path.join(temp_dir, 'README.md')

        initial_content = [
            '# [ ] Title\n',
            'Some content\n',
            '<!-- Index Start - WARNING: Do not delete or modify this markdown comment. -->\n',
            '| Day   | Title   | Solution   | Site   | Difficulty   |\n',
            '| ----- | ------- | ---------- | ------ | ------------ |\n',
            '<!-- Index End - WARNING: Do not delete or modify this markdown comment. -->\n'
        ]

        with open(readme_path, 'w', encoding='utf-8') as f:
            f.writelines(initial_content)

        # Initialize config with default values
        config = ConfigManager()
        config.config = {
            'PROJ_TITLE': '[ ] Title',
            'NB': 0,
            'NB_NAME': 'NB'
        }

        # Empty package changes dict
        package_changes = {}

        try:
            # Call function with readme_path's directory
            result = _handle_start_readme(config, package_changes, os.path.dirname(readme_path))

            # Verify return value
            assert result == 1

            # Read file after function call
            with open(readme_path, 'r', encoding='utf-8') as f:
                final_content = f.readlines()

            # Verify no changes were made
            assert final_content == initial_content

        finally:
            pass


def test_handle_start_readme_title_only():
    """Test _handle_start_readme functionality with title change only"""
    # Set up temporary directory and file
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create temporary README.md
        readme_path = os.path.join(temp_dir, 'README.md')

        initial_content = [
            '# [ ] Title\n',
            'Some content\n',
            '<!-- Index Start - WARNING: Do not delete or modify this markdown comment. -->\n',
            '| Day   | Title   | Solution   | Site   | Difficulty   |\n',
            '| ----- | ------- | ---------- | ------ | ------------ |\n',
            '<!-- Index End - WARNING: Do not delete or modify this markdown comment. -->\n'
        ]

        with open(readme_path, 'w', encoding='utf-8') as f:
            f.writelines(initial_content)

        # Initialize config with default values
        config = ConfigManager()
        config.config = {
            'PROJ_TITLE': 'New Title',
            'NB': 0,
            'NB_NAME': 'NB'
        }

        # Empty package changes dict
        package_changes = {
            'PROJ_TITLE': {'old_value': '[ ] Title', 'new_value': 'New Title'},
        }

        try:
            # Call function with readme_path's directory
            result = _handle_start_readme(config, package_changes, os.path.dirname(readme_path))

            # Verify return value
            assert result == 1

            # Read modified file
            with open(readme_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            # Verify changes
            assert lines[0] == '# New Title\n'
            assert lines[1] == initial_content[1]
            assert lines[2] == initial_content[2]
            assert lines[3] == initial_content[3]
            assert lines[4] == initial_content[4]
            assert lines[5] == initial_content[5]

        finally:
            pass


def test_handle_start_readme_all():
    """Test _handle_start_readme functionality with all configurable index changes"""
    # Set up temporary directory and file
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create temporary README.md
        readme_path = os.path.join(temp_dir, 'README.md')

        initial_content = [
            '# [ ] Title\n',
            'Some content\n',
            '<!-- Index Start - WARNING: Do not delete or modify this markdown comment. -->\n',
            '| Day   | Title   | Solution   | Site   | Difficulty   |\n',
            '| ----- | ------- | ---------- | ------ | ------------ |\n',
            '<!-- Index End - WARNING: Do not delete or modify this markdown comment. -->\n'
        ]

        with open(readme_path, 'w', encoding='utf-8') as f:
            f.writelines(initial_content)

        # Initialize config with default values
        config = ConfigManager()
        config.config = {
            'PROJ_TITLE': 'New Title',
            'NB': 1,
            'NB_NAME': 'Nota Bene'
        }

        # Empty package changes dict
        package_changes = {
            'PROJ_TITLE': {'old_value': '[ ] Title', 'new_value': 'New Title'},
            'NB': {'old_value': 0, 'new_value': 1},
            'NB_NAME': {'old_value': '', 'new_value': 'Nota Bene'}
        }

        try:
            # Call function with readme_path's directory
            result = _handle_start_readme(config, package_changes, os.path.dirname(readme_path))

            # Verify return value
            assert result == 1

            # Read modified file
            with open(readme_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            # Verify changes
            assert lines[0] == '# New Title\n'
            assert lines[1] == initial_content[1]
            assert lines[2] == initial_content[2]
            assert lines[3] == '| Day   | Title   | Solution   | Site   | Difficulty   | Nota Bene   |\n'
            assert lines[4] == '| ----- | ------- | ---------- | ------ | ------------ | ----------- |\n'
            assert lines[5] == initial_content[5]

        finally:
            pass
