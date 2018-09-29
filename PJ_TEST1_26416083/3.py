import socket

domain_name = input("input domain name?")
try:
    output = socket.gethostbyname_ex(domain_name)
    for ip in output[2]:
        print(ip)
except Exception as e:
    print("domain name, not found!")
    print(e)
