"""
TD
"""

import os
import shutil
# import json

from src import eevveerryyddaayy
from src.utils import validate_project


def copy_selected_items(src_dir, dest_dir, selected_items, ignore_patterns=None):
    """
    Copy specified directories and files from the root directory to the destination.
    
    Parameters
    ----------
    src_dir : str
        Source directory path
    dest_dir : str
        Destination directory path
    selected_items : list
        List of items to copy
    ignore_patterns : list, optional
        List of patterns to ignore (e.g. ['*.pyc', '.DS_Store'])
    """
    if ignore_patterns is None:
        ignore_patterns = []

    def should_ignore(path):
        return any(pattern in path for pattern in ignore_patterns)

    for item in selected_items:
        src_path = os.path.join(src_dir, item)
        dest_path = os.path.join(dest_dir, item)

        if should_ignore(src_path):
            continue

        if os.path.isdir(src_path):
            shutil.copytree(src_path, dest_path,
                          ignore=shutil.ignore_patterns(*ignore_patterns))
        elif os.path.isfile(src_path) and not should_ignore(src_path):
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


def test_eevveerryyddaayy_start_and_false_init(tmpdir, mocker):
    """
    Functional test for the EEVVEERRYYDDAAYY project.
    """
    if validate_project():
        return

    mock_root_dir = str(tmpdir)

    root_dir = os.path.abspath('.')
    selected_items = [
        '.github',
        '.vscode',
        'docs',
        'src/config',
        'README.md',
        'README.template.md',
        'renovate.json'
    ]
    ignore_patterns = [
        'c*.json',
        '*.pyc',
        '__pycache__',
        '.DS_Store'
    ]
    copy_selected_items(root_dir, mock_root_dir, selected_items, ignore_patterns)

    # print(root_dir)
    # print(mock_root_dir)

    # pre_state = get_directory_state(mock_root_dir)
    # print(json.dumps(pre_state, indent=4))
    # print("\n")

    validate_project_mock = mocker.patch('src.app.validate_project')
    validate_project_mock.return_value = False

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
                        source=0)
    actual_state = get_directory_state(mock_root_dir)

    # print("\n")
    # print(json.dumps(actual_state, indent=4))
    # print("\n")
    # print(actual_state['.github'])
    # print("\n")

    assert actual_state['.']['files'] == ["README.md"]
    assert 'codecov.yaml' not in actual_state['.github']
    assert actual_state['.vscode'] == {"dirs": [], "files": ["settings.json"]}


def test_eevveerryyddaayy_start_and_true_init(tmpdir, mocker):
    """
    Functional test for the EEVVEERRYYDDAAYY project.
    """
    if validate_project():
        return

    mock_root_dir = str(tmpdir)

    root_dir = os.path.abspath('.')
    selected_items = [
        '.github',
        '.vscode',
        'docs',
        'src/config',
        'README.md',
        'README.template.md',
        'renovate.json'
    ]
    ignore_patterns = [
        'c*.json',
        '*.pyc',
        '__pycache__',
        '.DS_Store'
    ]
    copy_selected_items(root_dir, mock_root_dir, selected_items, ignore_patterns)

    validate_project_mock = mocker.patch('src.app.validate_project')
    validate_project_mock.return_value = True

    proj_title='[ ] Everyday'
    nb=0
    nb_name='NB'
    seq_notation=0
    seq_sparse=0
    site_options=['Codewars', 'DataLemur', 'LeetCode']

    result = eevveerryyddaayy(proj_title,
                            nb,
                            nb_name,
                            seq_notation,
                            seq_sparse,
                            site_options,
                            root_dir=mock_root_dir,
                            source=0)

    assert result == 0
