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
_handle_start_configs_form          X
_handle_start_configs_index
_handle_start_configs_proj
_handle_start_configs
_handle_start_readme                
_handle_start_template
handle_start
-------------------------------------------------------

"""

import os
import tempfile

from src.config import ConfigManager
from src.handlers.handle_start import _handle_start_configs_form










def test_handle_start_configs_form_default():
    """Test _handle_start_configs_form functionality with default config"""
    # Set up temporary directory and file
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create temporary config form file
        form_path = os.path.join(temp_dir, 'config_form.py')

        initial_content = [
            "SITE_OPTIONS=['site1', 'site2', 'site3']\n",
            "OTHER_SETTING='value'\n"
        ]

        with open(form_path, 'w', encoding='utf-8') as f:
            f.writelines(initial_content)

        # Initialize config with default values
        config = ConfigManager()
        config.config = {
            'SITE_OPTIONS': ['site1', 'site2', 'site3']
        }

        try:
            # Call function
            result = _handle_start_configs_form(config, form_path)

            # Verify return value
            assert result == 1

            # Read file after function call
            with open(form_path, 'r', encoding='utf-8') as f:
                final_content = f.readlines()

            # Verify no changes were made since using default config
            assert final_content == initial_content

        finally:
            pass


def test_handle_start_configs_form_less_options():
    """Test _handle_start_configs_form functionality with single option config"""
    # Set up temporary directory and file
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create temporary config form file
        form_path = os.path.join(temp_dir, 'config_form.py')

        initial_content = [
            "SITE_OPTIONS=['site1', 'site2', 'site3']\n",
            "OTHER_SETTING='value'\n"
        ]

        with open(form_path, 'w', encoding='utf-8') as f:
            f.writelines(initial_content)

        # Initialize config with single option
        config = ConfigManager()
        config.config = {
            'SITE_OPTIONS': ['site1']
        }

        try:
            # Call function
            result = _handle_start_configs_form(config, form_path)

            # Verify return value
            assert result == 1

            # Read file after function call
            with open(form_path, 'r', encoding='utf-8') as f:
                final_content = f.readlines()

            # Verify content was updated to single option
            expected_content = [
                "SITE_OPTIONS=['site1']\n",
                "OTHER_SETTING='value'\n"
            ]
            assert final_content == expected_content

        finally:
            pass


def test_handle_start_configs_form_more_options():
    """Test _handle_start_configs_form functionality with single option config"""
    # Set up temporary directory and file
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create temporary config form file
        form_path = os.path.join(temp_dir, 'config_form.py')

        initial_content = [
            "SITE_OPTIONS=['site1', 'site2', 'site3']\n",
            "OTHER_SETTING='value'\n"
        ]

        with open(form_path, 'w', encoding='utf-8') as f:
            f.writelines(initial_content)

        # Initialize config with single option
        config = ConfigManager()
        config.config = {
            'SITE_OPTIONS': ['site1', 'site2', 'site3', 'site4', 'site5']
        }

        try:
            # Call function
            result = _handle_start_configs_form(config, form_path)

            # Verify return value
            assert result == 1

            # Read file after function call
            with open(form_path, 'r', encoding='utf-8') as f:
                final_content = f.readlines()

            # Verify content was updated to single option
            expected_content = [
                "SITE_OPTIONS=['site1', 'site2', 'site3', 'site4', 'site5']\n",
                "OTHER_SETTING='value'\n"
            ]
            assert final_content == expected_content

        finally:
            pass
