import socket
from threading import Thread

import threading

clients = {}

def broadcast(message):
    for client in clients:
        client.send(message)

def handle_client_join():
    while True:
        client, client_address = server_socket.accept()
        print(str(client_address) + " has connected to server")
        Thread(target=handle_client_messsage, args=(client, client_address,)).start()

def handle_client_messsage(client, client_address):
    clients[client] = client_address
    while True:
        try:
            message_from_client = client.recv(1024)
        except:
            print(clients[client][0] + " has disconnected")
            clients.pop(client)
            client.close()
            break
        if message_from_client == "quit":
            clients.pop(client)
            client.close()
            break
        broadcast(message_from_client)
    
server_socket = socket.socket()
host = socket.gethostname()
port = 16083
server_socket.bind((host, port))

server_socket.listen(5)

if __name__ == "__main__":
   # THREADING
   handle_client = threading.Thread(target=handle_client_join)
   handle_client.start()
   handle_client.join()