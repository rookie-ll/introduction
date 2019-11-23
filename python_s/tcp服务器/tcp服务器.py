import socket
def s(new_socket):
    # 回应客户端
    res = new_socket.recv(1024)
    reques = "HTTP/1.1 200 OK"
    reques += "\r\n"
    reques += "主体内容"
    new_socket.send(reques.encode("utf-8"))
    new_socket.close()


def main():
    # 创建一个套接字
    tcp_ser = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 绑定端口
    tcp_ser.bind(('',7080))
    # 设置为监听端口
    tcp_ser.listen(128)
    while True:
        #等待接收用户消息
        new_socket,kd=tcp_ser.accept()
        s(new_socket)
    tcp_ser.close()
if __name__ == "__main__":
     main()
