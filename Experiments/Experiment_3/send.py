import socket
# 创建一个socket:
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 9999))
client_name = b'LQH'
s.send(client_name)

print(s.recv(1024).decode('utf-8'))
while True:
    message = input("INPUT:").encode()
    if message:
        s.send(message)
    else:
        continue
    data = s.recv(1024)
    if data:
        print(data.decode('utf-8'))
s.close()
'''Data:asd To:a
INPUT:Data:qwe To:a
INPUT:Data:zxc TO:a'''

'''Data:fff To:DNB
INPUT:Data:PPP To:DNB
INPUT:Data:YYY To:DNB'''