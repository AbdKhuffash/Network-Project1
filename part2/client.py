import socket
import time


#SERVER DATA:
IP = '192.168.1.255'  # IP of the server
PORT = 8855     # PORT of the server
FORMAT = 'utf-8' # A way to encode UNICODE character to a binary string and vice versa
ADDR= (IP, PORT) #list of IP and PORT of server as its address

CLIENT = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #AF_INET declare the type of the Address (IPV4), SOCK_DGRAM stands for UDP Servers type

#Proccessing
while True:
    # Get user input
    firstName = input("Enter First Name:\n")
    lastName = input("Enter Last Name:\n")
    message = f"{firstName} {lastName}"

    # Send the message to the server
    while True:
        time.sleep(2)
        CLIENT.sendto(message.encode('utf-8'), ADDR)

# Close the connection
CLIENT.close()