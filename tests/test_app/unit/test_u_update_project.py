"""
TD
"""

from src.app import update_project










def test_update_project():
    """Test that update_project returns 0"""
    mock_package = {
            'PROJ_TITLE': (str, 'Test Title'),
            'NB': (int, 1),
            'NB_NAME': (str, 'Test Name'),
            'SEQ_NOTATION': (int, 1),
            'SEQ_SPARSE': (int, 1),
            'SITE_OPTIONS': (list, ['site1'])
        }

    assert update_project(mock_package) == 0
