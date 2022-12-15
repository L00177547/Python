"""
Script: ftp_03.py
By:Richard Vaughan
Purpose: Script to download a file from ftp.heanet.ie using FTP protocol using a seperate dictionary
stored in the settings folder.
Prerequisites: None.
Tested: On python 3.10 on Windows 11.
Revision history:
Alpha Version: 16OCT22
Notes:
"""

import ftplib
import settings.ftp as settings

# Make the connection
ftp = ftplib.FTP(settings.FTP['URL'])
# Anonymous login
ftp.login()
# Change to the correct directory
ftp.cwd(settings.FTP["PATH"])
# Retrieve the file
ftp.retrbinary("RETR " + settings.FTP["FILENAME"], open(settings.FTP["FILENAME"], 'wb').write)
ftp.quit()
