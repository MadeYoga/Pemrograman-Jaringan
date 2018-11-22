#!C:\Users\MYPC\AppData\Local\Programs\Python\Python36\python.exe

import cgi, cgitb
import smtplib

form = cgi.FieldStorage()

sender = form.getvalue('from')

receivers = form.getvalue('to')

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>TEST 2 SMTP</title>")
print ("</head>")
print ("<body>")

if ',' in receivers:
    receivers = receivers.split(',')

recvs = ""
for receiver in receivers:
    recvs += receiver + ','
    print(receiver + "<br>")

mail_cc = form.getvalue('cc')
message = form.getvalue('message')

message = """
From: <{}>
To: <{}>
Subject: {}

{}
""".format(sender, recvs, mail_cc, message)

try:
   smtpObj = smtplib.SMTP('john.petra.ac.id')
   smtpObj.sendmail(sender, receivers, message)
   smtpObj.starttls()
   print ("<h1>Successfully sent email</h1></body></html>")
except Exception as e:
   print(e)
   print ("Error: unable to send email")






