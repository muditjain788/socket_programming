#!/usr/bin/python3
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),1234))
#in this we are connecting we sender by using method connect
##msg=s.recv(1024)
#buffer size is  1024 means maximum size of message that can be send 
full_msg=''
while True:
    msg=s.recv(8)
    if len(msg)<=0:
        break
    full_msg+=msg.decode("utf-8")
##print(msg.decode("utf-8"))
#decoding the  message recieved from sender in character form again
print(full_msg)
