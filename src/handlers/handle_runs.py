"""
Project Run Handlers

This module handles new project entries through utility functions that 
process form inputs from Jupyter IPyWidgets. It manages the entire entry
workflow including:

1. Data preparation - Sanitizing user inputs and deriving new data such as
   sequence identifiers, filenames, and index table values
2. Data storage - Storing processed information in dictionary-based 
   containers and updating values as needed
3. Implementation - Generating new solution files and updating the Index 
   table in README.md with the new entries

The module supports standardized project management through consistent 
naming conventions, sequencing, and organization of entries.

Functions:
    Public:
        handle_runs_main: Main entry point that coordinates the entire workflow

    Private (internal use only):
        _handle_runs_prep_*: Prepare sequences, filenames, and data
        _handle_runs_implement: Creates files and updating indexes
        _handle_runs_close: Updates configuration settings
"""

# Python Standard Library
from datetime import datetime, timedelta
import json
import os
import re
from typing import Any, Dict, Optional, Tuple, Union

# Third-Party Libraries
from jinja2 import Environment

# Local
from src.config import ConfigManager
from src.config import ROOT_DIR_1
from src.config import ROOT_DIR_2
from src.utils import HYPHEN
from src.utils import INDEX_START
from src.utils import INDEX_END
from src.utils import PackageManager
from src.utils import clean_strings
from src.utils import get_target_line_dict
from src.utils import get_target_line_updated





ROOT_DIR = ROOT_DIR_1

if not os.path.exists(os.path.join(ROOT_DIR_1, 'src')):
    ROOT_DIR = ROOT_DIR_2










def _handle_runs_prep_seq_files(
        today: datetime,
        file_last: str,
        seq_notation_loc: int,
        seq_start_loc: str,
        hyphen: str = HYPHEN
    ) -> Tuple[str, str, Optional[Union[int, datetime.date]], Union[int, datetime.date]]:
    """
    Generate sequence when files exist in the directory.

    Parameters
    ----------
    today : datetime
        Current timestamp for sequence generation
    file_last : str
        Name of last file in directory
    seq_notation_loc : int
        Sequence notation type (0 for numeric, 1 for date-based)
    seq_start_loc : str
        Project start date for sequence calculation
    hyphen : str, optional
        Hyphen character to use in date formatting, by default HYPHEN

    Returns
    -------
    str
        Full sequence ID with suffix (e.g. "001_01" or "2025‑01‑31_01")
    str
        Main sequence part (e.g. "001" or "2025‑01‑31")
    Optional[Union[int, datetime.date]]
        Previous sequence number or date
    Union[int, datetime.date]
        Current sequence number or date

    Raises
    ------
    ValueError
        If seq_notation_loc is invalid
    """
    seq_next_full_str = ''

    # Handle sequence partials (main and suffix)
    if seq_notation_loc == 0:
        seq_last_main = int(file_last[:3])
        seq_last_suffix = int(file_last[4:6])

        seq_next_main = datetime.strptime(seq_start_loc, f'%Y{hyphen}%m{hyphen}%d').date()
        seq_next_main = (today.date() - seq_next_main).days + 1
        seq_next_main_str = f'{seq_next_main:03d}'

    elif seq_notation_loc == 1:
        seq_last_main = datetime.strptime(file_last[:10], f'%Y{hyphen}%m{hyphen}%d').date()
        seq_last_suffix = int(file_last[11:13])

        seq_next_main = today.date()
        seq_next_main_str = seq_next_main.strftime(f'%Y{hyphen}%m{hyphen}%d')

    else:
        raise ValueError('Invalid configuration: TODO')

    # Handle full sequence
    if seq_last_main == seq_next_main:
        seq_next_suffix = seq_last_suffix + 1
        seq_next_suffix_str = f'{seq_next_suffix:02d}'
        seq_next_full_str = f'{seq_next_main_str}_{seq_next_suffix_str}'
        print('Note: You have submitted more than 1 entry today.')

    elif seq_last_main < seq_next_main:
        seq_next_suffix_str = '01'
        seq_next_full_str = f'{seq_next_main_str}_{seq_next_suffix_str}'

    else:
        print('Note: Invalid sequence. Processing not terminated.')

    return seq_next_full_str, seq_next_main_str, seq_last_main, seq_next_main


def _handle_runs_prep_seq_no_files(
        today: datetime,
        seq_notation_loc: int,
        hyphen: str = HYPHEN
    ) -> Tuple[str, str, Optional[Union[int, datetime.date]], Union[int, datetime.date]]:
    """
    Generate sequence when no files exist in the directory.

    Parameters
    ----------
    today : datetime
        Current timestamp for sequence generation
    seq_notation_loc : int
        Sequence notation type (0 for numeric, 1 for date-based)

    Returns
    -------
    str
        Full sequence ID with suffix (e.g. "001_01" or "2025‑01‑31_01")
    str
        Main sequence part (e.g. "001" or "2025‑01‑31")
    Optional[Union[int, datetime.date]]
        Previous sequence number or date (None for first entry)
    Union[int, datetime.date]
        Current sequence number or date (None for first entry)

    Raises
    ------
    ValueError
        If seq_notation_loc is not 0 or 1
    """
    seq_last_main = None
    seq_next_main = None

    if seq_notation_loc == 0:

        seq_next_main_str = '001'
        seq_next_suffix_str = '01'
        seq_next_full_str = f'{seq_next_main_str}_{seq_next_suffix_str}'

    elif seq_notation_loc == 1:

        seq_next_main_str = today.strftime(f'%Y{hyphen}%m{hyphen}%d')
        seq_next_suffix_str = '01'
        seq_next_full_str = f'{seq_next_main_str}_{seq_next_suffix_str}'

    else:

        raise ValueError('Invalid configuration: Expected 0 or 1.')

    return seq_next_full_str, seq_next_main_str, seq_last_main, seq_next_main


def _handle_runs_prep_seq(
        config: ConfigManager,
        today: datetime
    ) -> Tuple[str, str, Optional[Union[int, datetime.date]], Union[int, datetime.date]]:
    """
    Generate sequence identifier for Index table entries and solution filenames.

    Parameters
    ----------
    config : ConfigManager
        Configuration manager containing application settings
    today : datetime
        Current timestamp for sequence generation

    Returns
    -------
    str
        Full sequence ID with suffix (e.g. "001_01" or "2025‑01‑31_01")
    str
        Main sequence part (e.g. "001" or "2025‑01‑31")
    Optional[Union[int, datetime.date]]
        Previous sequence number or date (None if first entry)
    Union[int, datetime.date]
        Current sequence number or date

    Raises
    ------
    ValueError
        If seq_notation_loc configuration is not 0 or 1

    Notes
    -----
    Sequence format is determined by seq_notation_loc:
    - 0: Three digit sequence (e.g. "001")
    - 1: Date format with Unicode non-breaking hyphens U+2011 (e.g. "2025‑01‑31")
    """
    seq_start_loc = config.get('PROJ_START')
    seq_notation_loc = config.get('SEQ_NOTATION')

    with os.scandir(config.get('SOLUTIONS_DIR')) as entries:
        files = sorted(entry.name for entry in entries)

    if files:
        return _handle_runs_prep_seq_files(today, files[-1], seq_notation_loc, seq_start_loc)

    return _handle_runs_prep_seq_no_files(today, seq_notation_loc)


def _handle_runs_prep_file(
        title: str,
        seq_full: str
    ) -> str:
    """
    Create a standardized filename from title and sequence identifier.
    
    Parameters
    ----------
    title : str
        Problem title to be converted into filename
    seq_full : str
        Full sequence identifier with suffix
    
    Returns
    -------
    str
        Formatted filename in the pattern "{seq_full}_{sanitized_title}.md"
        
    Notes
    -----
    Sanitizes the title by:
    - Converting to lowercase
    - Removing special characters
    - Replacing spaces and hyphens with underscores
    """
    filename = title.lower()
    filename = re.sub(r'[^a-z0-9\s-]', '', filename)
    filename = filename.strip()
    filename = filename.replace(' ', '_')
    filename = filename.replace('-', '_')
    filename = f'{seq_full}_{filename.strip()}.md'

    return filename


def _handle_runs_prep_index_num_seq(
        seq_last: int,
        seq_next: int,
        lines: list,
        target_line: int,
        gap_line: str
    ) -> list:
    """Handle numeric sequence gaps (e.g., 001, 002, etc.)"""
    max_gap = 30

    if seq_next <= seq_last:
        raise ValueError(f"Invalid sequence: next ({seq_next}) must be greater than last ({seq_last})")

    gap_size = seq_next - seq_last - 1
    if gap_size > max_gap:
        raise ValueError(f"Gap size ({gap_size}) exceeds maximum allowed ({max_gap})")

    if gap_size > 0:
        count = 0
        for i in range(seq_last + 1, seq_next):
            seq_gap_str = f'{i:03d}'
            lines.insert(target_line + count, f'| {seq_gap_str}   {gap_line}')
            count += 1

    return lines


def _handle_runs_prep_index_date_seq(
        seq_last: datetime.date,
        seq_next: datetime.date,
        lines: list,
        target_line: int,
        gap_line: str,
        hyphen: str
    ) -> list:
    """Handle date sequence gaps (e.g., 2025-01-01)"""
    max_gap = 30

    days_difference = (seq_next - seq_last).days

    if days_difference > 1:
        if days_difference > max_gap:
            raise ValueError(f"Date gap exceeds maximum allowed ({max_gap} days)")

        seq_bound = seq_next
        count = 0
        seq_gap = seq_last + timedelta(days=1)

        while seq_gap < seq_bound:
            seq_gap_str = seq_gap.strftime(f'%Y{hyphen}%m{hyphen}%d')
            lines.insert(target_line + count, f'| {seq_gap_str}   {gap_line}')
            count += 1
            seq_gap += timedelta(days=1)

    return lines


def _handle_runs_prep_index(
        config: ConfigManager,
        seq_last: Optional[Union[int, datetime.date]],
        seq_next: Union[int, datetime.date],
        root_dir: str = ROOT_DIR,
        hyphen: str = HYPHEN,
        index_end: str = INDEX_END
    ) -> int:
    """
    Fill gaps in Index table with empty rows based on sequence notation.
    
    Parameters
    ----------
    config : ConfigManager
        Custom container for validating, storing and retrieving application settings
    seq_last : Optional[Union[int, datetime.date]]
        Previous sequence number or date
    seq_next : Union[int, datetime.date]
        Current sequence number or date
        
    Returns
    -------
    int
        1 if successful
        
    Raises
    ------
    ValueError
        If sequence notation configuration is invalid
        
    Notes
    -----
    For date-based sequences, creates entries for each missing day.
    For numeric sequences, creates entries for each missing number.
    Gap entries are added to maintain continuity in the index table.
    """
    if seq_last is not None or seq_next is not None:
        readme_file_path = os.path.join(root_dir, 'README.md')

        if config.get('NB') == 1:
            gap_line = '|    |    |    |    |    |\n'
        else:
            gap_line = '|    |    |    |    |\n'

        with open(readme_file_path, 'r+', encoding='utf-8') as file:
            lines = file.readlines()

            target_line = len(lines) - 1
            while target_line >= 0:
                if index_end in lines[target_line]:
                    break
                target_line -= 1

            if target_line < 0:
                raise ValueError(f"Index end marker '{index_end}' not found in file")

            seq_notation = config.get('SEQ_NOTATION')

            if seq_notation == 0:
                lines = _handle_runs_prep_index_num_seq(seq_last,
                                                        seq_next,
                                                        lines,
                                                        target_line,
                                                        gap_line)
            elif seq_notation == 1:
                lines = _handle_runs_prep_index_date_seq(seq_last,
                                                         seq_next,
                                                         lines,
                                                         target_line,
                                                         gap_line,
                                                         hyphen)
            else:
                raise ValueError('Invalid configuration: SEQ_NOTATION is 0 or 1.')

            file.seek(0)
            file.writelines(lines)
            file.truncate()

    return 1


def _handle_runs_prep_package(
        package: PackageManager,
        seq: str,
        seq_full: str,
        new_package: Dict[str, str],
        filename: str
    ) -> int:
    """
    Update PackageManager dictionaries with new entry information.
    
    Parameters
    ----------
    package : PackageManager
        Custom container for storing and retrieving form data and derived values
    seq : str
        Main sequence identifier
    seq_full : str
        Full sequence identifier with suffix
    new_package : Dict[str, str]
        Dictionary containing problem information
    filename : str
        Generated filename for the solution
    
    Returns
    -------
    int
        1 if update successful
        
    Notes
    -----
    Updates:
    - package dictionary: Stores data submitted through form
    - package_widths dictionary: Stores column width calculations for display formatting
    """
    # Update package
    package.update_value('package', 'day', seq)
    package.update_value('package', 'url', new_package["url"])
    package.update_value('package', 'title', new_package["title"])
    package.update_value('package', 'title_index', f'[{new_package["title"]}]({new_package["url"]})')
    package.update_value('package', 'solution', f'[Solution](solutions/{filename})')
    package.update_value('package', 'site', new_package["site"])
    package.update_value('package', 'difficulty', new_package["difficulty"])
    package.update_value('package', 'problem', new_package["problem"])
    package.update_value('package', 'submitted_solution', new_package["submitted_solution"])
    package.update_value('package', 'site_solution', new_package["site_solution"])
    package.update_value('package', 'notes', new_package["notes"])
    package.update_value('package', 'nb', new_package["nb"])
    package.update_value('package', 'seq_full', seq_full)
    package.update_value('package', 'filename', filename)

    # Update entry_data_widths
    package.update_value('package_widths', 'day', len(seq) + 2)
    package.update_value('package_widths', 'title', len(f'[{new_package["title"]}]({new_package["url"]})') + 2)
    package.update_value('package_widths', 'solution', len(f'[Solution](solutions/{filename})') + 2)
    package.update_value('package_widths', 'site', len(new_package["site"]) + 2)
    package.update_value('package_widths', 'difficulty', len(new_package["difficulty"]) + 2)
    package.update_value('package_widths', 'nb', len(new_package["nb"]) + 2)


    return 1


def _handle_runs_prep(
        config: ConfigManager,
        package: PackageManager,
        data: Dict[str, str], today: datetime
    ) -> int:
    """
    Set up runs by processing project information and updating dictionaries.

    Parameters
    ----------
    config : ConfigManager
        Custom container for validating, storing and retrieving application settings
    package : PackageManager
        Custom container for storing and retrieving form data and derived values
    data : Dict[str, str]
        Dictionary containing form input data
    today : datetime
        Current date for timestamp generation

    Returns
    -------
    int
        1 if successful

    Raises
    ------
    ValueError
        If configuration settings are invalid
    
    Notes
    -----
    Updates:
    - package.package: Core project information and metadata
    - package.package_widths: Column width calculations
    
    Form data validation is expected to be done elsewhere.
    Does not update config.COLS_WIDTH dictionary.
    """
    # Prepare sequence
    seq_next_full_str, seq_next_main_str, seq_last_main, seq_next_main = _handle_runs_prep_seq(config, today)

    # Prepare filename
    filename = _handle_runs_prep_file(data['title'], seq_next_full_str)

    # Prepare Index
    if config.get('SEQ_SPARSE') == 1:
        _handle_runs_prep_index(config, seq_last_main, seq_next_main)

    # Update PackageHandler dicts
    _handle_runs_prep_package(package, seq_next_main_str, seq_next_full_str, data, filename)

    return 1


def _handle_runs_implement_file(
        config: ConfigManager,
        data: Dict[str, Any],
        root_dir: str = ROOT_DIR
    ) -> int:
    """
    Create a solution file using a template and provided data.

    Parameters
    ----------
    config : ConfigManager
        Custom container for validating, storing and retrieving application settings
    data : Dict[str, Any]
        Dictionary containing template variables including "filename"

    Returns
    -------
    int
        1 on successful file creation
    """
    template_file_path = os.path.join(root_dir, config.get("TEMPLATES_DIR"), 'solution.txt')
    with open(template_file_path, 'r', encoding='utf-8') as file:
        template_content = file.read()

    # Create a Jinja2 template object
    env = Environment(autoescape=True)
    template = env.from_string(template_content)

    # Render the template with the data
    filled_document = template.render(data)

    new_file_path = os.path.join(root_dir, 'solutions', data["filename"])
    with open(new_file_path, 'w', encoding='utf-8') as file:
        file.write(filled_document)

    return 1


def _handle_runs_implement_config(
        config: ConfigManager,
        package: PackageManager
    ) -> int:
    """
    TD
    """
    is_cols_width_changed = 0
    for key, config_value in config.get('COLS_WIDTH').items():
        package_value = package.get_dictionary('package_widths')[key]
        if package_value < config_value:
            package.update_value('package_widths', key, config_value)
            is_cols_width_changed = 1

    return is_cols_width_changed


def _handle_runs_implement_index(
        config: ConfigManager,
        package: PackageManager,
        is_cols_width_changed: int,
        root_dir: str = ROOT_DIR,
        index_start: str = INDEX_START,
        index_end: str = INDEX_END
    ) -> int:
    """
    Process new entries by creating files and updating the Index table.

    Parameters
    ----------
    config : ConfigManager
        Custom container for validating, storing and retrieving application settings
    package : PackageManager
        Custom container for storing and retrieving form data and derived values

    Returns
    -------
    int
        1 if successful

    Notes
    -----
    Updates:
    - Creates new solution file based on package data
    - Updates package_widths if necessary based on config.COLS_WIDTH
    - Adds new entry line to README.md index
    - Updates existing index lines if column widths changed

    Prerequisites:
    - Properly initialized configuration
    - Properly updated package dictionaries
    - Valid README.md with index block markers
    """
    # CREATE NEW LINE
    if package.get_value('package', 'nb') == 'TBD':
        package.update_value('package', 'nb_index', '')

    new_entry = get_target_line_updated(False,
                                        config,
                                        package,
                                        data=None)

    readme_file_path = os.path.join(root_dir, 'README.md')
    with open(readme_file_path, 'r+', encoding='utf-8') as file:
        lines = file.readlines()

        start_line = None
        end_line = None

        # GET START AND END LINES OF INDEX
        for i, line in enumerate(lines):
            if index_start in line:
                start_line = i  # Line numbers start from 1
            if index_end in line:
                end_line = i

        # UPDATE TARGET LINES (if needed)
        if is_cols_width_changed == 1:

            # Process each line between start_line and end_line
            for i in range(start_line + 1, end_line):

                # Convert target line (str) to data (dict)
                target_line_data = get_target_line_dict(config.get('NB'),
                                                        lines[i])

                # Update target line
                is_second_line = bool(i == start_line + 2)

                line_updated = get_target_line_updated(is_second_line,
                                                       config,
                                                       package,
                                                       data=target_line_data)

                # Replace the original line with the updated one
                lines[i] = f'{line_updated}\n'

        # INSERT NEW LINE TO LINES
        lines.insert(end_line, f'{new_entry}\n')

        file.seek(0)
        file.writelines(lines)
        file.truncate()

    return 1


def _handle_runs_close(
        config: ConfigManager,
        column_widths: Dict[str, int],
        root_dir: str = ROOT_DIR
    ) -> int:
    """
    Update the COLS_WIDTH configuration with new column width values.
    
    Parameters
    ----------
    config : ConfigManager
        Custom container for validating, storing and retrieving application settings
    column_widths : Dict[str, int]
        Dictionary containing column width values
    
    Returns
    -------
    int
        1 on successful completion
        
    Notes
    -----
    Updates the config_index.py file by replacing the COLS_WIDTH dictionary
    with updated values serialized as JSON.
    """
    config_index_path = os.path.join(root_dir, config.get('CONFIG_DIR'), 'config_index.py')
    with open(config_index_path, 'r+', encoding='utf-8') as file:
        lines = file.readlines()

        line_target = None
        for i, line in enumerate(lines):
            if 'COLS_WIDTH = {' in line:
                line_target = i
                break

        del lines[line_target:]

        data = f'COLS_WIDTH = {json.dumps(column_widths, indent=4)}\n'

        lines[line_target:line_target] = data.splitlines(True)

        file.seek(0)
        file.writelines(lines)
        file.truncate()


    return 1


def handle_runs_main(
        config: ConfigManager,
        package: PackageManager,
        data: Dict[str, Any],
        today: datetime
    ) -> int:
    """
    Coordinate the execution flow for processing form inputs and updating project files.
    
    Parameters
    ----------
    config : ConfigManager
        Custom container for validating, storing and retrieving application settings
    package : PackageManager
        Custom container for storing and retrieving form data and derived values
    data : Dict[str, Any]
        Dictionary containing form input data
    today : datetime
        Current date for timestamp generation

    Returns
    -------
    int
        1 if successful

    Notes
    -----
    Flow:
    1. Validates and cleans input strings
    2. Initiates run configuration process
    3. Implements run settings by creating files and updating index table
    4. Updates configuration column widths for future entries
    """
    # REVIEW DATA FROM FORM
    # print(json.dumps(data, indent=4))

    # PREPARE DATA FROM FORM
    if data['nb'] is None:
        data['nb'] = 'TBD'
    data = clean_strings(data)

    # RUNS - START (FIRST OR REGULAR)
    _handle_runs_prep(config, package, data, today)

    # RUNS - IMPLEMENT - FILE
    _handle_runs_implement_file(config, package.get_dictionary('package'))

    # RUNS - IMPLEMENT - CONFIG - COLS WIDTHS
    is_cols_width_changed = _handle_runs_implement_config(config, package)

    # RUNS - IMPLEMENT - INDEX
    _handle_runs_implement_index(config, package, is_cols_width_changed)

    # RUNS - CLOSE
    _handle_runs_close(config, package.get_dictionary('package_widths'))


    return 1
