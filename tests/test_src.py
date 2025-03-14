"""
Test the src module
"""

import os

import src










def test_src_module_structure():
    """Test that the src module exists and matches expected structure"""
    src_path = os.path.dirname(src.__file__)

    # Test main src directory
    assert os.path.isdir(src_path), "src directory should exist"
    assert os.path.isfile(os.path.join(src_path, "__init__.py")), "src/__init__.py should exist"
    assert os.path.isfile(os.path.join(src_path, "app.py")), "src/app.py should exist"

    # Test subdirectories that should be modules
    expected_modules = ["config", "forms", "handlers", "utils"]
    for dir_name in expected_modules:
        dir_path = os.path.join(src_path, dir_name)
        assert os.path.isdir(dir_path), f"src/{dir_name} directory should exist"
        assert os.path.isfile(os.path.join(dir_path, "__init__.py")), f"src/{dir_name}/__init__.py should exist"

    # Test templates directory (not a module)
    templates_path = os.path.join(src_path, "templates")
    assert os.path.isdir(templates_path), "src/templates directory should exist"
