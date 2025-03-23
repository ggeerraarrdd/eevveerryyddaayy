""""
TD
"""

from unittest.mock import call, patch

from src.app import eevveerryyddaayy
from src.utils import validate_project










def test_everyday_update(tmpdir):
    """
    Test that run_project properly processes entry data
    """
    if validate_project():
        return

    mock_root_dir = str(tmpdir)

    proj_title='Test Title'
    nb=1
    nb_name='Test Name'
    seq_notation=1
    seq_sparse=1
    site_options=['DataLemur', 'LeetCode']

    with patch('builtins.print') as mock_print:
        test_results = eevveerryyddaayy(proj_title,
                                        nb,
                                        nb_name,
                                        seq_notation,
                                        seq_sparse,
                                        site_options,
                                        root_dir=mock_root_dir,
                                        source=1)

        mock_print.assert_called_once_with('Not yet implemented')
        assert test_results == 0


def test_everyday_add_init(tmpdir):
    """
    Test that run_project properly processes entry data
    """
    if validate_project():
        return

    mock_root_dir = str(tmpdir)

    proj_title='Test Title'
    nb=1
    nb_name='Test Name'
    seq_notation=1
    seq_sparse=1
    site_options=['DataLemur', 'LeetCode']

    with patch('src.app.validate_project') as mock_validate_project, \
        patch('src.app.add_project') as mock_add_project:
        mock_validate_project.return_value = True

        eevveerryyddaayy(proj_title,
                        nb,
                        nb_name,
                        seq_notation,
                        seq_sparse,
                        site_options,
                        root_dir=mock_root_dir,
                        source=2)

        mock_add_project.assert_called_once()


def test_everyday_add_no_init(tmpdir):
    """
    Test that run_project properly processes entry data
    """
    if validate_project():
        return

    mock_root_dir = str(tmpdir)

    proj_title='Test Title'
    nb=1
    nb_name='Test Name'
    seq_notation=1
    seq_sparse=1
    site_options=['DataLemur', 'LeetCode']

    with patch('src.app.validate_project') as mock_validate_project, \
        patch('builtins.print') as mock_print:
        mock_validate_project.return_value = False

        test_results = eevveerryyddaayy(proj_title,
                                        nb,
                                        nb_name,
                                        seq_notation,
                                        seq_sparse,
                                        site_options,
                                        root_dir=mock_root_dir,
                                        source=2)

        mock_validate_project.assert_called_once()
        mock_print.assert_has_calls([
            call('The project is not initialized.'),
            call('Use every_start.ipynb to initialize project.')
        ])
        assert test_results == 0


def test_everyday_invalid(tmpdir):
    """
    Test that run_project properly processes entry data
    """
    mock_root_dir = str(tmpdir)

    proj_title='Test Title'
    nb=1
    nb_name='Test Name'
    seq_notation=1
    seq_sparse=1
    site_options=['DataLemur', 'LeetCode']

    with patch('builtins.print') as mock_print:

        test_results = eevveerryyddaayy(proj_title,
                                        nb,
                                        nb_name,
                                        seq_notation,
                                        seq_sparse,
                                        site_options,
                                        root_dir=mock_root_dir,
                                        source=4)

        mock_print.assert_called_once_with('Invalid source')
        assert test_results == 0


def test_everyday_run(tmpdir):
    """
    Test that run_project properly processes entry data
    """
    mock_root_dir = str(tmpdir)

    proj_title='Test Title'
    nb=1
    nb_name='Test Name'
    seq_notation=1
    seq_sparse=1
    site_options=['DataLemur', 'LeetCode']

    mock_args = (proj_title, nb, nb_name, seq_notation, seq_sparse, site_options)

    with patch('src.app.PackageManager') as mock_package_manager, \
        patch('src.app.run_project') as mock_run_project:

        mock_package = mock_package_manager()

        test_results = eevveerryyddaayy(proj_title,
                                        nb,
                                        nb_name,
                                        seq_notation,
                                        seq_sparse,
                                        site_options,
                                        root_dir=mock_root_dir,
                                        source=3)

        mock_run_project.assert_called_once_with(mock_package, mock_args)
        assert test_results == 1
