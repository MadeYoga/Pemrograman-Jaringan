import socket
from threading import Thread

addresses = {}

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (socket.gethostname(), 16083)
server_socket.bind(server_address)

def broadcast(message):
    for address in addresses:
        server_socket.sendto(message.encode(), address)

def run_server():
    while True:
        print("wating to receive message!")
        message_from_client, address = server_socket.recvfrom(4096)
        print(address)
        if not address in addresses:
            addresses[address] = message_from_client
        print(address[0] + ": " + str(message_from_client))
        broadcast(address[0] + ": " + str(message_from_client))

    server_socket.close()
    
Thread(target=run_server).start()