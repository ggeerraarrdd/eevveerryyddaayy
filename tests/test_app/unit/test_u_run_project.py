""""
TD
"""

from unittest.mock import Mock, patch

from src.app import run_project








def test_run_project():
    """
    Test that run_project properly processes entry data
    """
    # Create mock objects
    mock_config = Mock()
    mock_package = Mock()
    mock_data = ['test_data']

    # Set up patches
    with patch('src.app.ConfigManager', return_value=mock_config) as mock_config_class:
        with patch('src.app.datetime') as mock_datetime:
            with patch('src.app.handle_runs_main') as mock_handle_runs_main:
                mock_now = Mock()
                mock_datetime.now.return_value = mock_now

                result = run_project(mock_package, mock_data)

                mock_config_class.assert_called_once()

                mock_datetime.now.assert_called_once()

                mock_handle_runs_main.assert_called_once_with(mock_config, mock_package, mock_data[0], mock_now)

                assert result == 1
