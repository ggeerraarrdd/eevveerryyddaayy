"""
TD
"""

import pytest

from src.utils.utils_runs import get_target_line_dict










def test_get_target_line_dict_no_nb():
    """Test parsing table line when nb_loc = 0"""
    input_line = "| 1 | Two Sums | Solution.py | LC | Easy |"

    result = get_target_line_dict(0, input_line)

    expected = {
        'day': '1',
        'title': 'Two Sums',
        'solution': 'Solution.py',
        'site': 'LC',
        'difficulty': 'Easy',
        'nb': ''
    }
    assert result == expected, f'Expected {expected} but got {result}'


def test_get_target_line_dict_with_nb():
    """Test parsing table line when nb_loc = 0"""
    input_line = "| 1     |Two Sums    |Solution.py| LC        | Easy   | Note  |"

    result = get_target_line_dict(1, input_line)

    expected = {
        'day': '1',
        'title': 'Two Sums',
        'solution': 'Solution.py',
        'site': 'LC',
        'difficulty': 'Easy',
        'nb': 'Note'
    }
    assert result == expected, f'Expected {expected} but got {result}'

    with pytest.raises(ValueError) as exc_info:
        result = get_target_line_dict(2, input_line)

    assert str(exc_info.value) == 'Invalid configuration: NB must be 0 or 1.'
