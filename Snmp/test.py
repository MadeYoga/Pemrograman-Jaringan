from pysnmp.hlapi import *
g = getCmd(SnmpEngine(),
           CommunityData('public'),
           UdpTransportTarget(('demo.snmplabs.com', 161)),
           ContextData(),
           ObjectType(ObjectIdentity('SNMPv2-MIB'))

# FTP, jika file tidak ditemukan
# cara ngelist file di server

# DNS TOOLS
# A, alias
# PTR, MX, AAAA, CNAME

# GEOIP, input dari nama, bukan ip.

# check router snmp ada ato tidak. # service nya.
           
