import socket
def main():

    #创建一个套接字
    user_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #链接服务器
    tcp_conent=user_socket.connect(("192.168.46.1",port))
    #发送数据
    tcp_conent.send("要发的数据".encode("utf-8"))
    #关闭套接字
    user_socket.close()

if __name__=="__main__":
    main()