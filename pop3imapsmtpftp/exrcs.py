import getpass
import imaplib, poplib
import smtplib
import ftplib
ip_address = input("input: ")

try:
    pop = poplib.POP3(ip_address)
    print("POP3 enabled")
except Exception as e:
    print(e)
    if "[Errno 11001]" in str(e):
        print("Host not found")
        # quit() ## quit early
    else:
        print("POP3 disabled")

try:
    ftp = ftplib.FTP(ip_address)
    print("FTP enabled")
except Exception as e:
    print(e)
    if "[Errno 11001]" in str(e):
        print("Host not found")
    else:
        print("FTP disabled")

try:
    imap = imaplib.IMAP4(ip_address)
    print("IMAP enabled")
except Exception as e:
    print(e)
    if "[Errno 11001]" in str(e):
        print("Host not found")
    else:
        print("IMAP disabled")

try:
    smtp = smtplib.SMTP(ip_address)
    print("SMTP enabled")   
except Exception as e:
    print(e)
    if "[Errno 11001]" in str(e):
        print("Host not found")
    else:
        print("SMTP disabled")
