#!/usr/bin/python

import cgi, cgitb

form = cgi.FieldStorage()
HOST = form.getvalue('host')

print ("Content-type:text/html\r\n\r\n")
print ('<html>')
print ('<head>')
print ('<title>CHECK SNMP</title>')
print ('</head>')
print ('<body>')

import netsnmp

try:
	print("<div>{} Service SNMP: </div>\n".format(HOST))
	print("<div> output: - ")
	sess = netsnmp.Session(Version=2, DestHost=HOST, Community='public') ## gak throw exception
	vars = netsnmp.VarList(netsnmp.Varbind('iso.3.6.1.2.1.2.2.1.2'))
	print("</div><div>jika output '-', maka terdapat service")
except Exception as e:
	print("<div>Host Not found!</div>")
	print("<div>" + e + "</div>")

print ('</body>')
print ('</html>')
