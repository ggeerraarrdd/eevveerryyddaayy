"""
Utility Functions for Validating Project State
"""

# Local
from src.config import ConfigManager










def validate_project(
        config: ConfigManager = ConfigManager()
    ) -> bool:
    """
    Validate project is initialized or not.

    Parameters
    ----------
        None

    Returns
    -------
        bool
            True if this is first run (no files and no SEQ_START value), 
            False if regular run (files exist and SEQ_START set),

    Raises
    ------
        ValueError
            If project is in an invalid state regarding files and SEQ_START
    """
    is_seq_date = bool(config.get('PROJ_START'))

    # Project is not initialized if PROJ_START is not set
    if not is_seq_date:
        return False

    # Project is initialized if PROJ_START exists
    return True
