#!/usr/bin/python

import cgi, cgitb
import os
import GeoIP

# os.chdir('~/public_html/cgi-bin')

print ("Content-type:text/html\r\n\r\n")
print ('<html>')
print ('<head>')
print ('<title>GeoIP, Write to file</title>')
print ('</head>')
print ('<body>')
# print ('<h2>Hello Word! This is my first CGI program</h2>')

gi = GeoIP.open("/tmp/GeoLiteCity.dat", GeoIP.GEOIP_INDEX_CACHE | GeoIP.GEOIP_CHECK_CACHE) 
loc = gi.record_by_name(os.environ['REMOTE_ADDR'])
print (loc["city"])
print ("<div>" + os.environ["REMOTE_ADDR"] + "</div>")
print("<div>anda mengakses dari {}</div>".format(loc["country_name"]))

if loc["country_name"] == "Indonesia":
	print "<div>anda tidak dapat mengakses website ini</div>"

print("<div>WRITE IP & COUNTRY LOC TO FILE...</div>")
try:
	## WORKS WITH PYTHON3
	with open("log.txt", "a") as f:
 		log_text = "Access from IP: {}, Country: {}, \n".format(
 			os.environ["REMOTE_ADDR"]
 			loc["country_name"]
		)
		f.write(log_text)
except Exception as e:
	print(e)
print("<div>SUCCESS WRITE IPADDRESS & COUNTRY LOCATION TO FILE!</div>")
print ('</body>')
print ('</html>')
