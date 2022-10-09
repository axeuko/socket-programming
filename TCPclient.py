import socket
import sys

#we are going towrite a program such that we can see the interaction between client and server

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client_socket.connect(('127.0.0.1', 12345))#this takes a tuple of port number and ipaddress
payload = "yo Gang"

try:
    while True:
        client_socket.send(payload.encode('utf-8'))
        data = client_socket.recv(1024)#1024 is the buffer size
        print(str(data))
        more = input("want to send more data to the server ")
        if more.lower()=='y':
            payload = input("ENTER PAYLOAD: ")
        else:
            break
except KeyboardInterrupt:
    print("Exited by user")

client_socket.close()
    
        
        
