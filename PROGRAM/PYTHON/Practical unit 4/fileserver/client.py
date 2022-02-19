import socket

s= socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)
port = 60000
print(ip)
s.connect((ip,port))
s.send(b"Hello server!")
with open('received file','wb') as f:
    print('file opened')
    while True:
        print('receiving data...')
        data = s.recv(1024)
        print('data = %s',(data))
        if not data:
            break
        f.write(data)
    f.close()
    print('Successfully get the file')
    s.close()
    print('connection closed')
'''192.168.10.62
file opened
receiving data...
data = %s b'Maru Bhautik\r\ndharmesh\r\nhitesh'
receiving data...
data = %s b'Thank you for connecting'
receiving data...
data = %s b''
Successfully get the file
connection closed'''
