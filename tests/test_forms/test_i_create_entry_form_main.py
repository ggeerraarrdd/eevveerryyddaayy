"""
TD
"""

from ipywidgets import VBox, HTML, Textarea, Dropdown

from src.config import ConfigManager
from src.forms.form_entry import _create_entry_form_widgets
from src.forms.form_entry import _create_entry_form_main










def test_url_widget_creation():
    """
    TD
    """
    test_config = ConfigManager()

    test_widgets_package = _create_entry_form_widgets(test_config)
    test_output = _create_entry_form_main(test_config, test_widgets_package)

    test_config = ConfigManager()
    test_widgets_package = _create_entry_form_widgets(test_config)

    test_output: VBox = _create_entry_form_main(test_config, test_widgets_package)

    # pylint: disable=unsubscriptable-object, not-an-iterable

    # Test overall VBox structure
    assert isinstance(test_output, VBox)
    assert len(test_output.children) == 8
    assert test_output.layout.align_items == 'center'
    assert test_output.layout.display == 'flex'
    assert test_output.layout.flex_flow == 'column'
    assert test_output.layout.width == '100%'

    # Test URL section
    url_section = test_output.children[0]
    assert isinstance(url_section, VBox)
    assert len(url_section.children) == 2
    assert isinstance(url_section.children[0], HTML)
    assert url_section.children[0].value == '<b>URL</b>'
    assert isinstance(url_section.children[1], Textarea)
    assert url_section.children[1].placeholder == 'Enter url'

    # Test Title section
    title_section = test_output.children[1]
    assert isinstance(title_section, VBox)
    assert len(title_section.children) == 2
    assert isinstance(title_section.children[0], HTML)
    assert title_section.children[0].value == '<b>Title</b>'
    assert isinstance(title_section.children[1], Textarea)
    assert title_section.children[1].placeholder == 'Enter problem title'

    # Test Site section
    site_section = test_output.children[2]
    assert isinstance(site_section, VBox)
    assert len(site_section.children) == 2
    assert isinstance(site_section.children[0], HTML)
    assert site_section.children[0].value == '<b>Site</b>'
    assert isinstance(site_section.children[1], Dropdown)
    assert site_section.children[1].options == ('', 'Codewars', 'DataLemur', 'LeetCode')

    # Test Difficulty section
    difficulty_section = test_output.children[3]
    assert isinstance(difficulty_section, VBox)
    assert len(difficulty_section.children) == 2
    assert isinstance(difficulty_section.children[0], HTML)
    assert difficulty_section.children[0].value == '<b>Difficulty</b>'
    assert isinstance(difficulty_section.children[1], Dropdown)
    assert difficulty_section.children[1].options == ('', 'Easy', 'Medium', 'Hard')

    # Test Problem section
    problem_section = test_output.children[4]
    assert isinstance(problem_section, VBox)
    assert len(problem_section.children) == 2
    assert isinstance(problem_section.children[0], HTML)
    assert problem_section.children[0].value == '<b>Problem</b>'
    assert isinstance(problem_section.children[1], Textarea)
    assert problem_section.children[1].placeholder == 'Enter problem description'
    assert problem_section.children[1].layout.height == '100px'

    # Test Your Solution section
    solution_section = test_output.children[5]
    assert isinstance(solution_section, VBox)
    assert len(solution_section.children) == 2
    assert isinstance(solution_section.children[0], HTML)
    assert solution_section.children[0].value == '<b>Your Solution</b>'
    assert isinstance(solution_section.children[1], Textarea)
    assert solution_section.children[1].placeholder == 'Enter your solution here'
    assert solution_section.children[1].layout.height == '200px'

    # Test Site Solution section
    site_solution_section = test_output.children[6]
    assert isinstance(site_solution_section, VBox)
    assert len(site_solution_section.children) == 2
    assert isinstance(site_solution_section.children[0], HTML)
    assert site_solution_section.children[0].value == '<b>Site Solution</b>'
    assert isinstance(site_solution_section.children[1], Textarea)
    assert site_solution_section.children[1].placeholder == 'Enter site solution here'
    assert site_solution_section.children[1].layout.height == '200px'

    # Test Notes section
    notes_section = test_output.children[7]
    assert isinstance(notes_section, VBox)
    assert len(notes_section.children) == 2
    assert isinstance(notes_section.children[0], HTML)
    assert notes_section.children[0].value == '<b>Notes</b>'
    assert isinstance(notes_section.children[1], Textarea)
    assert notes_section.children[1].value == 'TBD'
    assert notes_section.children[1].layout.height == '100px'

    # Test common layout properties for all sections
    for section in test_output.children:
        assert section.layout.align_items == 'center'
        assert section.layout.display == 'flex'
        assert section.layout.flex_flow == 'column'
        assert section.layout.width == '100%'
        assert section.children[0].layout.margin == '0'
        assert section.children[0].layout.width == '50%'
        assert section.children[1].layout.margin == '0 0 25px 0'
        assert section.children[1].layout.width == '50%'

    # pylint: enable=unsubscriptable-object, not-an-iterable
