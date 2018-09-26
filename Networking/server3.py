import socket
import threading

clients = {}

def broadcast(message):
    for client in clients:
        client.send(message)

def run_server():
    while True:
        client, client_address = sock.accept()
        print(client_address[0] + " connected to server")
        threading.Thread(target=handle_client, args=(client, client_address,)).start()

def handle_client(client, client_address):
    clients[client] = client_address
    while True:
        try:
            message_from_client = client.recv(1024)
        except:
            print(client_address[0] + " disconnected")
            break
        print (message_from_client)
        broadcast(message_from_client)
        if message_from_client == "quit":
            break
    client.close()
    del clients[client]
        
sock = socket.socket()
server_address = (socket.gethostname(), 16083)
sock.bind(server_address)

sock.listen(5)

server = threading.Thread(target=run_server)
server.start()
server.join()