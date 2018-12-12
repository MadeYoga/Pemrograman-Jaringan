#!C:\Users\MYPC\AppData\Local\Programs\Python\Python36\python.exe

import cgi, cgitb 

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
first_name = form.getvalue('first')
# last_name  = form.getvalue('last')

slash_number = int(first_name)

slash_bin = ""

for i in range (32):
    if i < slash_number:
        slash_bin += "1"
    else:
        slash_bin += "0"

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Hello - Second CGI Program</title>")
print ("</head>")
print ("<body>")

print ("<h2>%s</h2>" % (first_name))
print("<h3>binary: " + slash_bin + "</h3>")

desimal_netmask = ""
desimal_netmask += str(int(slash_bin[:8], 2)) + "."
desimal_netmask += str(int(slash_bin[8:16], 2)) + "."
desimal_netmask += str(int(slash_bin[16:24], 2)) + "."
desimal_netmask += str(int(slash_bin[24:32], 2))

print("<h3>Netmask: " + desimal_netmask + "</h3>")
print ("</body>")
print ("</html>")
