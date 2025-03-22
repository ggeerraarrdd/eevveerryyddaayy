""""
TD
"""

from unittest.mock import Mock, patch

from src.app import add_project








def test_add_project():
    """
    TD
    """
    # Create mock objects
    mock_config = Mock()
    mock_form = Mock()

    # Mock both ConfigManager and create_entry_form
    with patch('src.app.ConfigManager', return_value=mock_config) as mock_config_class:
        with patch('src.app.create_entry_form', return_value=mock_form) as mock_create_form:
            # Call the function
            result = add_project()

            # Assert ConfigManager was called
            mock_config_class.assert_called_once()

            # Assert create_entry_form was called with correct config
            mock_create_form.assert_called_once_with(mock_config)

            # Assert the return value is correct
            assert result == mock_form
