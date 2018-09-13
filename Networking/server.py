# PROTOCOL
# TCP / UDP , ICMP->ping, traceroute
# HOSTNAME -> DNS -> convert name<->IP

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 16083                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   request = c.recv(1024)
   print ('Got connection from ' + str(addr))
   c.sendall(request)
   c.close()                # Close the connection

#c.close()
