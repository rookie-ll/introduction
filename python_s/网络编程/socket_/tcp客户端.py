import socket

def main():
    #1.创建tcp的套接字
    tcp_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #2.链接服务器
    tcp_fwq=tcp_socket.connect(("192.168.33.21",port))
    

    #3.发送数据/接收数据
    tcp_fwq.send("要发的数据".encode("utf-8")

    #4.关闭套接字
    tcp_socket.close()

if __name__="__main__":
    main()
