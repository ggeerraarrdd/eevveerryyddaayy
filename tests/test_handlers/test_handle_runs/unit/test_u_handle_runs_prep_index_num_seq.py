"""
TD
"""

from src.handlers.handle_runs import _handle_runs_prep_index_num_seq











def test_handle_runs_prep_index_num_seq():
    """Test numeric sequence gap handling with various scenarios"""
    lines = [
        '| 001   | col2   | col3   | col4   | col5   |\n'
    ]

    gap_line = '|    |    |    |    |\n'

    # Test no gap
    result = _handle_runs_prep_index_num_seq(
        seq_last=1,
        seq_next=2,
        lines=lines.copy(),
        target_line=1,
        gap_line=gap_line
    )
    assert len(result) == len(lines)  # original line + 2 gap entries
    assert result[0] == lines[0]

    # Test normal gap
    expected = [
        '| 001   | col2   | col3   | col4   | col5   |\n',
        '| 002   |    |    |    |    |\n',
        '| 003   |    |    |    |    |\n',
    ]

    result = _handle_runs_prep_index_num_seq(
        seq_last=1,
        seq_next=4,
        lines=lines.copy(),
        target_line=1,
        gap_line=gap_line
    )
    assert len(result) == 3  # original line + 2 gap entries
    assert result[0] == expected[0]
    assert result[1] == expected[1]
    assert result[2] == expected[2]

    # Test invalid sequence (next <= last)
    try:
        _handle_runs_prep_index_num_seq(
            seq_last=5,
            seq_next=3,
            lines=lines.copy(),
            target_line=0,
            gap_line=gap_line
        )
        assert False, "Expected ValueError"
    except ValueError as e:
        assert "Invalid sequence" in str(e)

    # Test max gap exceeded
    try:
        _handle_runs_prep_index_num_seq(
            seq_last=1,
            seq_next=33,  # 31 gaps, exceeds max_gap of 30
            lines=lines.copy(),
            target_line=0,
            gap_line=gap_line
        )
        assert False, "Expected ValueError"
    except ValueError as e:
        assert "Gap size" in str(e)
