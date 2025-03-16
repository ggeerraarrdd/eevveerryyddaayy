"""
TD
"""

import unittest
from datetime import datetime
from unittest.mock import patch

from src.handlers.handle_runs import _handle_runs_prep_seq_files









class TestHandleRunsPrepSeqFiles(unittest.TestCase):
    """
    TD
    """
    def setUp(self):
        self.today = datetime(2025, 3, 15)
        self.hyphen = '\u2011'


    def test_numeric_seq_first_entry_of_day(self):
        """TD"""
        result = _handle_runs_prep_seq_files(
            today=self.today,
            file_last='001_01_test.md',
            seq_notation_loc=0,
            seq_start_loc=f'2025{self.hyphen}03{self.hyphen}14',
            hyphen=self.hyphen
        )

        self.assertEqual(result[0], '002_01')  # full sequence
        self.assertEqual(result[1], '002')     # main sequence
        self.assertEqual(result[2], 1)         # last main
        self.assertEqual(result[3], 2)         # next main


    def test_numeric_seq_second_entry_of_day(self):
        """TD"""
        with patch('builtins.print') as mock_print:
            result = _handle_runs_prep_seq_files(
                today=self.today,
                file_last='002_01_test.md',
                seq_notation_loc=0,
                seq_start_loc=f'2025{self.hyphen}03{self.hyphen}14',
                hyphen=self.hyphen
            )

            self.assertEqual(result[0], '002_02')  # full sequence
            self.assertEqual(result[1], '002')     # main sequence
            self.assertEqual(result[2], 2)         # last main
            self.assertEqual(result[3], 2)         # next main
            mock_print.assert_called_once_with('Note: You have submitted more than 1 entry today.')


    def test_date_seq_first_entry_of_day(self):
        """TD"""
        result = _handle_runs_prep_seq_files(
            today=self.today,
            file_last=f'2025{self.hyphen}03{self.hyphen}14_01_test.md',
            seq_notation_loc=1,
            seq_start_loc=f'2025{self.hyphen}03{self.hyphen}14',
            hyphen=self.hyphen
        )

        self.assertEqual(result[0], f'2025{self.hyphen}03{self.hyphen}15_01')
        self.assertEqual(result[1], f'2025{self.hyphen}03{self.hyphen}15')
        self.assertEqual(result[2], datetime(2025, 3, 14).date())  # last main should be previous day
        self.assertEqual(result[3], self.today.date())


    def test_date_seq_second_entry_of_day(self):
        """TD"""
        with patch('builtins.print') as mock_print:
            result = _handle_runs_prep_seq_files(
                today=self.today,
                file_last=f'2025{self.hyphen}03{self.hyphen}15_01_test.md',
                seq_notation_loc=1,
                seq_start_loc=f'2025{self.hyphen}03{self.hyphen}14',
                hyphen=self.hyphen
            )

            self.assertEqual(result[0], f'2025{self.hyphen}03{self.hyphen}15_02')
            self.assertEqual(result[1], f'2025{self.hyphen}03{self.hyphen}15')
            self.assertEqual(result[2], datetime(2025, 3, 15).date())  # last main should be previous day
            self.assertEqual(result[3], self.today.date())
            mock_print.assert_called_once_with('Note: You have submitted more than 1 entry today.')


    def test_invalid_notation_type(self):
        """Test invalid sequence notation type raises ValueError"""
        with self.assertRaises(ValueError):
            _handle_runs_prep_seq_files(
                today=self.today,
                file_last='001_01',
                seq_notation_loc=2,  # Invalid value
                seq_start_loc='2025-03-15',
                hyphen=self.hyphen
            )
