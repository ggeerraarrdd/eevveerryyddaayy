"""
TD
"""

import unittest

from src.utils import PackageManager










class TestPackageManager(unittest.TestCase):
    """
    TD
    """
    def setUp(self):
        self.package_manager = PackageManager()

    def test_get_value_valid_input(self):
        """Test getting a value with valid dictionary and key"""
        value = self.package_manager.get_value('package', 'day')
        self.assertEqual(value, '')

    def test_get_value_invalid_dict(self):
        """Test getting a value with invalid dictionary name"""
        with self.assertRaises(KeyError):
            self.package_manager.get_value('invalid_dict', 'day')

    def test_get_value_invalid_key(self):
        """Test getting a value with invalid key"""
        with self.assertRaises(KeyError):
            self.package_manager.get_value('package', 'invalid_key')

    def test_update_value_valid_input(self):
        """Test updating a value with valid inputs"""
        self.package_manager.update_value('package', 'day', '1')
        value = self.package_manager.get_value('package', 'day')
        self.assertEqual(value, '1')

    def test_get_dictionary_valid(self):
        """Test getting a valid dictionary"""
        package_dict = self.package_manager.get_dictionary('package')
        self.assertIsInstance(package_dict, dict)
        self.assertIn('day', package_dict)

    def test_reset_all(self):
        """Test resetting all dictionaries"""
        self.package_manager.update_value('package', 'day', '1')
        self.package_manager.reset()
        value = self.package_manager.get_value('package', 'day')
        self.assertEqual(value, '')

    def test_reset_specific_dict(self):
        """Test resetting specific dictionary"""
        self.package_manager.update_value('package', 'day', '1')
        self.package_manager.reset(['package'])
        value = self.package_manager.get_value('package', 'day')
        self.assertEqual(value, '')
