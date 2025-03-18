"""
TD
"""

import os
import shutil
import json
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


def test_eevveerryyddaayy(tmpdir):
    """
    Functional test for the EEVVEERRYYDDAAYY project.
    """
    if validate_project():
        return

    root_dir = os.path.abspath('.')
    selected_items = [
        ".vscode",
    ]

    mock_root_dir = str(tmpdir)

    print(root_dir)
    print(mock_root_dir)

    copy_selected_items(root_dir, mock_root_dir, selected_items)
    actual_state = get_directory_state(mock_root_dir)
    print(json.dumps(actual_state, indent=4))

    with patch('src.utils.validate_project', return_value=False):

        proj_title='[ ] Everyday'
        nb=0
        nb_name='NB'
        seq_notation=0
        seq_sparse=0
        site_options=['Codewars', 'DataLemur', 'LeetCode']

        eevveerryyddaayy(proj_title,
                         nb,
                         nb_name,
                         seq_notation,
                         seq_sparse,
                         site_options,
                         root_dir=mock_root_dir,
                         source=1)

        actual_state = get_directory_state(mock_root_dir)
        print(json.dumps(actual_state, indent=4))
