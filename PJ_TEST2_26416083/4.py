#!C:\Users\MYPC\AppData\Local\Programs\Python\Python36\python.exe

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head> <title>TEST2, NOMER 4</title> <head>")
print("<body>")

import cgi, cgitb
import imaplib, poplib
import smtplib
import ftplib

form = cgi.FieldStorage()
ip_address = form.getvalue('domain')

print("<h3>{}</h3>".format(ip_address))

try:
    pop = poplib.POP3(ip_address)
    print("<div>POP3 enabled</div>")
except Exception as e:
    # print(e)
    if "[Errno 11001]" in str(e):
        print("<div>Host '{}' not found</div>".format(ip_address))
    else:
        print("<div>POP3 disabled</div>")

try:
    ftp = ftplib.FTP(ip_address)
    print("<div>FTP enabled</div>")
except Exception as e:
    # print(e)
    if "[Errno 11001]" in str(e):
        print("<div>Host '{}' not found</div>".format(ip_address))
    else:
        print("<div>FTP disabled</div>")

try:
    imap = imaplib.IMAP4(ip_address)
    print("<div>IMAP enabled</div>")
except Exception as e:
    # print(e)
    if "[Errno 11001]" in str(e):
        print("<div>Host '{}' not found</div>".format(ip_address))
    else:
        print("<div>IMAP disabled</div>")

try:
    smtp = smtplib.SMTP(ip_address)
    print("<div>SMTP enabled</div>")   
except Exception as e:
    # print(e)
    if "[Errno 11001]" in str(e):
        print("<div>Host '{}' not found</div>".format(ip_address))
    else:
        print("<div>SMTP disabled</div>")


print("</body></html>")
print("</html>")
