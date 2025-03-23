""""
TD
"""

from unittest.mock import patch

from src.app import eevveerryyddaayy










def test_everyday_no_root_kwargs():
    """
    TD
    """
    proj_title='Test Title'
    nb=1
    nb_name='Test Name'
    seq_notation=1
    seq_sparse=1
    site_options=['DataLemur', 'LeetCode']

    with patch('src.app.ROOT_DIR', 'fake/path/no/root/kwargs') as mock_root_dir, \
         patch('src.app.start_project') as mock_start_project, \
         patch('src.app.validate_project', return_value=False), \
         patch('src.app.ConfigManager'):

        result = eevveerryyddaayy(proj_title,
                                    nb,
                                    nb_name,
                                    seq_notation,
                                    seq_sparse,
                                    site_options,
                                    source=0)
        assert result == 1

        _, _, root_dir_arg = mock_start_project.call_args[0]
        assert root_dir_arg == mock_root_dir


def test_everyday_with_root_kwargs():
    """
    TD
    """
    proj_title='Test Title'
    nb=1
    nb_name='Test Name'
    seq_notation=1
    seq_sparse=1
    site_options=['DataLemur', 'LeetCode']

    test_root_kwarg = 'fake/path/with/root/kwargs'

    with patch('src.app.ROOT_DIR', 'fake/path/no/root/kwargs'), \
         patch('src.app.start_project') as mock_start_project, \
         patch('src.app.validate_project', return_value=False), \
         patch('src.app.ConfigManager'):

        result = eevveerryyddaayy(proj_title,
                                    nb,
                                    nb_name,
                                    seq_notation,
                                    seq_sparse,
                                    site_options,
                                    root_dir=test_root_kwarg,
                                    source=0)
        assert result == 1

        _, _, root_dir_arg = mock_start_project.call_args[0]
        assert root_dir_arg == test_root_kwarg
