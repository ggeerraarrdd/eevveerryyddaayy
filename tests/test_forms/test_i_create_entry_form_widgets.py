"""
TD
"""

from ipywidgets import Dropdown, Text, Textarea

from src.config import ConfigManager
from src.forms.form_entry import _create_entry_form_widgets










def test_url_widget_creation():
    """
    TD
    """
    test_config = ConfigManager()

    widgets_package = _create_entry_form_widgets(test_config)

    assert len(widgets_package) == 10

    # Test URL widget
    assert widgets_package['url'].value == ''
    assert widgets_package['url'].placeholder == 'Enter url'
    assert widgets_package['url'].layout.margin == '0 0 25px 0'
    assert widgets_package['url'].layout.width == '50%'
    assert isinstance(widgets_package['url'], Textarea)

    # Test title widget
    assert widgets_package['title'].value == ''
    assert widgets_package['title'].placeholder == 'Enter problem title'
    assert widgets_package['title'].layout.margin == '0 0 25px 0'
    assert widgets_package['title'].layout.width == '50%'
    assert isinstance(widgets_package['title'], Textarea)

    # Test difficulty widget
    assert widgets_package['difficulty'].value == ''
    assert widgets_package['difficulty'].options == ('', 'Easy', 'Medium', 'Hard')
    assert widgets_package['difficulty'].layout.margin == '0 0 25px 0'
    assert widgets_package['difficulty'].layout.width == '50%'
    assert isinstance(widgets_package['difficulty'], Dropdown)

    # Test problem widget
    assert widgets_package['problem'].value == ''
    assert widgets_package['problem'].placeholder == 'Enter problem description'
    assert widgets_package['problem'].layout.margin == '0 0 25px 0'
    assert widgets_package['problem'].layout.width == '50%'
    assert widgets_package['problem'].layout.height == '100px'
    assert isinstance(widgets_package['problem'], Textarea)

    # Test submitted_solution widget
    assert widgets_package['submitted_solution'].value == ''
    assert widgets_package['submitted_solution'].placeholder == 'Enter your solution here'
    assert widgets_package['submitted_solution'].layout.margin == '0 0 25px 0'
    assert widgets_package['submitted_solution'].layout.width == '50%'
    assert widgets_package['submitted_solution'].layout.height == '200px'
    assert isinstance(widgets_package['submitted_solution'], Textarea)

    # Test site_solution widget
    assert widgets_package['site_solution'].value == ''
    assert widgets_package['site_solution'].placeholder == 'Enter site solution here'
    assert widgets_package['site_solution'].layout.margin == '0 0 25px 0'
    assert widgets_package['site_solution'].layout.width == '50%'
    assert widgets_package['site_solution'].layout.height == '200px'
    assert isinstance(widgets_package['site_solution'], Textarea)

    # Test notes widget
    assert widgets_package['notes'].value == 'TBD'
    assert widgets_package['notes'].layout.margin == '0 0 25px 0'
    assert widgets_package['notes'].layout.width == '50%'
    assert widgets_package['notes'].layout.height == '100px'
    assert isinstance(widgets_package['notes'], Textarea)

    # Test nb widget
    assert widgets_package['nb'].value == 'TBD'
    assert widgets_package['nb'].layout.margin == '0 0 25px 0'
    assert widgets_package['nb'].layout.width == '50%'
    assert widgets_package['nb'].layout.height == '100px'
    assert isinstance(widgets_package['nb'], Textarea)

    # Test page_title widget
    assert widgets_package['page_title'].value == ''
    assert widgets_package['page_title'].placeholder == 'Enter page title'
    assert widgets_package['page_title'].layout.margin == '0 0 25px 0'
    assert widgets_package['page_title'].layout.width == '50%'
    assert widgets_package['page_title'].layout.height == '100px'
    assert isinstance(widgets_package['page_title'], Text)


def test_url_widget_creation_with_sites_default():
    """
    TD
    """
    test_config = ConfigManager()

    widgets_package = _create_entry_form_widgets(test_config)

    assert len(widgets_package) == 10

    # Test site widget
    assert widgets_package['site'].value == ''
    assert widgets_package['site'].options == ('', 'Codewars', 'DataLemur', 'LeetCode')
    assert widgets_package['site'].layout.margin == '0 0 25px 0'
    assert widgets_package['site'].layout.width == '50%'
    assert isinstance(widgets_package['site'], Dropdown)


def test_url_widget_creation_with_one_site():
    """
    TD
    """
    test_config = ConfigManager()
    test_config.update('SITE_OPTIONS', ['Codewars'])

    widgets_package = _create_entry_form_widgets(test_config)

    print(widgets_package['site'])

    assert len(widgets_package) == 10

    # Test URL widget
    assert widgets_package['site'].options == ('Codewars',)
    assert isinstance(widgets_package['site'], Dropdown)


def test_url_widget_creation_no_sites():
    """
    TD
    """
    test_config = ConfigManager()
    test_config.update('SITE_OPTIONS', [])

    widgets_package = _create_entry_form_widgets(test_config)

    assert len(widgets_package) == 10

    # Test URL widget
    assert widgets_package['site'].options == ('', 'Codewars', 'DataLemur', 'LeetCode')
    assert isinstance(widgets_package['site'], Dropdown)
