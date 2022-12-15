"""
Script: test_formatter.py
By:Richard Vaughan
Purpose: Code that calls Formatter.py and performs testing using unitest.
Unittest requires that tests are put into classes as methods and 
special assertion methods in the unittest.TestCase class are used 
instead of the built-in assert statement
Prerequisites: None.
Tested: On python 3.10 on Windows 11.
Revision history:
Alpha Version: 16OCT22
Notes:
"""

import unittest
import formatter


class TestFormatter(unittest.TestCase):
    def test_lower(self):
        test_text = "JOHN ORAW"
        result = formatter.convert_lower(test_text)
        self.assertEqual(result, "john oraw")

    def test_upper(self):
        test_text = "John ORaw"
        result = formatter.convert_upper(test_text)
        self.assertEqual(result, "JoHN ORAW")


if __name__ == "__main":
    unittest.main()
