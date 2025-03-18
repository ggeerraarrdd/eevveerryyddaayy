"""
Utility Functions for Project Runs
"""

# Python Standard Library
import os
from typing import Dict

# Local
from src.config import ConfigManager
from src.config import ROOT_DIR_1
from src.config import ROOT_DIR_2
from src.utils import PackageManager





ROOT_DIR = ROOT_DIR_1

if not os.path.exists(os.path.join(ROOT_DIR_1, 'src')):
    ROOT_DIR = ROOT_DIR_2










def clean_strings(
        data: Dict[str, str]
    ) -> Dict[str, str]:
    """
    Remove newline characters from string values in a dictionary.

    Parameters
    ----------
    data : Dict[str, str]
        Dictionary containing string values to clean

    Returns
    -------
    Dict[str, str]
        Cleaned dictionary with newlines removed from string values
    """
    cleaned_dict = {}
    for key, value in data.items():
        if isinstance(value, str):
            cleaned_dict[key] = value.strip('\n')
        else:
            cleaned_dict[key] = value
    return cleaned_dict


def get_target_line_dict(
        nb_loc: int,
        line: str
    ) -> Dict[str, str]:
    """
    Parse a table line into a dictionary based on notebook configuration.

    Parameters
    ----------
    nb_loc : int
        Notebook configuration value determining parsing behavior
    line : str
        String containing pipe-separated table data

    Returns
    -------
    Dict[str, str]
        Dictionary with parsed table data fields

    Raises
    ------
    ValueError
        If notebook configuration is invalid
    """
    data = {
        'day': '',
        'title': '',
        'solution': '',
        'site': '',
        'difficulty': '',
        'nb': '',
    }

    if nb_loc == 0:
        keys = list(data.keys())[:-1]  # Exclude 'nb'
    elif nb_loc == 1:
        keys = list(data.keys())
    else:
        raise ValueError('Invalid configuration: NB must be 0 or 1.')

    segments = []
    for segment in line.split('|'):
        segment = segment.strip()
        if segment:
            segments.append(segment)

    for i, key in enumerate(keys):
        if i < len(segments):
            data[key] = f'{segments[i]}'

    results = data

    return results


def get_target_line_updated(
        is_second_line: bool,
        config: ConfigManager,
        package: PackageManager,
        data: Dict[str, str]
    ) -> str:
    """
    Format a table line with proper padding based on column widths.

    Parameters
    ----------
    is_second_line : bool
        Boolean indicating if this is the second line of Index table
    config : ConfigManager
        Custom container for validating, storing and retrieving application settings
    package : PackageManager
        Custom container for storing and retrieving form data and derived values
    data : Dict[str, str]
        Dictionary containing table cell values

    Returns
    -------
    str
        Formatted table line with proper padding

    Raises
    ------
    ValueError
        If notebook configuration is invalid
    """
    nb_local = config.get('NB')
    widths = package.get_dictionary('package_widths')

    if data is None:
        data_dict = package.get_dictionary('package')
        data = {
            'day': data_dict['day'],
            'title': data_dict['title'],
            'solution': data_dict['solution'],
            'site': data_dict['site'],       
            'difficulty': data_dict['difficulty'],
            'nb': data_dict['nb'],
        }

    target_line = '|'

    if nb_local == 0:

        for key, value in data.items():

            if key != 'nb':  # Skip the "nb" key

                value_str = str(value)
                diff = widths[key] - len(value_str)

                if is_second_line is True:
                    padding = '-' * diff
                else:
                    padding = ' ' * diff

                target_line += f' {value_str}{padding} |'

    elif nb_local == 1:

        for key, value in data.items():

            value_str = str(value)
            diff = widths[key] - len(value_str)

            if is_second_line is True:
                padding = '-' * diff
            else:
                padding = ' ' * diff

            target_line += f' {value_str}{padding} |'

    else:

        raise ValueError('Invalid configuration: NB must be 0 or 1')

    results = target_line


    return results
