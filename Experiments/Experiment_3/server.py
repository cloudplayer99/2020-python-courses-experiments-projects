import re
import threading
import socket
import time


client = {}
Data_Set_DNB = []
Data_Set_LQH = []


def tcplink(sock, addr):
    name = sock.recv(1024).decode('utf-8')
    # print(name)
    # print(addr[0], addr[1])
    client[name] = addr[0] + ':' + str(addr[1])
    # print(Client)
    print("Accept new connection from %s:%s..." % addr)
    print("online terminal: {}".format(len(client)))
    sock.send(b'Welcome!')
    while True:
        if name == "LQH":
            data = sock.recv(1024)
            time.sleep(1)
            if not data or data.decode('utf-8') == 'exit':
                break
            # print(re.findall(r'Data:(.+?)\sTo:(.+?)', data.decode('utf-8')))
            Myfind = re.findall(r'Data:(.+?)\sTo:(.+?)', data.decode('utf-8'))
            if Myfind:
                Data, Client = Myfind[0]
            # sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
                if Data and Client:
                    Data_Set_DNB.append(Data)
                    # print(Data)
        if name == "DNB":
            if Data_Set_DNB:
                # print(Data_Set)
                sock.send(Data_Set_DNB[0].encode())
                Data_Set_DNB.pop()
    sock.close()
    print("Connection from %s:%s closed." % addr)


if __name__ == '__main__':

    # server_addr = '10.15.26.39'
    server_addr = '127.0.0.1'
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((server_addr, 9999))
    server.listen(2)
    print("Waiting for connection...")
    while True:
        sock, addr = server.accept()
        t = threading.Thread(target=tcplink, args=(sock, addr))
        t.start()
    pass
