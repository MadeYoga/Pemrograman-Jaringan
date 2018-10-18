import socket

hostname = input("input hostname: ")

try:
    results = socket.gethostbyname_ex(hostname)
    print(results)
    for ip in results[2]:
        print (ip)
    print ( "{} memiliki {} ip address".format(results[0], str(len(results[2]) )) )
except Exception as e:
    print ("{}\nhost not found".format(e))
    