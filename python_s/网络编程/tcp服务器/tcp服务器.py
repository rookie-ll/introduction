import socket
def main():
    #创建一个套接字
    tcp_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #绑定一个端口
    tcp_socket.bind(("",2323))
    #设置这个端口为监听端口
    tcp_socket.listen(128)
    while True:
        #循环为多个客户端服务
        #等待客户端链接
        print("等待客户端链接到服务器...")
        new_socket,useradd=tcp_socket.accept()

        print("一个新的客户端已经到来%s"%(str(useradd)))

        while True:
            #循环为同一个客户端服务多次
            #接受客户端的请求
            revc_date=new_socket.recv(1024)
            print("客户端发送过来的请求是:%s"%(revc_date.decode("utf-8")))

            #如果revc解堵塞，要不就是接收到了数据，要不就是对方调用了close，如果调用close，则revc_date为空字符串
            if revc_date:
                #回复客户端信息
                new_socket.send("你好啊".encode('UTF-8'))
            else:
                break
        #关闭套接字
        tcp_socket.close()
        print("服务结束")
    new_socket.close()

if __name__=="__main__":
    main()