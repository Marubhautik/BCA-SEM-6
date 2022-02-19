import socket
port = 60000
s=socket.socket()
host = socket.gethostname()
s.bind((host,port))
s.listen(5)

print('Server listening....')

while True:
    conn, addr = s.accept()
    print('Got connection from',addr)
    data = conn.recv(1024)
    print('Server received',repr(data))
    filename = 'mytext.txt'
    f = open(filename,'rb')
    l = f.read(1024)
    while(l):
        conn.send(l)
        print('sent',repr(l))
        l = f.read(1024)
    f.close()
    print('Done sending')
    conn.send(b'Thank you for connecting')
    conn.close()
'''Server listening....
Got connection from ('192.168.10.62', 50388)
Server received b'Hello server!'
sent b'Maru Bhautik\r\ndharmesh\r\nhitesh'
Done sending'''