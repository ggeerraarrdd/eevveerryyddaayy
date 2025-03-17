"""
TD
"""

from datetime import datetime
import os
import tempfile
from unittest import TestCase
from unittest.mock import Mock

from src.handlers.handle_runs import _handle_runs_prep_index










def test_handle_runs_prep_index_case_1_default():
    """Test sequence generation with mock directory and README.md"""
    # Setup mock config
    mock_config = Mock()
    mock_config.get.side_effect = {
        'NB': 0,
        'SEQ_NOTATION': 0
    }.get

    # Create temp directory and mock README.md
    with tempfile.TemporaryDirectory() as test_root_dir:
        test_readme_file_path = os.path.join(test_root_dir, 'README.md')

        test_readme_template = [
            '# Test README\n',
            '<!-- START -->\n',
            '| Seq   | Col2   | Col3   | Col4   | Col5  |\n',
            '| ----- | ------ | ------ | ------ | ----- |\n',
            '| 001   | test   | test   | test   | test  |\n',
            '<!-- END -->\n'
        ]

        # Create mock README with index end marker
        with open(test_readme_file_path, 'w', encoding='utf-8') as f:
            f.truncate(0)
            f.write(''.join(test_readme_template))

        # Test numeric sequence gap filling with 0 gap
        expected = [
            '# Test README\n',
            '<!-- START -->\n',
            '| Seq   | Col2   | Col3   | Col4   | Col5  |\n',
            '| ----- | ------ | ------ | ------ | ----- |\n',
            '| 001   | test   | test   | test   | test  |\n',
            '<!-- END -->\n'
        ]

        result = _handle_runs_prep_index(
            config=mock_config,
            seq_last=1,
            seq_next=2, #Expecting 0 gap
            root_dir=test_root_dir,
            index_end='<!-- END -->'
        )
        assert result == 1

        with open(test_readme_file_path, 'r+', encoding='utf-8') as file:
            lines = file.readlines()
            assert len(lines) == len(expected)
            assert lines == expected

        # Create mock README with index end marker
        with open(test_readme_file_path, 'w', encoding='utf-8') as f:
            f.truncate(0)
            f.write(''.join(test_readme_template))

        # Test numeric sequence gap filling with 1 gap
        expected = [
            '# Test README\n',
            '<!-- START -->\n',
            '| Seq   | Col2   | Col3   | Col4   | Col5  |\n',
            '| ----- | ------ | ------ | ------ | ----- |\n',
            '| 001   | test   | test   | test   | test  |\n',
            '| 002   |    |    |    |    |\n',
            '<!-- END -->\n'
        ]

        result = _handle_runs_prep_index(
            config=mock_config,
            seq_last=1,
            seq_next=3, #Expecting 1 gap
            root_dir=test_root_dir,
            index_end='<!-- END -->'
        )
        assert result == 1

        with open(test_readme_file_path, 'r+', encoding='utf-8') as file:
            lines = file.readlines()
            assert len(lines) == len(expected)
            assert lines == expected

        # Create mock README with index end marker
        with open(test_readme_file_path, 'w', encoding='utf-8') as f:
            f.truncate(0)
            f.write(''.join(test_readme_template))

        # Test numeric sequence gap filling with 5 gap
        expected = [
            '# Test README\n',
            '<!-- START -->\n',
            '| Seq   | Col2   | Col3   | Col4   | Col5  |\n',
            '| ----- | ------ | ------ | ------ | ----- |\n',
            '| 001   | test   | test   | test   | test  |\n',
            '| 002   |    |    |    |    |\n',
            '| 003   |    |    |    |    |\n',
            '| 004   |    |    |    |    |\n',
            '| 005   |    |    |    |    |\n',
            '| 006   |    |    |    |    |\n',
            '<!-- END -->\n'
        ]

        result = _handle_runs_prep_index(
            config=mock_config,
            seq_last=1,
            seq_next=7, #Expecting 5 gap
            root_dir=test_root_dir,
            index_end='<!-- END -->'
        )
        assert result == 1

        with open(test_readme_file_path, 'r+', encoding='utf-8') as file:
            lines = file.readlines()
            assert lines == expected


def test_handle_runs_prep_index_case_2():
    """Test sequence generation with mock directory and README.md"""
    # Setup mock config
    mock_config = Mock()

    # Test Case 2
    mock_config.get.side_effect = {
        'NB': 0,
        'SEQ_NOTATION': 1
    }.get

    # Create temp directory and mock README.md
    with tempfile.TemporaryDirectory() as test_root_dir:
        test_readme_file_path = os.path.join(test_root_dir, 'README.md')

        test_readme_template = [
            '# Test README\n',
            '<!-- START -->\n',
            '| Seq          | Col2   | Col3   | Col4   | Col5  |\n',
            '| ------------ | ------ | ------ | ------ | ----- |\n',
            '| 2025-03-15   | test   | test   | test   | test  |\n',
            '<!-- END -->\n'
        ]

        # Create mock README with index end marker
        with open(test_readme_file_path, 'w', encoding='utf-8') as f:
            f.truncate(0)
            f.write(''.join(test_readme_template))

        # Test numeric sequence gap filling with 0 gap
        expected = [
            '# Test README\n',
            '<!-- START -->\n',
            '| Seq          | Col2   | Col3   | Col4   | Col5  |\n',
            '| ------------ | ------ | ------ | ------ | ----- |\n',
            '| 2025-03-15   | test   | test   | test   | test  |\n',
            '<!-- END -->\n'
        ]

        result = _handle_runs_prep_index(
            config=mock_config,
            seq_last=datetime(2025, 3, 15).date(),
            seq_next=datetime(2025, 3, 16).date(), #Expecting 0 gap
            root_dir=test_root_dir,
            index_end='<!-- END -->',
            hyphen='-'
        )
        assert result == 1

        with open(test_readme_file_path, 'r+', encoding='utf-8') as file:
            lines = file.readlines()
            assert len(lines) == len(expected)
            assert lines == expected

        # Create mock README with index end marker
        with open(test_readme_file_path, 'w', encoding='utf-8') as f:
            f.truncate(0)
            f.write(''.join(test_readme_template))

        # Test numeric sequence gap filling with 1 gap
        expected = [
            '# Test README\n',
            '<!-- START -->\n',
            '| Seq          | Col2   | Col3   | Col4   | Col5  |\n',
            '| ------------ | ------ | ------ | ------ | ----- |\n',
            '| 2025-03-15   | test   | test   | test   | test  |\n',
            '| 2025-03-16   |    |    |    |    |\n',
            '<!-- END -->\n'
        ]

        result = _handle_runs_prep_index(
            config=mock_config,
            seq_last=datetime(2025, 3, 15).date(),
            seq_next=datetime(2025, 3, 17).date(), #Expecting 1 gap
            root_dir=test_root_dir,
            index_end='<!-- END -->',
            hyphen='-'
        )
        assert result == 1

        with open(test_readme_file_path, 'r+', encoding='utf-8') as file:
            lines = file.readlines()
            assert len(lines) == len(expected)
            assert lines == expected

        # Create mock README with index end marker
        with open(test_readme_file_path, 'w', encoding='utf-8') as f:
            f.truncate(0)
            f.write(''.join(test_readme_template))

        # Test numeric sequence gap filling with 5 gap
        expected = [
            '# Test README\n',
            '<!-- START -->\n',
            '| Seq          | Col2   | Col3   | Col4   | Col5  |\n',
            '| ------------ | ------ | ------ | ------ | ----- |\n',
            '| 2025-03-15   | test   | test   | test   | test  |\n',
            '| 2025-03-16   |    |    |    |    |\n',
            '| 2025-03-17   |    |    |    |    |\n',
            '| 2025-03-18   |    |    |    |    |\n',
            '| 2025-03-19   |    |    |    |    |\n',
            '| 2025-03-20   |    |    |    |    |\n',
            '<!-- END -->\n'
        ]

        result = _handle_runs_prep_index(
            config=mock_config,
            seq_last=datetime(2025, 3, 15).date(),
            seq_next=datetime(2025, 3, 21).date(), #Expecting 5 gap
            root_dir=test_root_dir,
            index_end='<!-- END -->',
            hyphen='-'
        )
        assert result == 1

        with open(test_readme_file_path, 'r+', encoding='utf-8') as file:
            lines = file.readlines()
            assert lines == expected


def test_handle_runs_prep_index_case_3():
    """Test sequence generation with mock directory and README.md"""
    # Setup mock config
    mock_config = Mock()
    mock_config.get.side_effect = {
        'NB': 1,
        'SEQ_NOTATION': 0
    }.get

    # Create temp directory and mock README.md
    with tempfile.TemporaryDirectory() as test_root_dir:
        test_readme_file_path = os.path.join(test_root_dir, 'README.md')

        test_readme_template = [
            '# Test README\n',
            '<!-- START -->\n',
            '| Seq   | Col2   | Col3   | Col4   | Col5  | Col6  |\n',
            '| ----- | ------ | ------ | ------ | ----- | ----- |\n',
            '| 001   | test   | test   | test   | test  | test  |\n',
            '<!-- END -->\n'
        ]

        # Create mock README with index end marker
        with open(test_readme_file_path, 'w', encoding='utf-8') as f:
            f.truncate(0)
            f.write(''.join(test_readme_template))

        # Test numeric sequence gap filling with 0 gap
        expected = [
            '# Test README\n',
            '<!-- START -->\n',
            '| Seq   | Col2   | Col3   | Col4   | Col5  | Col6  |\n',
            '| ----- | ------ | ------ | ------ | ----- | ----- |\n',
            '| 001   | test   | test   | test   | test  | test  |\n',
            '<!-- END -->\n'
        ]

        result = _handle_runs_prep_index(
            config=mock_config,
            seq_last=1,
            seq_next=2, #Expecting 0 gap
            root_dir=test_root_dir,
            index_end='<!-- END -->'
        )
        assert result == 1

        with open(test_readme_file_path, 'r+', encoding='utf-8') as file:
            lines = file.readlines()
            assert len(lines) == len(expected)
            assert lines == expected

        # Create mock README with index end marker
        with open(test_readme_file_path, 'w', encoding='utf-8') as f:
            f.truncate(0)
            f.write(''.join(test_readme_template))

        # Test numeric sequence gap filling with 5 gap
        expected = [
            '# Test README\n',
            '<!-- START -->\n',
            '| Seq   | Col2   | Col3   | Col4   | Col5  | Col6  |\n',
            '| ----- | ------ | ------ | ------ | ----- | ----- |\n',
            '| 001   | test   | test   | test   | test  | test  |\n',
            '| 002   |    |    |    |    |    |\n',
            '| 003   |    |    |    |    |    |\n',
            '| 004   |    |    |    |    |    |\n',
            '| 005   |    |    |    |    |    |\n',
            '| 006   |    |    |    |    |    |\n',
            '<!-- END -->\n'
        ]

        result = _handle_runs_prep_index(
            config=mock_config,
            seq_last=1,
            seq_next=7, #Expecting 5 gap
            root_dir=test_root_dir,
            index_end='<!-- END -->'
        )
        assert result == 1

        with open(test_readme_file_path, 'r+', encoding='utf-8') as file:
            lines = file.readlines()
            assert lines == expected


def test_handle_runs_prep_index_case_4_no_end_marker():
    """Test that ValueError is raised when end marker is missing"""
    # Setup mock config
    mock_config = Mock()
    mock_config.get.side_effect = {
        'NB': 0,
        'SEQ_NOTATION': 0
    }.get

    # Create temp directory and mock README.md
    with tempfile.TemporaryDirectory() as test_root_dir:
        test_readme_file_path = os.path.join(test_root_dir, 'README.md')

        test_readme_template = [
            '# Test README\n',
            '<!-- START -->\n',
            '| Seq   | Col2   | Col3   | Col4   | Col5  |\n',
            '| ----- | ------ | ------ | ------ | ----- |\n',
            '| 001   | test   | test   | test   | test  |\n',
        ]

        # Create mock README with missing end marker
        with open(test_readme_file_path, 'w', encoding='utf-8') as f:
            f.truncate(0)
            f.write(''.join(test_readme_template))

        # Test using TestCase just for assertions
        test_case = TestCase()
        with test_case.assertRaises(ValueError) as context:
            _handle_runs_prep_index(
                config=mock_config,
                seq_last=1,
                seq_next=2,
                root_dir=test_root_dir,
                index_end='<!-- END -->'
            )

        test_case.assertEqual(
            str(context.exception),
            "Index end marker '<!-- END -->' not found in file"
        )


def test_handle_runs_prep_index_case_5_invalid_notation():
    """Test that ValueError is raised when end marker is missing"""
    # Setup mock config
    mock_config = Mock()
    mock_config.get.side_effect = {
        'NB': 0,
        'SEQ_NOTATION': 2
    }.get

    # Create temp directory and mock README.md
    with tempfile.TemporaryDirectory() as test_root_dir:
        test_readme_file_path = os.path.join(test_root_dir, 'README.md')

        test_readme_template = [
            '# Test README\n',
            '<!-- START -->\n',
            '| Seq   | Col2   | Col3   | Col4   | Col5  |\n',
            '| ----- | ------ | ------ | ------ | ----- |\n',
            '| 001   | test   | test   | test   | test  |\n',
            '<!-- END -->\n'
        ]

        # Create mock README with missing end marker
        with open(test_readme_file_path, 'w', encoding='utf-8') as f:
            f.truncate(0)
            f.write(''.join(test_readme_template))

        # Test using TestCase just for assertions
        test_case = TestCase()
        with test_case.assertRaises(ValueError) as context:
            _handle_runs_prep_index(
                config=mock_config,
                seq_last=1,
                seq_next=2,
                root_dir=test_root_dir,
                index_end='<!-- END -->'
            )

        test_case.assertEqual(
            str(context.exception),
            'Invalid configuration: SEQ_NOTATION is 0 or 1.'
        )
