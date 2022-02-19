import socket

localip ="127.0.0.1"
localport = 20001
buffersize = 1024

msgFromServer = "Hello UDP Client Bhautik"
bytesToSend = str.encode(msgFromServer)

UDPServerSocket = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localip,localport))

print("UDP server up and listening")
while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(buffersize)
    message = bytesAddressPair[0]
    address =bytesAddressPair[1]
    clientmsg = "message from client:{}".format(message)
    clientip = "Client ip address:{}".format(address)
    print(clientmsg)
    print(clientip)
    UDPServerSocket.sendto(bytesToSend,address)

'''UDP server up and listening
message from client:b'Hello UDP Server Maru'
Client ip address:('127.0.0.1', 59407)
'''