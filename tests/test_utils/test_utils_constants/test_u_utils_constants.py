"""
Test the constants in utils_constants.py
"""

import os

from src.utils.utils_constants import HYPHEN
from src.utils.utils_constants import INDEX_START
from src.utils.utils_constants import INDEX_END
from src.utils.utils_constants import FIRST_ROW
from src.utils.utils_constants import SECOND_ROW










def test_utils_constants():
    """Test that utils_constants.py has the expected constants"""    
    # Test file exists
    constants_path = os.path.join('src', 'utils', 'utils_constants.py')
    assert os.path.exists(constants_path)

    # Test number of constants
    with open(constants_path, 'r', encoding='utf-8') as file:
        content = file.read()
        # Count actual constant assignments (excluding comments/docstrings)
        constants_count = 0
        for line in content.split('\n'):
            if '=' in line and not line.strip().startswith('#'):
                constants_count += 1
        assert constants_count == 5

    # Test constant values and types
    assert HYPHEN == '\u2011'
    assert isinstance(HYPHEN, str)
    assert INDEX_START == '<!-- Index Start - WARNING: Do not delete or modify this markdown comment. -->'
    assert isinstance(INDEX_START, str)
    assert INDEX_END == '<!-- Index End - WARNING: Do not delete or modify this markdown comment. -->'
    assert isinstance(INDEX_END, str)
    assert FIRST_ROW == '| Day   | Title   | Solution   | Site   | Difficulty   |'
    assert isinstance(FIRST_ROW, str)
    assert SECOND_ROW == '| ----- | ------- | ---------- | ------ | ------------ |'
    assert isinstance(SECOND_ROW, str)
