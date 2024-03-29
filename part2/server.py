import socket
import time


#Definning Server INFO:
IP = "192.168.1.112"     # IP of the server
PORT = 8855              # PORT of the server
FORMAT = 'utf-8'         # A way to encode UNICODE character to a binary string and vice versa
serverName="Main Server" #Server Name
ADDR=((IP, PORT))       #list of IP and PORT of server as its address


SERVER = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   #AF_INET declare the type of the Address (IPV4), SOCK_DGRAM stands for UDP Servers type


SERVER.bind(ADDR)

print("[SERVER] Server STARTING...")
print(f"[SERVER] {serverName}")

#PROCCESSING
while True:
    encodedMsg, addr = SERVER.recvfrom(1024)
    message = encodedMsg.decode(FORMAT)
    Time = time.strftime("%H:%M:%S", time.localtime())
    print(f"Received message from {message} at {Time}")


