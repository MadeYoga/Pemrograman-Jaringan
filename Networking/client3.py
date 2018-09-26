import socket
import threading

sock = socket.socket()

sock.connect((socket.gethostname(), 16083))

def handle_connection():
    while True:
        try:
            response_from_server = sock.recv(1024)    
            print(response_from_server)
        except:
            break
        
client_thread = threading.Thread(target=handle_connection)
client_thread.start()

while True:
    message_to_send = input("send: ")
    if message_to_send == "quit":
        break
    try:
        sock.send(message_to_send.encode())
    except Exception as e:
        print(e)
        break

print("run complete")