import socket


#create socket object
#then bind to an ip and port
#then enter send and recieve loop

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(('127.0.0.1',12345))#takes a tuple of ip and port


while 1:
    #for sending data with udp we use recvfrom of socket module and this returns data as well as address
##in TCP when the connection is formed the address doesnt change thats why we just use recv()
    # in udp there is no connection so we have to recieve the address so that we know where to send the address back to
    

    data,addr = sock.recvfrom(4096)#we pass an integer that represents the number of bytes you want to accept
#the message size of the udp shoud be equal to the packet size
    #now to send data to the client
    print(str(data))
    message =  "this is ALEX" #we have to sent this in bytes and encode the message also
    sock.sendto(message.encode('utf-8'),addr)
    


    

