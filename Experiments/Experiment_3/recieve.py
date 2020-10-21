import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))
client_name = b'DNB'
s.send(client_name)
while True:
    data = s.recv(1024)
    if data:
        print(data.decode('utf-8'))
    message = input("INPUT:").encode()
    if message:
        s.send(message)
    else:
        continue
s.close()
