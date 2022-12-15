"""
Script: ftp_02.py
By:Richard Vaughan
Purpose: Script to download a file from ftp.heanet.ie using FTP protocol using a dictionary.
Prerequisites: None.
Tested: On python 3.10 on Windows 11.
Revision history:
Alpha Version: 16OCT22
Notes:
"""

import ftplib

FTP = {"PATH": '/mirrors/ubuntu-cdimage/releases/22.04/release', "FILENAME": 'SHA256SUMS',
       "URL": 'ftp.heanet.ie'}
# Make the connection
ftp = ftplib.FTP(FTP['URL'])
# Anonymous login
ftp.login()
# Change to the correct directory
ftp.cwd(FTP["PATH"])
# Retrieve the file
ftp.retrbinary("RETR " + FTP["FILENAME"], open(FTP["FILENAME"], 'wb').write)
ftp.quit()
