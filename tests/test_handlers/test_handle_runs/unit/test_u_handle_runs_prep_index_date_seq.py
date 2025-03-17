"""
TD
"""

from datetime import datetime

from src.handlers.handle_runs import _handle_runs_prep_index_date_seq










def test_handle_runs_prep_index_date_seq():
    """Test date sequence gap handling with various scenarios"""
    lines = [
        '| 2025-03-15   | col2   | col3   | col4   | col5   |\n'
    ]

    gap_line = '|    |    |    |    |\n'
    hyphen = '-'

    # Test no gap
    result = _handle_runs_prep_index_date_seq(
        seq_last=datetime(2025, 3, 15).date(),
        seq_next=datetime(2025, 3, 16).date(),
        lines=lines.copy(),
        target_line=1,
        gap_line=gap_line,
        hyphen=hyphen
    )
    assert len(result) == len(lines)  # no new lines added
    assert result[0] == lines[0]

    # Test normal gap
    expected = [
        '| 2025-03-15   | col2   | col3   | col4   | col5   |\n',
        '| 2025-03-16   |    |    |    |    |\n',
        '| 2025-03-17   |    |    |    |    |\n',
    ]

    result = _handle_runs_prep_index_date_seq(
        seq_last=datetime(2025, 3, 15).date(),
        seq_next=datetime(2025, 3, 18).date(),
        lines=lines.copy(),
        target_line=1,
        gap_line=gap_line,
        hyphen=hyphen
    )
    assert len(result) == 3  # original line + 2 gap entries
    assert result[0] == expected[0]
    assert result[1] == expected[1]
    assert result[2] == expected[2]

    # Test max gap exceeded (31 days)
    try:
        _handle_runs_prep_index_date_seq(
            seq_last=datetime(2025, 3, 15).date(),
            seq_next=datetime(2025, 4, 15).date(),
            lines=lines.copy(),
            target_line=0,
            gap_line=gap_line,
            hyphen=hyphen
        )
        assert False, "Expected ValueError"
    except ValueError as e:
        assert "Date gap exceeds maximum allowed" in str(e)
