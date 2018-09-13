import socket
import threading
from threading import Thread

import asyncio
import time 
def connection_handler(server_socket):
    print("aaab")
    while True:
        response = server_socket.recv(1024)
        print("\nanon: " + str(response)[2:-1])

s = socket.socket()
host = socket.gethostname()
port = 16083

s.connect((host, port))

Thread(target=connection_handler, args=(s,)).start()

while True:
    msg = input("send: ")
    s.sendall(msg.encode())

s.close()
