#!/usr/bin/python3
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#s is a socket object  "IPV4"         "TCP"
s.bind((socket.gethostname(),1234))
#binding the socket and getting the host address of pc's ip and port no can be
#any but below 1234 are occupied
s.listen(5)
#this is queue so that the server doesn't get the load 
while True:
    clientsocket, address=s.accept()
    #socketobject ip of client   method to get the mentioned
    print(f"Connection from {address} has been established!")
    clientsocket.send(bytes("welcome,to my server","utf-8"))
    #now we are sending message to client in form of bytes by encoding them to 
    #bytes to that transfer can be easy
    clientsocket.close()
