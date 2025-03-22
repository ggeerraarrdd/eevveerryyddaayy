"""
TD
"""

import os
import tempfile

import pytest

from src.config import ConfigManager









def test_config():
    """Test _handle_start_readme functionality with default configs"""
    # Set up temporary directories and files
    with tempfile.TemporaryDirectory() as temp_dir:
        test_root_dir = temp_dir
        test_config_dir = os.path.join(test_root_dir, 'src', 'config')

        # Create the directory structure
        os.makedirs(test_config_dir, exist_ok=True)

        # Create test config files with sample data
        config_files = {
            'config_form.py': "SITE_OPTIONS=['Codewars', 'DataLemur', 'LeetCode']\nNB_NAME='Number'",
            'config_index.py': "NB=1\nSEQ_NOTATION=0\nSEQ_SPARSE=0",
            'config_paths.py': "SOLUTIONS_DIR='solutions'\nTEMPLATES_DIR='templates'",
            'config_proj.py': "PROJ_TITLE='[ ] Everyday'\nPROJ_START='2025-01-01'"
        }

        # Write test files
        for filename, content in config_files.items():
            file_path = os.path.join(test_config_dir, filename)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)

        config = ConfigManager(test_root_dir, test_config_dir)

        # Test that all expected config values were loaded
        assert config.get('SITE_OPTIONS') == ['Codewars', 'DataLemur', 'LeetCode']
        assert config.get('NB') == 1
        assert config.get('NB_NAME') == 'Number'
        assert config.get('SEQ_NOTATION') == 0
        assert config.get('SOLUTIONS_DIR') == 'solutions'
        assert config.get('TEMPLATES_DIR') == 'templates'
        assert config.get('PROJ_TITLE') == '[ ] Everyday'
        assert config.get('PROJ_START') == '2025-01-01'

        # Test getting non-existent key
        assert config.get('NON_EXISTENT_KEY') is None

        # Test get_all method
        all_config = config.get_all()
        assert isinstance(all_config, dict)
        assert len(all_config) == 9  # Number of config items we defined

        # Test update()
        config.update('NB', 0)
        assert config.get('NB') == 0

        # Test load_settings_from_form()
        test_config_vars = {
            'PROJ_TITLE': (str, 'Test Project'),
            'NB': (int, 1),
            'NB_NAME': (str, 'Test Notes'),
            'SEQ_NOTATION': (int, 1),
            'SEQ_SPARSE': (int, 1),
            'SITE_OPTIONS': (list, ['Site 1', 'Site 2'])
        }
        changes = config.load_settings_from_form(test_config_vars)

        # Verify values were set correctly
        assert config.get('PROJ_TITLE') == 'Test Project'
        assert config.get('NB') == 1
        assert config.get('SITE_OPTIONS') == ['Site 1', 'Site 2']

        expected_changes = {
            'PROJ_TITLE': {'old_value': '[ ] Everyday', 'new_value': 'Test Project'}, 
            'NB': {'old_value': 0, 'new_value': 1}, 
            'NB_NAME': {'old_value': 'Number', 'new_value': 'Test Notes'}, 
            'SEQ_NOTATION': {'old_value': 0, 'new_value': 1},
            'SEQ_SPARSE': {'old_value': 0, 'new_value': 1}, 
            'SITE_OPTIONS': {'old_value': ['Codewars', 'DataLemur', 'LeetCode'], 'new_value': ['Site 1', 'Site 2']}
        }
        assert changes == expected_changes


def test_config_load_error():
    """Test _handle_start_readme functionality with default configs"""
    # Set up temporary directories and files
    with tempfile.TemporaryDirectory() as temp_dir:
        test_root_dir = temp_dir
        test_config_dir = os.path.join(test_root_dir, 'src', 'config')

        # Create the directory structure
        os.makedirs(test_config_dir, exist_ok=True)

        # Test all possible exceptions
        with pytest.raises((FileNotFoundError, ImportError, AttributeError, ValueError)):
            ConfigManager(test_root_dir, test_config_dir)
