## INPUT IP ADDRESS & SUBNET MASK ##
## OUTPUT NETWORK & BROADCAST ADDRESS

from Network_Util import get_broadcast_address, get_network_address, isIpValid, isSubnetValid

while True:
    ip_address = input ("input ip address: ")
    if isIpValid(ip_address):
        break

while True:
    subnet_mask = input("input subnet mask: ")
    if isSubnetValid(subnet_mask):
        break

print( "Valid Ip Address : " + ip_address  )
print( "Valid Subnet Mask: " + subnet_mask )
print( '-----------------------------------------')
print( "Network Address  : " + get_network_address  (ip_address, subnet_mask ))
print( "Broadcast Address: " + get_broadcast_address(ip_address, subnet_mask ))