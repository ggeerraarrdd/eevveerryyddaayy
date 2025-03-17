"""
TD
"""

from unittest.mock import Mock

from src.handlers.handle_runs import _handle_runs_implement_config










# def test_handle_runs_implement_config():
#     """
#     TD
#     """
#     # Mock dependencies
#     mock_config = Mock()
#     mock_package = Mock()

#     # Configure mock returns
#     mock_config.get.return_value = {
#         'col1': 10,
#         'col2': 15,
#         'col3': 20
#     }

#     mock_package.get_dictionary.return_value = {
#         'col1': 5,
#         'col2': 20,
#         'col3': 15
#     }

#     # Call function
#     result = _handle_runs_implement_config(mock_config, mock_package)

#     # Verify results
#     assert result == 1

#     # Verify mock interactions
#     mock_config.get.assert_called_once_with('COLS_WIDTH')
#     mock_package.get_dictionary.assert_called_once_with('package_widths')

#     # Verify package updates
#     expected_calls = [
#         ('package_widths', 'col1', 10),
#         ('package_widths', 'col3', 20)
#     ]

#     for call in expected_calls:
#         mock_package.update_value.assert_any_call(*call)

#     assert mock_package.update_value.call_count == 2


def test_handle_runs_implement_config():
    """
    TD
    """
    # Mock config and package instance
    mock_config = Mock()
    mock_package = Mock()

    # Mock package.get_dictionary() return value
    mock_package.get_dictionary.return_value = {
        'day': 5,
        'title': 7,
        'solution': 10,
        'site': 6,
        'difficulty': 12,
        'nb': 1
    }

    # Mock package.update_value() with side effect
    def mock_update_value(dict_name, key, value):
        if dict_name != 'package_widths':
            raise KeyError(f'Invalid dictionary name {dict_name}')
        if key not in mock_package.get_dictionary.return_value:
            raise KeyError(f'Invalid key {key}')
        mock_package.get_dictionary.return_value[key] = value

    mock_package.update_value = Mock(side_effect=mock_update_value)

    # Test Case 1 - no changes
    # Mock config.get() return value
    mock_config.get.return_value = {
        'day': 5,
        'title': 7,
        'solution': 10,
        'site': 6,
        'difficulty': 12,
        'nb': 1
    }
    # Call function
    result = _handle_runs_implement_config(mock_config, mock_package)
    assert result == 0

    # Test Case 2 - with changes
    # Mock config.get() return value
    mock_config.get.return_value = {
        'day': 10,
        'title': 7,
        'solution': 20,
        'site': 6,
        'difficulty': 12,
        'nb': 1
    }
    # Call function
    result = _handle_runs_implement_config(mock_config, mock_package)
    assert result == 1
