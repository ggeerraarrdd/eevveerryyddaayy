"""
TD
"""

from unittest.mock import Mock

from src.utils.utils_runs import get_target_line_updated










def test_get_target_line_normal_row_no_nb():
    """Test normal row formatting when nb_local = 0"""
    # Setup mocks
    config_mock = Mock()
    package_mock = Mock()

    # Configure mocks
    config_mock.get.return_value = 0  # nb_local = 0

    # Mock widths dictionary
    widths = {
        'day': 5,
        'title': 10,
        'solution': 10,
        'site': 10,
        'difficulty': 10
    }
    package_mock.get_dictionary.return_value = widths

    test_data = {
        'day': '1',
        'title': 'Test',
        'solution': 'Sol',
        'site': 'LC',
        'difficulty': 'Easy',
        'nb': '57'  # Should be ignored when nb_local = 0
    }

    result = get_target_line_updated(
        is_second_line=False,
        config=config_mock,
        package=package_mock,
        data=test_data
    )

    expected = "| 1     | Test       | Sol        | LC         | Easy       |"
    assert result == expected, f"Expected '{expected}' but got '{result}'"


def test_get_target_line_normal_row_with_nb():
    """Test normal row formatting when nb_local = 0"""
    # Setup mocks
    config_mock = Mock()
    package_mock = Mock()

    # Configure mocks
    config_mock.get.return_value = 1  # nb_local = 1

    # Mock widths dictionary
    widths = {
        'day': 5,
        'title': 10,
        'solution': 10,
        'site': 10,
        'difficulty': 10,
        'nb': 10
    }
    package_mock.get_dictionary.return_value = widths

    test_data = {
        'day': '1',
        'title': 'Test',
        'solution': 'Sol',
        'site': 'LC',
        'difficulty': 'Easy',
        'nb': '57'
    }

    result = get_target_line_updated(
        is_second_line=False,
        config=config_mock,
        package=package_mock,
        data=test_data
    )
    expected = "| 1     | Test       | Sol        | LC         | Easy       | 57         |"

    assert result == expected, f"Expected '{expected}' but got '{result}'"


def test_get_target_line_second_row_no_nb():
    """Test normal row formatting when nb_local = 0"""
    # Setup mocks
    config_mock = Mock()
    package_mock = Mock()

    # Configure mocks
    config_mock.get.return_value = 0  # nb_local = 0

    # Mock widths dictionary
    widths = {
        'day': 5,
        'title': 10,
        'solution': 10,
        'site': 10,
        'difficulty': 10
    }
    package_mock.get_dictionary.return_value = widths

    test_data = {
        'day': '-',
        'title': '---',
        'solution': '---',
        'site': '--',
        'difficulty': '----',
        'nb': '--'  # Should be ignored when nb_local = 0
    }

    result = get_target_line_updated(
        is_second_line=True,
        config=config_mock,
        package=package_mock,
        data=test_data
    )

    expected = "| ----- | ---------- | ---------- | ---------- | ---------- |"
    assert result == expected, f"Expected '{expected}' but got '{result}'"


def test_get_target_line_second_row_with_nb():
    """Test normal row formatting when nb_local = 0"""
    # Setup mocks
    config_mock = Mock()
    package_mock = Mock()

    # Configure mocks
    config_mock.get.return_value = 1  # nb_local = 1

    # Mock widths dictionary
    widths = {
        'day': 5,
        'title': 10,
        'solution': 10,
        'site': 10,
        'difficulty': 10,
        'nb': 10
    }
    package_mock.get_dictionary.return_value = widths

    test_data = {
        'day': '-',
        'title': '---',
        'solution': '---',
        'site': '--',
        'difficulty': '----',
        'nb': '--'
    }

    result = get_target_line_updated(
        is_second_line=True,
        config=config_mock,
        package=package_mock,
        data=test_data
    )
    expected = "| ----- | ---------- | ---------- | ---------- | ---------- | ---------- |"

    assert result == expected, f"Expected '{expected}' but got '{result}'"
