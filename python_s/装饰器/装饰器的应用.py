def fun(fun):
    def fun2():
        return "<h1>"+fun()+"</h1>"
    return fun2

def funn(funn):
    def funn2():
        return "<td>"+funn()+"</td>"
    return funn2

@fun
@funn
def text():
    return "hahhahha"

print(text())