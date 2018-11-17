#!C:\Users\MYPC\AppData\Local\Programs\Python\Python36\python.exe

import cgi, cgitb
import smtplib

import poplib
import getpass

form = cgi.FieldStorage()
user = form.getvalue("user")
password = form.getvalue("pass")

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Hello - Second CGI Program</title>")
print ("</head>")
print ("<body>")

M = poplib.POP3('john.petra.ac.id')
M.user(user)
# M.user(getpass.getuser())
try:
    M.pass_(password)
    print(len(M.list()[1]))
    print("<br>Berhasil login")
except Exception as e:
    print(e)



print ("</body>")