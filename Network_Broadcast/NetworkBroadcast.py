## INPUT IP ADDRESS & SUBNET MASK ##
## OUTPUT NETWORK & BROADCAST ADDRESS

from Network_Util import get_broadcast_address, get_network_address, isIpValid, isSubnetValid
from NetworkUtil import NetworkUtility

network = NetworkUtility()
while True:
    ip_address = input ("input ip address: ")
    if network.isIpValid(ip_address):
        break

while True:
    subnet_mask = input("input subnet mask: ")
    if network.isSubnetValid(subnet_mask):
        break

print( "Valid Ip Address : " + ip_address  )
print( "Valid Subnet Mask: " + subnet_mask )
print( '-----------------------------------------')
print( "Network Address  : " + network.get_network_address  (ip_address, subnet_mask ))
print( "Broadcast Address: " + network.get_broadcast_address(ip_address, subnet_mask ))