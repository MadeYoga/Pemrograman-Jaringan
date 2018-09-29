import socket
from threading import Thread

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (socket.gethostname(), 16083)
client_socket.connect(server_address)

def handle_connection():
    while True:
        try:
            data, server = client_socket.recvfrom(4096)
            print("\nrecieved data from server: " + str(data))
        except Exception as e:
            print(e + "\nDestroy 'handle connection' Thread")
            break

Thread(target=handle_connection).start()

stop = False
while True:
    message_to_send = input("send: ")
    if message_to_send == "quit" or stop:
        break
    client_socket.sendto(message_to_send.encode(), server_address)
    #data, server = client_socket.recvfrom(4096)
    #print("\nrecieved data from server: " + str(data))

client_socket.close()
    
