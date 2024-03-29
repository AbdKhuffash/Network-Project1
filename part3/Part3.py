from socket import *
from jinja2 import *

serverPort = 9977
serverSocket = socket(AF_INET,SOCK_STREAM) #TCP Socket
#serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind(('192.168.1.100', serverPort)) #server socket binded with server port
serverSocket.listen(1) #listen for 1 tcp connectio request. Server can handle atmost one queued connection at a time


print ("The server is ready to receive")
while True:
        connectionSocket, addr= serverSocket.accept() #clients sends tcp conn request-> connectiosocket made
        sentence = connectionSocket.recv(2048).decode()
        print (addr)
        print (sentence)

        ip = addr[0]
        port = addr[1]

        #this to write on the html , using jinja2 library; will read the Error_temp.html ,will recognize the ip/port,
        # and then write on Error.html ip/port

        with open('Error_temp.html', 'r') as file:
            Error_content = file.read()
        template = Template(Error_content)
        variables ={
            'port':port,
            'ip':ip
        }
        rendered_template = template.render(**variables)
        #print(rendered_template)
        with open("Error.html",'w') as file:
            file.write(rendered_template)

        #request=sentence.split()[1] #spliting the sentace and accessing second word
        words = sentence.split()

        # Check if the list has at least two elements before accessing the second element
        if len(words) >= 2:
            request = words[1]
            #print("Request:", request)
        else:
            print("Invalid sentence format")
            break;

        print(f"HTTP Request: {request}")

        if (request == '/'  or request == '/main-en.html' or request=='/en' or request=='/index.html'): # English ; / /main-en.html
            # /en /index.html will result the same html
            connectionSocket.send("HTTP/1.1 200 OK \r\n".encode()) #http response status "200 ok"
            connectionSocket.send("Content-Type: text/html; charset=utf-8 \r\n".encode()) #send html file, text/html
            connectionSocket.send("\r\n".encode()) #sends the bytes b'\r\n' through the connectionSocket,
            # used to send  line ending sequence to indicate the end of a request or a section of data in a network protocol.
            f = open("main-en.html", "rb") #loading main-en.html//
            #allows you to read the content of the file a binary data^
            connectionSocket.send(f.read())

        elif (request=='/ar'):#Arabic
            connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
            connectionSocket.send("Content-Type: text/html; charset=utf-8\r\n".encode())
            connectionSocket.send("\r\n".encode())
            f = open("main-ar.html", "rb")
            connectionSocket.send(f.read())

        elif(request.endswith('.html')):
            connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
            connectionSocket.send("Content-Type: text/html; charset=utf-8\r\n".encode())
            connectionSocket.send("\r\n".encode())
            f = open("extension.html", "rb")
            connectionSocket.send(f.read())

        elif (request.endswith('.css')):
            connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
            connectionSocket.send("Content-Type: text/css; charset=utf-8\r\n".encode()) #connection type text/css;
            # to specify that the data being sent is CSS (Cascading Style Sheets) content.
            connectionSocket.send("\r\n".encode())
            f = open("styles.css", "rb")
            connectionSocket.send(f.read())

        elif (request.endswith('.jpg')):
            connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
            connectionSocket.send("Content-Type: image/jpeg; charset=utf-8\r\n".encode()) #t to specify that the data being sent is jpeg/image content.
            connectionSocket.send("\r\n".encode())
            f = open("net.jpg", "rb")
            connectionSocket.send(f.read())

        elif (request.endswith('.png')):
            connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
            connectionSocket.send("Content-Type: image/png; charset=utf-8\r\n".encode())#to specify that the data being sent is png/image content.
            connectionSocket.send("\r\n".encode())
            f = open("net.PNG", "rb")
            connectionSocket.send(f.read())


        elif (request=='/so'):
            connectionSocket.send("HTTP/1.1 307 Temporary Redirect  \r\n".encode())
            connectionSocket.send("Content-Type: text/html; charset=utf-8 \r\n".encode())
            connectionSocket.send("Location: https://stackoverflow.com  \r\n".encode())
            connectionSocket.send("\r\n".encode())

        elif (request=='/yt'):
            connectionSocket.send("HTTP/1.1 307 Temporary Redirect  \r\n".encode())
            connectionSocket.send("Content-Type: text/html \r\n".encode())
            connectionSocket.send("Location: https://youtube.com  \r\n".encode())
            connectionSocket.send("\r\n".encode())

        elif (request=='/rt'):
            connectionSocket.send("HTTP/1.1 307 Temporary Redirect  \r\n".encode())
            connectionSocket.send("Content-Type: text/html \r\n".encode())
            connectionSocket.send("Location: https://ritaj.birzeit.edu/  \r\n".encode())
            connectionSocket.send("\r\n".encode())

        else:
            connectionSocket.send("HTTP/1.1 404 Not Found  \r\n".encode())
            connectionSocket.send("Content-Type: text/html; charset=utf-8\r\n".encode())
            connectionSocket.send("\r\n".encode())

            f = open("Error.html", "rb")
            connectionSocket.send(f.read())

connectionSocket.close()


