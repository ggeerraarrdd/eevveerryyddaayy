"""
TD
"""

from ipywidgets import VBox, Button, ButtonStyle

from src.config import ConfigManager
from src.forms.form_entry import _create_entry_form_widgets
from src.forms.form_entry import _create_entry_form_button










def test_create_entry_form_button():
    """
    TD
    """
    test_config = ConfigManager()

    test_widgets_package = _create_entry_form_widgets(test_config)
    test_output = _create_entry_form_button(test_config, test_widgets_package)

    # Test overall VBox structure
    assert isinstance(test_output, VBox)
    assert len(test_output.children) == 1
    assert test_output.layout.align_items == 'center'
    assert test_output.layout.display == 'flex'
    assert test_output.layout.flex_flow == 'column'
    assert test_output.layout.width == '100%'

    # Test Button properties
    button = test_output.children[0]
    assert isinstance(button, Button)
    assert button.description == 'Process Entry'
    assert isinstance(button.style, ButtonStyle)
    assert button.tooltip == 'Processing...'
