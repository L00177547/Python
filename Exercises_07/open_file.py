"""
Script: open_file.py
By:Richard Vaughan
Purpose: open a file called logfile.txt and write Test Line to the file.
Prerequisites: None.
Tested: On python 3.10 on Windows 11.

Revision history:
Alpha Version: 08OCT22
Notes:

"""

my_filename = "logfile.txt"
try:
    # Open File logfile.txt ( w(write) can be replaced with a(append) or r(read)).
    with open(my_filename, "w") as file_handle:
        print(f"Writing a test line to {my_filename}")
        file_handle.write("Test line")
except IOError as err:
    print(f"IOError was {err}")
except EOFError as err:
    print(f"End of file error was {err}")
except OSError:
    print("OS Error")
except:
    print("General Error")
else:
    print("File created")
finally:
    print("Finishing up!")
    # close not needed because with statement
    # file_handle.close()
