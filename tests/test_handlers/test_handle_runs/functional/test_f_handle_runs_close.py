"""
TD
"""

import importlib
import os
import tempfile
from textwrap import dedent

from src.config import ConfigManager
from src.handlers.handle_runs import _handle_runs_close









def test_handle_runs_close_functional():
    """
    TD
    """
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create temporary README.md
        test_root_dir = str(temp_dir)
        test_config_dir = os.path.join(test_root_dir, 'config')
        os.makedirs(test_config_dir)
        test_config_index_path = os.path.join(test_config_dir, 'config_index.py')

        test_config_index = dedent(dedent(dedent("""
            '''
            Some Content
            '''
            COLS_WIDTH = {
                'day': 5,
                'title': 7,
                'solution': 15
                'site': 6,
                'difficulty': 12,
                'nb': 1
            }" 
        """
        )))

        with open(test_config_index_path, 'w', encoding='utf-8') as f:
            f.write(test_config_index)

        # Setup test environment
        test_config = ConfigManager()
        test_config.config = {
            'CONFIG_DIR': test_config_dir
        }

        # New column widths to update
        test_column_widths = {
            'day': 10,
            'title': 30,
            'solution': 30,
            'site': 10,
            'difficulty': 12,
            'nb': 20
        }

        result = _handle_runs_close(test_config,
                                    test_column_widths,
                                    test_root_dir)
        assert result == 1

        # Import the updated config file to verify changes
        spec = importlib.util.spec_from_file_location("config_index", test_config_index_path)
        config_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(config_module)

        # Verify each column width matches expected value
        for column, width in test_column_widths.items():
            assert config_module.COLS_WIDTH[column] == width
