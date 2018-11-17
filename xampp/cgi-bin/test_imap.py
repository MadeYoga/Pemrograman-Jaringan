#!C:\Users\MYPC\AppData\Local\Programs\Python\Python36\python.exe

import cgi, cgitb
import smtplib

import imaplib
import getpass

form = cgi.FieldStorage()
user = form.getvalue("user2")
password = form.getvalue("pass2")

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Hello - Second CGI Program</title>")
print ("</head>")
print ("<body>")

M = imaplib.IMAP4('john.petra.ac.id')
# M.user(getpass.getuser())
try:
    M.login(user, password)
    M.select()
    print("<br>Berhasil login")
except Exception as e:
    print(e)

M.close()
M.logout()

print ("</body>")