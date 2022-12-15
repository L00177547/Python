"""
Script: pylint2.py
By:Richard Vaughan
Purpose: Testing using pylint - This Code  gets 10/10
Prerequisites: None.
Tested: On python 3.10 on Windows 11.
Revision history:
Alpha Version: 16OCT22
Notes:
"""


def pylint_test():
    """
    Test Pylint
    """
    a_1 = 1
    b_1 = 2
    c_1 = "JOR"
    print(a_1 + b_1)
    print(a_1 + b_1)
    print(str(a_1) + c_1)


pylint_test()

if __name__ == '__main__':
    print("")
    pylint_test()
else:
    print(f"This module is called {__name__} and is being called by another script")
