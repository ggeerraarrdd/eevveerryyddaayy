"""
TD
"""

from unittest.mock import Mock, call

from src.handlers.handle_runs import _handle_runs_prep_package










def test_handle_runs_prep_package():
    """Test _handle_runs_prep_package function in isolation"""
    # Setup mock package with side effects
    mock_package = Mock()
    mock_values = {
        ('package', 'day'): '',
        ('package', 'url'): '',
        ('package', 'title'): '',
        ('package', 'title_index'): '',
        ('package', 'solution'): '',
        ('package', 'site'): '',
        ('package', 'difficulty'): '',
        ('package', 'problem'): '',
        ('package', 'submitted_solution'): '',
        ('package', 'site_solution'): '',
        ('package', 'notes'): '',
        ('package', 'nb'): '',
        ('package', 'seq_full'): '',
        ('package', 'filename'): '',
        ('package_widths', 'day'): 0,
        ('package_widths', 'title'): 0,
        ('package_widths', 'solution'): 0,
        ('package_widths', 'site'): 0,
        ('package_widths', 'difficulty'): 0,
        ('package_widths', 'nb'): 0
    }

    def mock_update_value(section, key, value):
        mock_values[(section, key)] = value
        return True

    def mock_get(section, key):
        return mock_values.get((section, key), '')

    mock_package.update_value.side_effect = mock_update_value
    mock_package.get.side_effect = mock_get

    test_seq = '001'
    test_seq_full = '001_01'
    test_filename = '001_01_test.md'

    test_new_package = {
        'url': 'https://example.com',
        'title': 'Test Problem',
        'site': 'TestSite',
        'difficulty': 'Easy',
        'problem': 'Test description',
        'submitted_solution': 'Test solution',
        'site_solution': 'Official solution',
        'notes': 'Test notes',
        'nb': '0'
    }

    result = _handle_runs_prep_package(
        package=mock_package,
        seq=test_seq,
        seq_full=test_seq_full,
        new_package=test_new_package,
        filename=test_filename
    )

    assert result == 1

    # Assert package updates
    expected_package_calls = [
        call('package', 'day', test_seq),
        call('package', 'url', test_new_package['url']),
        call('package', 'title', test_new_package['title']),
        call('package', 'title_index', f'[{test_new_package["title"]}]({test_new_package["url"]})'),
        call('package', 'solution', f'[Solution](solutions/{test_filename})'),
        call('package', 'site', test_new_package['site']),
        call('package', 'difficulty', test_new_package['difficulty']),
        call('package', 'problem', test_new_package['problem']),
        call('package', 'submitted_solution', test_new_package['submitted_solution']),
        call('package', 'site_solution', test_new_package['site_solution']),
        call('package', 'notes', test_new_package['notes']),
        call('package', 'nb', test_new_package['nb']),
        call('package', 'seq_full', test_seq_full),
        call('package', 'filename', test_filename)
    ]

    # Assert package_widths updates
    expected_widths_calls = [
        call('package_widths', 'day', len(test_seq) + 2),
        call('package_widths', 'title', len(f'[{test_new_package["title"]}]({test_new_package["url"]})') + 2),
        call('package_widths', 'solution', len(f'[Solution](solutions/{test_filename})') + 2),
        call('package_widths', 'site', len(test_new_package['site']) + 2),
        call('package_widths', 'difficulty', len(test_new_package['difficulty']) + 2),
        call('package_widths', 'nb', len(test_new_package['nb']) + 2)
    ]

    # Verify all expected calls were made with proper side effects
    mock_package.update_value.assert_has_calls(
        expected_package_calls + expected_widths_calls,
        any_order=True
    )

    # Verify values were properly stored
    assert mock_package.get('package', 'day') == test_seq
    assert mock_package.get('package', 'url') == test_new_package['url']
    assert mock_package.get('package_widths', 'day') == len(test_seq) + 2
