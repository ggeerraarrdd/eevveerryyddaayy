"""
TD
"""

from src.utils.utils_runs import clean_strings










def test_clean_strings():
    """
    TD
    """
    # Test with normal string values
    test_data = {
        "key1": "value1\n",
        "key2": "value2\nvalue2",
        "key3": "\nvalue3\n"
    }
    expected = {
        "key1": "value1",
        "key2": "value2\nvalue2",
        "key3": "value3"
    }
    assert clean_strings(test_data) == expected

    # Test with mixed types
    mixed_data = {
        "str_key": "value\n",
        "int_key": 42,
        "none_key": None
    }
    expected_mixed = {
        "str_key": "value",
        "int_key": 42,
        "none_key": None
    }
    assert clean_strings(mixed_data) == expected_mixed

    # Test with empty dictionary
    assert clean_strings({}) == {}

    # # Test with empty strings
    # empty_data = {
    #     "empty": "",
    #     "newline": "\n",
    #     "spaces": "  \n  "
    # }
    # expected_empty = {
    #     "empty": "",
    #     "newline": "",
    #     "spaces": "  "
    # }
    # assert clean_strings(empty_data) == expected_empty
