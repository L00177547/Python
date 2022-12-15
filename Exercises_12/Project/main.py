"""
Script: main.py
By:Richard Vaughan
Purpose: Code to test the OS and check for the working directory called from 
directory_utilities.py in the Source folder.
Prerequisites: None.
Tested: On python 3.10 on Windows 11.
Revision history:
Alpha Version: 23OCT22
Notes:
"""


from Source.directory_utilities import detect_os, detect_working_directory

print(detect_os())
print(detect_working_directory())
