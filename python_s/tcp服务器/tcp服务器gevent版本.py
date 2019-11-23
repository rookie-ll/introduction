import socket
import gevent
from gevent import monkey
import re

monkey.patch_all()
def test(new_socket):
    '''模拟服务器发送给客户端的头'''
    res=new_socket.recv(1024).decode("utf-8")
    reslines=res.splitlines()
    print(reslines)
    #print(res)
    ret=re.match(r"[^/]+(/[^ ]*)",reslines[0])
    file_name=""
    if ret:
        file_name=ret.group(1)
        print("*"*20,file_name)
        if file_name=="/":
            file_name="index.html"
    try:
        f=open(file_name,"rb")
    except:
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response+="\r\n"
        response+="find is not ..."
        new_socket.send(response.encode("utf-8"))
    else:
        html_content=f.read()
        f.close()
        # 准备发送给浏览器的数据
        response = "HTTP/1.1 200 OK\r\n"
        response += "\r\n"
        #将头部和主体一起发送到浏览器
        new_socket.send(response.encode("utf-8"))
        new_socket.send(html_content)

    #关闭套接字
    new_socket.close()

def main():
    #创建一个套接字
    socket_tcp=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #socket_tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    #绑定一个端口
    socket_tcp.bind(("",8888))
    #设置一个监听端口
    socket_tcp.listen(128)
    while True:
        #等待客户端链接
        new_socket,dk=socket_tcp.accept()
        gevent.spawn(test,new_socket)
    #p1=multiprocessing.Process(target=test,args=new_socket)
    socket_tcp.close()

if __name__=="__main__":
    main()