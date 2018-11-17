#!C:\Users\MYPC\AppData\Local\Programs\Python\Python36\python.exe

import os

print ("Content-type:text/html\r\n\r\n")
print ('<html>')
print ('<head>')
print ('<title>Hello Word - First CGI Program</title>')
print ('</head>')
print ('<body>')
print ('<h2>Hello Word! This is my first CGI program</h2>')

# for param in os.environ.keys():
#     print ("<b>%20s</b>: %s<br>" % (param, os.environ[param]))

print("<h3>anda akses dari ip: " + os.environ['REMOTE_ADDR'] + "</h3>")

if "HTTP_VIA" in os.environ.keys():
    print("<h1>VIA proxy: " + os.environ['HTTP_VIA'] + "</h1>")
    print("<h1>IP proxy: " + os.environ['HTTP_X_FORWARDED_FOR'] + "</h1>")
else:
    print("<h1>tidak menggunakan proxy</h1>")

print ('</body>')
print ('</html>')

