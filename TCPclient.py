#!/usr/bin/python3

# Importing the socket module
import socket

# Creating a socket object
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
host = socket.gethostname()
port = 1120

# Connect to the server
clientsocket.connect((host, port))

# Recieving a maximum of 1024 bytes
message = clientsocket.recv(1024)

# Close the client socket after receiving the message
clientsocket.close()

# Decode and print the received message
print(message.decode("utf-8"))
