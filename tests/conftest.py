"""
TD
"""

import os
import sys
import pytest










# Get the project root directory
def pytest_sessionstart(session):  # pylint: disable=unused-argument
    """
    Configure Python path before test session starts
    """
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__)))
    sys.path.insert(0, project_root)


@pytest.fixture(scope="session")
def get_project_root():
    """
    Fixture to provide project root path
    """
    return os.path.abspath(os.path.join(os.path.dirname(__file__)))


@pytest.fixture(scope="session")
def get_src_path(project_root):
    """
    Fixture to provide src directory path
    """
    return os.path.join(project_root, "src")


@pytest.fixture(scope="session")
def get_tests_path(project_root):
    """
    Fixture to provide tests directory path
    """
    return os.path.join(project_root, "tests")
