import socket
hostname=socket.gethostname()
ip_address=socket.gethostbyname(hostname)
print(f"Hostname:{hostname}")
print(f"ip address:{ip_address}")


'''Hostname:STUD-PC
ip address:192.168.10.62'''