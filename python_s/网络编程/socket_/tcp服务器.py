import socket
def main():
    
    #1.创建套接字
    tcp_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    #2.绑定端口
    tcp_socket.bind("",2323)
    
    #3.设置监听端口
    tcp_socket.listen(128)
    
    #4.等待客户端链接
    new_socket,lianjiekehuduandizhi=tcp_socket.accept()

    #5.接受客户端发送的请求
    recv_date=new_socket.recv(1024)#返回一个字符串

    #回送一部分数据给客户端
    new_socket.send("收到数据了".encode("utf-8"))
    
    #6.关闭套接字
    tcp_socket.close()
    new_socket.close()

if __name__=="__main__":
    main()
