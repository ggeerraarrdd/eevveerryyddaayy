"""
TD
"""

import os
import tempfile
from unittest.mock import Mock

from src.handlers.handle_runs import _handle_runs_implement_file










def test_handle_runs_implement_file():
    """Test _handle_runs_implement_file function in isolation"""
    # Mock config
    mock_config = Mock()
    mock_config.get.return_value = 'templates'

    # Test data
    test_data = {
        'filename': '001_01_test_solution.md',
        'title': 'Test Problem',
        'difficulty': 'Easy'
    }

    # Create temp test files and directories
    with tempfile.TemporaryDirectory() as test_root_dir:
        # Create mock template directory and file
        os.makedirs(os.path.join(test_root_dir, 'templates'))
        os.makedirs(os.path.join(test_root_dir, 'solutions'))

        template_path = os.path.join(test_root_dir, 'templates', 'solution.txt')
        with open(template_path, 'w', encoding='utf-8') as f:
            f.write('Title: {{title}}\nDifficulty: {{difficulty}}')

        # Test function
        result = _handle_runs_implement_file(
            config=mock_config,
            data=test_data,
            root_dir=test_root_dir
        )

        # Verify results
        assert result == 1

        # Check created file contents
        solution_path = os.path.join(test_root_dir, 'solutions', '001_01_test_solution.md')
        with open(solution_path, 'r', encoding='utf-8') as f:
            content = f.read()

        assert content == 'Title: Test Problem\nDifficulty: Easy'

        # Verify config was called correctly
        mock_config.get.assert_called_once_with('TEMPLATES_DIR')
