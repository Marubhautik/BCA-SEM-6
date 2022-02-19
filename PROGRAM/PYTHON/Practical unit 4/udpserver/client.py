import socket

msgFromClient = "Hello UDP Server Maru"

bytesToSend = str.encode(msgFromClient)
serverAddressPort =("127.0.0.1",20001)
buffersize =1024
UDPClientSocket = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)

UDPClientSocket.sendto(bytesToSend,serverAddressPort)
msgFromClient = UDPClientSocket.recvfrom(buffersize)

msg = "Message from Server{}".format(msgFromClient[0])
print(msg)

'''Message from Serverb'Hello UDP Client Bhautik'''