import socket
def main():
    #创建一个套接字
    udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #获取对方的ip
    dest_ip=input("请输入对方的ip")
    #获取对方的端口
    dest_post=int(input("请输入对方的端口"))
    #从键盘获取数据
    use_date=input("请输入您要发送的数据")

    udp_socket.sendto(use_date.encode("UTF-8"),(dest_ip,dest_post))

    #接收会送过来的数据
    recv_adte=udp_socket.recvfrom(1024)
    #套接字是可以同时收发数据的
    print(recv_adte)
    udp_socket.close()


if __name__=="__main__":
    main()