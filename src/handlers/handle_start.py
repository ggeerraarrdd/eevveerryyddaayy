"""
Project Start Handlers

This module provides handlers for initializing project settings selected by
users. It handles setting up configuration files, README.md, and solution 
templates based on those settings.

Functions:
    Public:
        handle_start: Main entry point for project initialization
    
    Private (internal use only):
        _handle_start_date: Updates project start date in config
        _handle_start_configs: Updates configuration files with environment variables
        _handle_start_readme: Sets up notebook column in README and templates
        _handle_start_solutions: Handles solution file initialization 
        _handle_start_template: Updates project title in files
"""

# Python Standard Library
from datetime import datetime
import os
import shutil

# Third-Party Libraries

# Local
from src.config import ConfigManager
from src.config import ROOT_DIR_1
from src.config import ROOT_DIR_2
from src.utils import HYPHEN
from src.utils import INDEX_START
from src.utils import INDEX_END





ROOT_DIR = ROOT_DIR_1

if not os.path.exists(os.path.join(ROOT_DIR_1, 'src')):
    ROOT_DIR = ROOT_DIR_2










def _handle_start_dirs(
        root_dir: str
    ) -> str:
    """
    Create backup directory for project initialization files.
    
    Returns
    -------
    str
        Path to the created backup directory
    
    Example
    -------
    'root_dir/assets/start/2025-03-15_start_bak'
    """
    assets_dir = os.path.join(root_dir, 'assets')
    start_dir = os.path.join(assets_dir, 'start')
    bak_dir = os.path.join(start_dir, f'{datetime.now().strftime("%Y-%m-%d")}_start_bak')

    os.makedirs(bak_dir, exist_ok=True)

    return bak_dir


def _handle_start_backup(
        input_path: str,
        output_path: str
    ) -> int:
    """
    Create a backup copy of specified file in backup directory.
    
    Parameters
    ----------
    input_path : str
        Path to the file to backup
    output_path : str
        Directory to store the backup file
        
    Returns
    -------
    int
        1 if backup successful
    """
    file_name = os.path.basename(input_path)
    bak_name = f'{file_name}.bak'
    bak_path = os.path.join(output_path, bak_name)

    shutil.copy2(input_path, bak_path)

    return 1


def _handle_start_file(
        input_dir: str,
        input_file: str,
        bak_dir: str,
        output_dir: str,
        output_file: str
    ) -> int:
    """
    Handle file operations including backup, move/copy, and cleanup.

    Parameters
    ----------
    input_dir : str
        Source directory containing the file
    input_file : str
        Name of the file to process
    bak_dir : str
        Directory to store backup files
    output_dir : str
        Destination directory for the file
    output_file : str
        New name for the file at destination

    Returns
    -------
    int
        1 if operations successful
    """
    input_file_path = os.path.join(input_dir, input_file)

    # Step 1: Create a backup copy
    _handle_start_backup(input_file_path, bak_dir)

    # Step 2: Move files (or rename files if already at destination dir)
    if output_dir and output_file:
        shutil.copy(input_file_path, os.path.join(output_dir, output_file))

    # Step 3: Remove file
    os.remove(input_file_path)


    return 1


def _handle_start_files(
        root_dir: str,
        bak_dir: str
    ) -> int:
    """
    Handle all project initialization of files.
    
    Parameters
    ----------
    bak_dir : str
        Directory to store backup files
        
    Returns
    -------
    int
        1 if all file operations successful
    
    Notes
    -----
    Current list of files to handle:
    README.md
    README.template.md
    settings.json
    settings.template.json
    renovate.json
    codecov.yaml
    
    Example args passed to _handle_start_file():
    (1) root/full/path/eevveerryyddaayy
    (2) root/full/path/eevveerryyddaayy/README.md
    (3) root/full/path/eevveerryyddaayy/assets/start/2025-03-15_start_bak
    (4) root/full/path/eevveerryyddaayy/docs
    (5) README.md
    """
    # README.md
    _handle_start_file(root_dir,
                        'README.md',
                        bak_dir,
                        os.path.join(root_dir, 'docs'),
                        'README.md')

    # README.template.md
    _handle_start_file(root_dir,
                        'README.template.md',
                        bak_dir,
                        root_dir,
                        'README.md')

    # settings.json
    _handle_start_file(os.path.join(root_dir, '.vscode'),
                        'settings.json',
                        bak_dir,
                        '',
                        '')

    # settings.template.json
    _handle_start_file(os.path.join(root_dir, '.vscode'),
                        'settings.template.json',
                        bak_dir,
                        os.path.join(root_dir, '.vscode'),
                        'settings.json')

    # renovate.json
    _handle_start_file(root_dir,
                       'renovate.json',
                       bak_dir,
                       '',
                       '')

    # api.yaml
    _handle_start_file(os.path.join(root_dir, '.github/workflows'),
                       'codecov.yaml',
                       bak_dir,
                       '',
                       '')


    return 1


def _handle_start_date(
        config: ConfigManager
    ) -> int:
    """
    Update the project start date in configuration file.

    Parameters
    ----------
    config : ConfigManager
        Custom container for validating, storing and retrieving application settings

    Returns
    -------
    int
        1 if update successful
    """
    today = datetime.now().strftime(f'%Y{HYPHEN}%m{HYPHEN}%d')

    config_proj_file_path = os.path.join(ROOT_DIR, config.get('CONFIG_DIR'), 'config_proj.py')

    with open(config_proj_file_path, 'r+', encoding='utf-8') as file:
        lines = file.readlines()

        for i, line in enumerate(lines):

            if line.startswith('PROJ_START='):
                lines[i] = f'PROJ_START=\'{today}\'\n'

        file.seek(0)
        file.writelines(lines)
        file.truncate()

    return 1


def _handle_start_solutions(
        config: ConfigManager
    ) -> int:
    """
    Create solutions directory.

    Ensures there is a directory for storing solution files.

    Parameters
    ----------
    config : ConfigManager
        Custom container for validating, storing and retrieving application settings

    Returns
    -------
    int
        1 if directory creation successful or
        0 if directory creation failed
    """
    solutions_dir = os.path.join(ROOT_DIR, config.get('SOLUTIONS_DIR'))

    try:
        if not os.path.exists(solutions_dir):
            os.makedirs(solutions_dir)

        return 1
    except OSError:
        return 0


def _handle_start_configs_form(
        config: ConfigManager,
        file_path: str
    ) -> int:
    """
    Update config_form.py with user-selected site options.

    Parameters
    ----------
    config : ConfigManager
        Configuration manager instance
    file_path : str
        Path to the form configuration file

    Returns
    -------
    int
        1 if update successful
    """
    with open(file_path, 'r+', encoding='utf-8') as file:
        lines = file.readlines()

        for i, line in enumerate(lines):

            if line.startswith('SITE_OPTIONS='):
                lines[i] = f"SITE_OPTIONS={config.get('SITE_OPTIONS')}\n"

        file.seek(0)
        file.writelines(lines)
        file.truncate()


    return 1


def _handle_start_configs_index(
        config: ConfigManager,
        file_path: str
    ) -> int:
    """
    Update config_index.py file with user-selected settings.

    Parameters
    ----------
    config : ConfigManager
        Configuration manager instance
    file_path : str
        Path to the index configuration file

    Returns
    -------
    int
        1 if update successful
    """
    with open(file_path, 'r+', encoding='utf-8') as file:
        lines = file.readlines()

        for i, line in enumerate(lines):

            if line.startswith('NB='):
                lines[i] = f"NB={config.get('NB')}\n"

            if line.startswith('NB_NAME='):
                lines[i] = f"NB_NAME=\'{config.get('NB_NAME')}\'\n"

            if line.startswith('SEQ_NOTATION='):
                lines[i] = f"SEQ_NOTATION={config.get('SEQ_NOTATION')}\n"

            if line.startswith('SEQ_SPARSE='):
                lines[i] = f"SEQ_SPARSE={config.get('SEQ_SPARSE')}\n"

        file.seek(0)
        file.writelines(lines)
        file.truncate()


    return 1


def _handle_start_configs_proj(
        config: ConfigManager,
        file_path: str
    ) -> int:
    """
    Update config_proj.py file with user-selected settings.

    Parameters
    ----------
    config : ConfigManager
        Configuration manager instance
    file_path : str
        Path to the index configuration file

    Returns
    -------
    int
        1 if update successful
    """
    with open(file_path, 'r+', encoding='utf-8') as file:
        lines = file.readlines()

        for i, line in enumerate(lines):

            if line.startswith('PROJ_TITLE='):
                lines[i] = f"PROJ_TITLE=\'{config.get('PROJ_TITLE')}\'\n"

        file.seek(0)
        file.writelines(lines)
        file.truncate()


    return 1


def _handle_start_configs(
        config: ConfigManager,
        root_dir: str = ROOT_DIR
    ) -> int:
    """
    Coordinate updates to configuration files with user-selected settings.

    Parameters
    ----------
    config : ConfigManager
        Configuration manager instance

    Returns
    -------
    int
        1 if all updates successful

    Notes
    -----
    Updates the following config files:
    - config_form.py: Options for Site field in Jupyter IPywidgets form
    - config_index.py: Index table settings in README.md
    - config_proj.py: Project title
    """
    # UPDATE config_form.py
    config_form_file_path = os.path.join(root_dir,
                                         config.get('CONFIG_DIR'),
                                         'config_form.py')
    _handle_start_configs_form(config, config_form_file_path)

    # UPDATE config_index.py
    config_index_file_path = os.path.join(root_dir,
                                         config.get('CONFIG_DIR'),
                                         'config_index.py')
    _handle_start_configs_index(config, config_index_file_path)

    # UPDATE config_proj.py
    config_proj_file_path = os.path.join(root_dir,
                                         config.get('CONFIG_DIR'),
                                         'config_proj.py')
    _handle_start_configs_proj(config, config_proj_file_path)


    return 1


def _handle_start_readme(
        config: ConfigManager,
        package_changes: dict,
        root_dir: str = ROOT_DIR
    ) -> int:
    """
    Update project title and index table settings in README.md.

    Parameters
    ----------
    config : ConfigManager
        Custom container for validating, storing and retrieving application settings

    Returns
    -------
    int
        1 if notebook initialization successful

    Notes
    -----
    Updates both README.md index table and solution template files
    with the configured notebook column name
    """
    readme_file_path = os.path.join(root_dir, 'README.md')

    nb_name = config.get('NB_NAME')

    index_header = {
        'labels': f'| Day   | Title   | Solution   | Site   | Difficulty   | {nb_name}   |',
        'sep': f'| ----- | ------- | ---------- | ------ | ------------ | { "-" * (len(nb_name) + 2) } |'
    }

    start_line_readme = None
    end_line_readme = None
    lines_readme = []

    with open(readme_file_path, 'r+', encoding='utf-8') as file:
        lines_readme = file.readlines()

        # HANDLE README CHANGES - TITLE
        if 'PROJ_TITLE' in package_changes.keys():
            lines_readme[0] = f'# {config.get("PROJ_TITLE")}\n'

        # HANDLE README CHANGES - NB
        if 'NB' in package_changes.keys() and 'NB_NAME' in package_changes.keys():
            for i in range(len(lines_readme)-1, -1, -1):

                if INDEX_START in lines_readme[i]:
                    start_line_readme = i

                if INDEX_END in lines_readme[i]:
                    end_line_readme = i

            lines_readme[start_line_readme + 1] = f'{index_header["labels"]}\n'
            lines_readme[start_line_readme + 2] = f'{index_header["sep"]}\n'

            for j in range(start_line_readme + 3, end_line_readme):

                lines_readme[j] = ''

            print(f'Extra column selected: {nb_name}')

        file.seek(0)
        file.writelines(lines_readme)
        file.truncate()

    return 1


def _handle_start_template(
        config : ConfigManager,
        package_changes: dict,
        root_dir: str = ROOT_DIR
    ) -> int:
    """
    Update project title and optional sixth column settings in template file.

    Parameters
    ----------
    config : ConfigManager
        Custom container for validating, storing and retrieving application settings

    Returns
    -------
    int
        1 if title update successful
    """
    solutions_file_path = os.path.join(root_dir,
                                       config.get('TEMPLATES_DIR'),
                                       'solution.txt')

    lines_template = []

    with open(solutions_file_path, 'r+', encoding='utf-8') as file:
        lines_template = file.readlines()

        # HANDLE TEMPLATE CHANGES - TITLE
        if 'PROJ_TITLE' in package_changes.keys():
            lines_template[0] = f"# {config.get('PROJ_TITLE')} \\#{{{{ seq_full }}}}\n"

        # HANDLE TEMPLATE CHANGES - NB
        if 'NB' in package_changes.keys() and 'NB_NAME' in package_changes.keys():
            lines_template[29] = f'## {config.get("NB_NAME")}\n'
            lines_template[32] = '\n'

        file.seek(0)
        file.writelines(lines_template)
        file.truncate()


    return 1


def handle_start(
        config: ConfigManager,
        package_changes: dict,
        root_dir: str = ROOT_DIR
    ) -> int:
    """
    Coordinate the project initialization process.

    Parameters
    ----------
    config : ConfigManager
        Configuration manager instance
    package_changes : dict
        Dictionary of configuration changes to apply

    Returns
    -------
    int
        1 if all initialization steps successful

    Notes
    -----
    Manages all aspects of project setup including:
    - Creating backup directories
    - Processing initialization files
    - Setting project start date
    - Creating solutions directory
    - Updating all configuration files
    - Modifying README and template files
    """
    # HANDLE BACKUP DIR
    bak_dir = _handle_start_dirs(root_dir)

    # HANDLE FILES
    _handle_start_files(root_dir, bak_dir)

    # HANDLE PROJECT START DATE
    _handle_start_date(config)

    # HANDLE SOLUTIONS DIRECTORY
    _handle_start_solutions(config)

    if len(package_changes) > 0:
        # print(json.dumps(package_changes, indent=4))

        # HANDLE CONFIG FILES
        _handle_start_configs(config)

        if 'PROJ_TITLE' in package_changes.keys() or 'NB' in package_changes.keys():
            # HANDLE README
            _handle_start_readme(config, package_changes)

            # HANDLE TEMPLATE FILE
            _handle_start_template(config, package_changes)

    return 1
