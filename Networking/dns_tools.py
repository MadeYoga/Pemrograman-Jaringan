import socket
import dns.resolver
import dns.reversename

from NetworkUtil import NetworkUtility

## NS
## MX, A, AAAA(IPV6)

## Reverse
# PTR, TXT(informasi domain tsb)

# print(socket.gethostbyname('google.com'))
# print(socket.gethostbyname_ex('google.com'))
# print(socket.getaddrinfo('google.com', 80))
# print(socket.gethostbyaddr("203.189.120.4")) # reverse PTR

network = NetworkUtility()

ip_address = input("input IP address?")
while not network.isIpValid(ip_address):
    ip_address = input("input IP address?")
    
try:
    output = socket.gethostbyaddr(ip_address)
except:
    print("host not found")
print(output[0]) 

## input domain
domain_name = input("input domain name?")
output = socket.gethostbyname_ex(domain_name)
for ip in output[2]:
    print(ip)

# USABLE IP
# (2 ^ (32 - mask)) - 2

# 1024 / 24

# 3. input ip address, netmask
# output network address, broadcast address
# input : 10.0.0.67, mask: 26
# output: 10.0.0.64 bc: 10.0.0.127
