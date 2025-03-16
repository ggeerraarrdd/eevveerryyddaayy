"""
TD
"""

from datetime import datetime
import pytest

from src.handlers.handle_runs import _handle_runs_prep_seq_no_files









def test_sequence_generation_for_empty_directory():
    """Test sequence generation for empty directory"""
    today = datetime(2025, 3, 15)
    hyphen = '\u2011'

    # Numeric sequence
    result = _handle_runs_prep_seq_no_files(today, 0, hyphen)
    assert result[0] == '001_01'  # full sequence
    assert result[1] == '001'     # main sequence
    assert result[2] is None      # last main should be None
    assert result[3] is None      # next main should be None

    # Date sequence
    result = _handle_runs_prep_seq_no_files(today, 1, hyphen)
    assert result[0] == f'2025{hyphen}03{hyphen}15_01'  # full sequence
    assert result[1] == f'2025{hyphen}03{hyphen}15'     # main sequence
    assert result[2] is None                            # last main should be None
    assert result[3] is None                            # next main should be None

    # Act & Assert - Invalid notation
    with pytest.raises(ValueError) as exc_info:
        _handle_runs_prep_seq_no_files(today, 2, hyphen)
    assert str(exc_info.value) == 'Invalid configuration: Expected 0 or 1.'
