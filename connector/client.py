import socket


def connect(ip, port):
    # 声明socket类型，同时生成链接对象
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 6999))  # 建立一个链接，连接到本地的6969端口

    while True:
        data = client.recv(1024)  # 接收一个信息，并指定接收的大小 为1024字节
        print('recv:', data.decode())  # 输出我接收的信息

    client.close()  # 关闭这个链接
