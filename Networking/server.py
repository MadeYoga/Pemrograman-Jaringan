# PROTOCOL
# TCP / UDP , ICMP->ping, traceroute
# HOSTNAME -> DNS -> convert name<->IP

import socket               # Import socket module
import threading
from threading import Thread
import asyncio

clients = {}
addresses = {}

def broadcast(message):
   print("broadcast")
   for sock in clients:
      sock.send(message)

def client_join_handler():
   while True:
      client, client_address = s.accept()
      print(str(client_address) + " has connected to server")
      addresses[client] = client_address
      Thread(target=client_handler, args=(client,)).start()
   
def client_handler(client):
   clients[client] = "anon"
   while True:
      msg = client.recv(1024)
      #client.send(msg)
      broadcast(msg)
   
s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 16083                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
s.listen(5)              # Now wait for client connection.

if __name__ == "__main__":
   # THREADING
   handle_client = threading.Thread(target=client_join_handler)
   handle_client.start()
   handle_client.join()

   # ASYNC WAY
   #loop = asyncio.get_event_loop()
   #loop.create_task(asyncio.start_server(handle_client, 'localhost', 16083))
   #try:
   #   loop.run_forever()
   #except KeyboardInterrupt:
   #   loop.close()

async def handle_client(client):
   #if not clients[client]:
   if not clients[client]:
      clients[client] = "anon"
   while True:
      msg = client.recv(1024)
      broadcast(msg)

async def run_server():
   while True:
      client, client_address = s.accept()
      print(str(client_address) + " has connected to server")
      addresses[client] = client_address
      loop.create_task(handle_client(client))
