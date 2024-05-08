# Import necessary modules
import random
from socket import *


serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('192.168.227.1', 12000))

print('Server is ready to receive requests...')

while True:
 
    rand = random.randint(0, 11)

    message, address = serverSocket.recvfrom(1024)

    message = message.decode().upper()  

    if rand < 4:
        continue

    # Otherwise, the server responds
    serverSocket.sendto(message.encode(), address)  # Encode string to bytes before sending
