import socket
import time

IP = '192.168.1.100'  # IP address of the server
PORT = 8855  # Port number for communication
ADDR= (IP, PORT)
FORMAT = 'utf-8'
CLIENTS={}

# Create a UDP socket
SERVER = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the IP address and port
SERVER.bind(ADDR)

print("[SERVER] Server STARTING...")

while True:
    # Receive a message and the client's address
    message, client_address = SERVER.recvfrom(2048)
    print(f"[SERVER] Received message: {message.decode(FORMAT)} from {client_address}")
    receivedMsg=message.decode(FORMAT)
    clientData=receivedMsg.split('$')
    print(clientData)
    Time = time.strftime("%H:%M:%S", time.localtime())
    clientData.append(Time)
    CLIENTS[client_address] = clientData
    print(CLIENTS)

    for key in CLIENTS:
        messageToSend = f"{key}${CLIENTS[key][0]}${CLIENTS[key][1]}${CLIENTS[key][2]}"
        print(f"Message : {messageToSend}")
        response = f"{messageToSend}"
        for key in CLIENTS:
            SERVER.sendto(response.encode(FORMAT), key)