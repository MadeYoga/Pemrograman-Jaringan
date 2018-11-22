import getpass
import sys

domain = sys.argv[1]
username = sys.argv[2]
file = sys.argv[3]

import os
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

from ftplib import FTP

ftp = FTP(domain)

password = getpass.getpass()

try:
    ftp.login(username, password)
    print("Login sukses")
    print("Uploading {} ...".format(file))
    ftp.storbinary("STOR {}".format(file), open(file, "rb"))
    print("Upload Success {}".format(file))
except Exception as e:
    print(e)
    
ftp.quit()
