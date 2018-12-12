from ftplib import FTP
import getpass

username = input("user: ")
password = getpass.getpass()

try:
    ftp = FTP('john.petra.ac.id')
except Exception as e:
    print(e)
    
try:
    ftp.login(username, password)
    ftp.retrlines("LIST")
    files = ftp.nlst()
    print(files)
    file_to_retr = input("input file yang ingin di retr: ")
    if file_to_retr in files:
        ftp.retrbinary("RETR " + file_to_retr, open(file_to_retr, "wb").write)
    else:
        print("No such file or directory named " + file_to_retr)
except Exception as e:
    print(e)
