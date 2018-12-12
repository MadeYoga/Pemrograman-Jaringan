from pysnmp.hlapi import *
g = getCmd(
    SnmpEngine(),
    CommunityData('public'),
    UdpTransportTarget(('demo.snmplabs.com', 161)),
    ContextData(),
    ObjectType(ObjectIdentity('SNMPv2-MIB')),
               )
print(g)

# import netsnmp
# sess = netsnmp.Session(Version=2, DestHost='203.189.120.25', Community='public')
# vars = netsnmp.VarList(netsnmp.Varbind('iso.3.6.1.2.1.2.2.1.2'))
# a = sess.walk(vars)
# print (a)

# FTP, jika file tidak ditemukan
# cara ngelist file di server

# DNS TOOLS
# A, alias
# PTR, MX, AAAA, CNAME

# GEOIP, input dari nama, bukan ip.

# check router snmp ada ato tidak. # service nya.
