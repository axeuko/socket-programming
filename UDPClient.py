import socket

#create socket object

client_sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

message = 'This is Ground Control'

client_sock.sendto(message.encode('utf-8'),('127.0.0.1',12345))
data,addr = client_sock.recvfrom(4096)
print('ALEX: ')
print(str(data))
client_sock.close()

