""""
TD
"""""

from src.handlers.handle_runs import _handle_runs_prep_file












def test_filename_sanitization():
    """TD"""
    title = 'Hello World! #123'
    seq_full = '001_01'

    result = _handle_runs_prep_file(title, seq_full)

    expected = '001_01_hello_world_123.md'
    assert result == expected


def test_empty_title():
    """TD"""
    title = ''
    seq_full = '001_01'

    result = _handle_runs_prep_file(title, seq_full)

    assert result == '001_01_.md'


def test_special_characters_removed():
    """TD"""
    title = 'Special!!@#$%^&*'
    seq_full = '001_01'

    result = _handle_runs_prep_file(title, seq_full)

    assert result == '001_01_special.md'


def test_trailing_and_leading_spaces():
    """TD"""
    title = '! Leftover Leading and Trailing Spaces !'
    seq_full = '001_01'

    result = _handle_runs_prep_file(title, seq_full)

    assert result == '001_01_leftover_leading_and_trailing_spaces.md'
