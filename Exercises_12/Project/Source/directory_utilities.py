"""
Script: directory_utilities.py
By:Richard Vaughan
Purpose: Script provided by JOR for directory utilities.
Prerequisites: None.
Tested: On python 3.10 on Windows 11.
Revision history:
Alpha Version: 18OCT22
Notes:
directory_utilities.py
By: JOR
Date: 01
OCT22
"""
import os
import sys
import platform

# Define global variables
current_working_directory = None


def detect_os() -> str:
    # Detect the OS in use
    return platform.system()


def detect_working_directory() -> str:
    # Returns the directory this script was run from
    return os.getcwd()


if __name__ == '__main__':
    print(f"This module executes as a standalone script")

    # Check the OS in use, lower case
    my_os = detect_os()
    my_os = my_os.lower()

    # Parse the response, only check for Windows and Linux
    if my_os == "windows":
        print("Your system is Windows")
    elif my_os == "linux":
        print("Your system is Linux")
    else:
        print(f"Cannot continue, unidentified system = {my_os}")
        sys.exit()
    # Get the current working directory
    current_working_directory = detect_working_directory()
    print(f"You are coding in: {current_working_directory}")
else:
    print(f"This module is called {__name__} and is being called by another script")
