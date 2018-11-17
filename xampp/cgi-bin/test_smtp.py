#!C:\Users\MYPC\AppData\Local\Programs\Python\Python36\python.exe

import cgi, cgitb
import smtplib

form = cgi.FieldStorage()

sender = form.getvalue('from')

receivers = form.getvalue('to')
if ',' in receivers:
    receivers = receivers.split(',')

mail_cc = form.getvalue('cc')
mail_bcc = form.getvalue('bcc')
message = form.getvalue('message')

message = """
From: <{}>
To: <{}>
Subject: TEST SMTP

{}
""".format(sender, receivers, message)

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Hello - Second CGI Program</title>")
print ("</head>")
print ("<body>")

for receiver in receivers:
    print(receiver)

try:
   smtpObj = smtplib.SMTP('john.petra.ac.id')
   smtpObj.sendmail(sender, receivers, message)
   smtpObj.starttls()
   print ("<h1>Successfully sent email</h1></body></html>")
except Exception as e:
   print(e)
   print ("Error: unable to send email")






