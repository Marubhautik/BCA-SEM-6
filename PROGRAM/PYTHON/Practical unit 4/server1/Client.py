import pr

#take the server name and port name

host ='192.168.10.62'
port=5000

#create a socket at server side using TCP/IP protocol
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#bind the socket with server and port number
s.bind((host,port))

#allow maximum 1 connection to the socket
s.listen(1)
c,addr=s.accept()
print("CONNECTION FROM :",str(addr))
c.send(b"HELLO,How are you?\Welcome to Bhautik hacking  world")

msg = "Bye......................"
c.send(msg.encode())
c.close()