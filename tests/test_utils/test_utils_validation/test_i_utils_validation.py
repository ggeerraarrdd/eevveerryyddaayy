"""
TD
"""

from src.config import ConfigManager
from src.utils.utils_validation import validate_project









def test_validate_project():
    """
    TD
    """
    test_config = ConfigManager()

    test_config.update('PROJ_START', '')
    result = validate_project(test_config)
    assert result is False

    test_config.update('PROJ_START', '2025-01-01')
    result = validate_project(test_config)
    assert result is True
