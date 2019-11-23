import socket
def get_shuju(udp_socket):
    dest_ip = input("请输入目标ip")
    dest_port = int(input("请输入目标端口"))
    get_date = input("请输入您要发送的信息")
    udp_socket.sendto(get_date.encode("UTF-8"), (dest_ip, dest_port))


def jieshou(udp_socket):
    recv_date = udp_socket.recvfrom(1024)
    print("%s:%s" % (str(recv_date[1]), recv_date[0].decode("JBK")))


def main():
    #创建套接字
    udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #绑定信息
    udp_socket.bind(("",7788))
    #while处理聊天流程
    while True:
        #获取要发送的内容
        get_shuju(udp_socket)

        #接受数据
        jieshou(udp_socket)


if __name__=="__main__":
    main()