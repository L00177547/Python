"""
Script: mytime.py
By:Richard Vaughan
Purpose: Demonstrate how to work with the datetime and time modules
Prerequisites: None.
Tested: On python 3.10 on Windows 11.
Revision history:
Alpha Version: 16OCT22
Notes:
"""

# import datetime as dt.
from datetime import datetime as dt
# import strftime from time.
from time import strftime

# Get the current time, returns a value like 2022-10-09 17:46:45.151666
today = dt.now()
print(today)
# Get Unix time, returns a value like 1665566809.057217
unix_epoch_time = dt.timestamp(today)
print(unix_epoch_time)
# Display strftime help.
help(strftime)
weekday = dt.now().strftime("%A")
month = dt.now().strftime("%B")
print(f"{weekday}")
print(f"{month}")
hours = dt.now().strftime("%H")
minutes = dt.now().strftime("%M")
seconds = dt.now().strftime("%S")
print(f"The Time in (hours:minutes:seconds)is:{hours}:{minutes}:{seconds}")
dayofmonth = dt.now().strftime("%d")
monthdecimal = dt.now().strftime("%m")
year = dt.now().strftime("%Y")
print(f"Today's Date is DD/MM/YYY: {dayofmonth}/{monthdecimal}/{year}")
