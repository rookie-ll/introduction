import socket
import re
def test(new_socket,res):
    '''模拟服务器发送给客户端的头'''
    #res=new_socket.recv(1024).decode("utf-8")
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
        f=open("word"+file_name,"rb")
    except:
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response+="\r\n"
        response+="find is not ..."
        new_socket.send(response.encode("utf-8"))
    else:
        html_content=f.read()
        f.close()
        response_body=html_content
        response_header = "HTTP/1.1 200 OK\r\n"
        response_header += "Content-length:%d\r\n"%len(response_body)
        response_header+="\r\n"
        response =response_header.encode("utf-8")+response_body
        new_socket.send(response)
        new_socket.send(html_content)

    #关闭套接字
    #new_socket.close()

def main():
    #创建一个套接字
    socket_tcp=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket_tcp.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    #绑定一个端口
    socket_tcp.bind(("",8888))
    #设置一个监听端口
    socket_tcp.listen(128)
    socket_tcp.setblocking(False)
    a=list()
    while True:
        try:
            #等待客户端链接
            new_socket,dk=socket_tcp.accept()
            #test(new_socket)
        except Exception as ret:
            pass
        else:
            new_socket.setblocking(False)
            a.append(new_socket)
        for i in a:
            try:
                recv_date=i.recv(1024).decode("utf-8")
            except Exception as ret:
                pass
            else:
                if recv_date:
                    test(i,recv_date)
                else:
                    i.close()
                    a.remove(i)

    socket_tcp.close()

if __name__=="__main__":
    main()