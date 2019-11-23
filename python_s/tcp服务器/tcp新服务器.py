import socket
def s(new_socket):
    # 回应客户端
    #接收浏览器发过来的请求
    res = new_socket.recv(1024).decode("utf-8")
    print(res)
    reques = "HTTP/1.1 200 OK\r\n"
    reques += "\r\n"
    #reques += "主体内容"
    f=open("index.html","rb")
    f_con=f.read()
    f.close()
    #response header 发送给浏览器
    new_socket.send(reques.encode("utf-8"))
    #将response body 发送给浏览器
    new_socket.send(f_con)
    #关闭套接字
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