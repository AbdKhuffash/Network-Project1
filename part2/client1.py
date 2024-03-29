import socket


IP = '192.168.1.255'  # IP address of the server
PORT = 8855  # Port number for communication
ADDR= (IP, PORT)
FORMAT = 'utf-8'
DATA = {}
# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


# Get user input
firstName = input("Enter First Name:\n")
lastName = input("Enter Last Name:\n")
msg=input("Enter message:\n")

message = f"{firstName} {lastName}${msg}"

# Send the message to the server
client_socket.sendto(message.encode(FORMAT), ADDR)
i=int(1)

while True:

    # Receive the response from the server
    response, server_address = client_socket.recvfrom(2048)
    msg=response.decode(FORMAT)
    senderData = msg.split("$")
    senderADDR=senderData[0]
    DATA[senderADDR] = senderData
    senderName=DATA[senderADDR][1]
    receiveTime=DATA[senderADDR][3]
    dataList = list(DATA)

    for address in dataList:
        if address!=senderADDR:
            flag=False
        else:
            flag=True

    if flag==False:
        i=1



    print(f"[CLIENT] {i}- Received a message from {senderName} at {receiveTime}")
    print("=============================\n")
    i+=1

    choice=input("Enter message number to show followed by d ( S to skip) :\n")
    choice=choice[0]
    if choice.lower()=="s":
        continue
    else:
        print(f"Message is: {DATA[dataList[int(choice) - 1]][2]}")

# Close the socket
client_socket.close()