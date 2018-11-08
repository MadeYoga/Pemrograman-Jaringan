# active mode yang active client, download dari server
# server buka port baru untuk upload file
# FTP client, default PASSIVE mode
# ACTIVE, tidak dipisah command dan data
# PASSIVE, PORT 21 command, PORT
# Streaming juga dari client.
# FTP. anonymous FTP,
# user: anon
# pass: a@a.com
# put, upload
# get, download
# ftp://ftp.ubuntu.com

from ftplib import FTP
import getpass
import os
os.chdir(r"C:\Users\MYPC\Desktop\Pemjar\FTP")

# USER
# PASS
# PASSIVE

username = input("user: ")
password = getpass.getpass()

ftp = FTP('john.petra.ac.id')

# ftp.set_pasv(True) set to passive, by default: passive
try:
    ftp.login(username, password)
except Exception as e:
    print(e)
ftp.retrlines("LIST")		# list files
# ftp.cwd("")		        # change into a directory
ftp.retrbinary("RETR perl1.pl", open("perl1.pl", "wb").write)

# Upload text file:
# ftp.storlines("STOR namaFile", open("localFile","rb"))

# Upload binary file: aman gunakan binary
ftp.storbinary("STOR namaLokal", open("namaLokal","rb"))
ftp.retrlines("LIST")		# list files
ftp.quit()


