"""
TD
"""

import os
import shutil
import tempfile
from unittest.mock import patch

from src import eevveerryyddaayy
from src.utils import validate_project


def copy_selected_items(src_dir, dest_dir, selected_items):
    """
    Copy specified directories and files from the root directory to the destination.
    """
    for item in selected_items:
        src_path = os.path.join(src_dir, item)
        dest_path = os.path.join(dest_dir, item)
        if os.path.isdir(src_path):
            shutil.copytree(src_path, dest_path)
        elif os.path.isfile(src_path):
            shutil.copy2(src_path, dest_path)

def get_directory_state(directory):
    """
    Get the current state of a directory for comparison.
    """
    state = {}
    for root, dirs, files in os.walk(directory):
        rel_path = os.path.relpath(root, directory)
        state[rel_path] = {"dirs": sorted(dirs), "files": sorted(files)}
    return state

def x_eevveerryyddaayy():
    """
    Functional test for the EEVVEERRYYDDAAYY project.
    """
    if validate_project():
        return

    root_dir = os.path.dirname(os.path.abspath(__file__))  # Dynamically find root directory
    selected_items = [
        ".vscode",
    ]

    # Step 1: Create a temporary directory and copy the selected items
    with tempfile.TemporaryDirectory() as temp_dir:
        copy_selected_items(root_dir, temp_dir, selected_items)

        with patch('src.utils.validate_project', return_value=False):

            # Test Form Inputs
            proj_title='[ ] Everyday'
            nb=0
            na_name='NB'
            seq_notation=0
            seq_sparse=0
            site_options=['Codewars', 'DataLemur', 'LeetCode']

            # Step 2: Trigger the eevveerryyddaayy function
            # Simulate running the main function here, e.g., using subprocess or calling directly
            eevveerryyddaayy(proj_title, nb, na_name, seq_notation, seq_sparse, site_options, source=0)

            # Step 3: Verify the current state of the directory
            expected_state = {
                ".": {
                    "dirs": [".vscode"],
                },
                ".vscode": {
                    "dirs": [],
                    "files": ["settings.json"]
                }
            }
            actual_state = get_directory_state(temp_dir)

            # Compare actual and expected states
            assert actual_state == expected_state, f"Mismatch found: {actual_state}"
