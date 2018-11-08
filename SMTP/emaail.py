# SMTP PORT 25
# MUA (mail user agent)
# PORT 25 saat MTA (Mail Transport Agent),
# e.g microsoft exchange, lotus
# Linux -> postfix, exim, sendmail,

# DNS tugasnya record MX (10/15/20) alamat...

# MUA -> MTA -> INT -> MTA -> MUA
# mail ditampung di MTA, mail server.
# diambil dengan POP3(port 110)/imap(143).

# DNS, SMTP tidak ter enkripsi

# POP3s (993)
# IMAPS (345)

# TLS/SSL

# SMTP COMMANDS
# HELO <domain>,
# EHLO,
# RCPT To user@domain.com,
# MAIL FROM asal@domain.com,
# DATA

# MTA Petra john.petra.ac.id / peter.petra.ac.id

import smtplib

sender = 'm26416083@john.petra.ac.id'
receivers = ['m26416083@john.petra.ac.id']

message = """From: Made <m26416083@john.petra.ac.id>
To: Made <m26416083@john.petra.ac.id>
Subject: TESTING SMTP

HALLO WORLD TEST
"""

try:
   smtpObj = smtplib.SMTP('john.petra.ac.id')
   smtpObj.sendmail(sender, receivers, message)         
   print ("<html><body><h1>Successfully sent email</h1></body></html>")
except Exception as e:
   print(e)
   print ("Error: unable to send email")





