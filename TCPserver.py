#!/usr/bin/python3

#Importing the socket module
import socket 

#Creating a socket object with a socket function as its value containing the socket family and socket type
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


host = socket.gethostname() #Host is the server IP
port = 1120 #Port to listen to

# Bind the socket to the host and port
serversocket.bind((host, port))

# Number of connections to listen at a time
serversocket.listen(5) 

# Waiting for a connection
while True:
    clientsocket, address = serversocket.accept()

    print("Recived connection from %s" % str(address))

    message = "Hello, thank you for connecting to the server" + "\r\n"

    # Message sent to the client after a succefull connection
    clientsocket.send(message.encode("utf-8")) #Encode message to bytes before sending


    # Close the client socket to end communication
    clientsocket.close()