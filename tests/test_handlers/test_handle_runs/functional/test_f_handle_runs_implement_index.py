"""
TD
"""

import os
import tempfile

from src.config import ConfigManager
from src.handlers.handle_runs import _handle_runs_implement_index
from src.utils import PackageManager










def test_handle_runs_implement_index_no_nb():
    """
    TD
    """
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create temporary README.md
        test_root_dir = str(temp_dir)
        test_readme_path = os.path.join(test_root_dir, 'README.md')

        test_readme = [
            '# Test Title\n',
            'Some content\n',
            '<!-- Index Start - WARNING: Do not delete or modify this markdown comment. -->\n',
            '| Day   | Title   | Solution   | Site   | Difficulty   |\n',
            '| ----- | ------- | ---------- | ------ | ------------ |\n',
            '<!-- Index End - WARNING: Do not delete or modify this markdown comment. -->\n'
        ]

        with open(test_readme_path, 'w', encoding='utf-8') as f:
            f.writelines(test_readme)

        # Initialize config with default values
        test_config = ConfigManager()
        test_config.config = {
            'CONFIG_DIR': 'config',
            'SITE_OPTIONS': ['site1', 'site2', 'site3'],
            'NB': 0,
            'NB_NAME': 'old_name',
            'SEQ_NOTATION': 0,
            'SEQ_SPARSE': 0,
            'PROJ_TITLE': 'Old Title',
            'COLS_WIDTH': {
                'day': 5,
                'title': 7,
                'solution': 10,
                'site': 6,
                'difficulty': 12,
                'nb': 1
            }
        }

        # Initialize config with default values
        test_package = PackageManager()
        test_package.update_value('package', 'day', '001')
        test_package.update_value('package', 'url', 'https://example.com')
        test_package.update_value('package', 'title', '[Test Title](https://example.com)')
        test_package.update_value('package', 'title_index', 'Test Title')
        test_package.update_value('package', 'solution', '[Solution](solutions/001_01_test_title)')
        test_package.update_value('package', 'site', 'Test Site')
        test_package.update_value('package', 'difficulty', 'Easy')
        test_package.update_value('package', 'problem', 'Test Problem')
        test_package.update_value('package', 'submitted_solution','Test Submitted Solution')
        test_package.update_value('package', 'site_solution', 'Test Site Solution')
        test_package.update_value('package', 'notes', 'Test Notes')
        test_package.update_value('package', 'nb', 'TBD')
        test_package.update_value('package', 'seq_full', '001_01')
        test_package.update_value('package', 'filename', '001_01_test_title')

        # Note:
        # Col widths updated prior to _handle_runs_implement_index() call
        # Not the lengths of package items
        # But higher between config values and length of item in package
        test_package.update_value('package_widths', 'day', 5)
        test_package.update_value('package_widths', 'title', 35)
        test_package.update_value('package_widths', 'solution', 41)
        test_package.update_value('package_widths', 'site', 11)
        test_package.update_value('package_widths', 'difficulty', 12)
        test_package.update_value('package_widths', 'nb', 1)


        test_return = _handle_runs_implement_index(test_config,
                                                    test_package,
                                                    1,
                                                    test_root_dir)
        assert test_return == 1

        with open(test_readme_path, 'r', encoding='utf-8') as f:
            test_lines = f.readlines()

        # for test_line in test_lines:
        #     print(test_line)

        header = '| Day   | Title                               | Solution                                  | Site        | Difficulty   |\n'
        sep = '| ----- | ----------------------------------- | ----------------------------------------- | ----------- | ------------ |\n'
        entry = '| 001   | [Test Title](https://example.com)   | [Solution](solutions/001_01_test_title)   | Test Site   | Easy         |\n'

        assert len(test_lines) == 7
        assert test_lines[3] == header
        assert test_lines[4] == sep
        assert test_lines[5] == entry
