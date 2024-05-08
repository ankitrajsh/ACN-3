# TCPPingerServer.py
import random
from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('192.168.254.1', 12000))

serverSocket.listen(1)
print("The server is ready to receive connections...")

while True:
    connectionSocket, clientAddress = serverSocket.accept()

    rand = random.randint(0, 11)

    message = connectionSocket.recv(1024).decode()

    print(f"Received message '{message}' from {clientAddress}")

    message = message.upper()

    if rand < 4:
        print("Packet lost (simulated)")
    else:
        connectionSocket.send(message.encode())
        print("Response sent")


    connectionSocket.close()
