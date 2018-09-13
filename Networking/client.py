import socket
import threading

def handler_connection(server_socket):
    request = server_socket.recv(1024)
    print(request.encode())

s = socket.socket()
host = socket.gethostname()
port = 16083

s.connect((host, port))

# print(s.recv(1024))
while True:
    msg = input("send: ")
    s.send(msg.encode())

    print(str(s.recv(1024)))

s.close()
