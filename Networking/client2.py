import socket
from threading import Thread

client_socket = socket.socket()
client_socket.connect((socket.gethostname(), 16083))

disconnected = False

def message_handler(client_socket):
    while True:
        try:
            response_from_server = client_socket.recv(1024)
        except:
            # disconnected = True
            pass
        print(response_from_server)

Thread(target=message_handler, args=(client_socket,)).start()

while True:
    msg = input("send: ")
    if msg == "quit" or disconnected:
        break
    client_socket.sendall(msg.encode())

client_socket.close()