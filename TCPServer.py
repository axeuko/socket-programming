#the server has to do alot more work than the client
#we will write a server that sends and recieves data from client
#AF_INET refers to the address family of ipv4

import socket
import sys

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #create server object

server_socket.bind(('127.0.0.1',12345))#this takes a tuple of port number and ipaddress

server_socket.listen(5)#it takes a backlog parameter. 5 here meansthat 5 connections can keep waiting if the server is busy but a 6th connection will be refused


while True:

    print("server waiting for connection")
    client_socket,addr = server_socket.accept()
    print("client connected from ", addr)

    while True: # the second while loop to get the data and send the data to the client
        data = client_socket.recv(1024) #to recieve data from the client, the max slize is 1024
        if not data or data.decode('utf-8')=='END':
            break    
        print("recieved from client: %s" %data.decode("utf-8"))
        try:
            client_socket.send(bytes('Wagwan bigC','utf-8'))
        except:
            print('exited by the user')

    client_socket.close()



        
        
