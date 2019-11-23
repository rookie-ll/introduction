def fun(fun):
    print("俺要开始装你来")
    def fun2():
        print("俺是一个装饰器")
        return fun()
    return fun2

def fun3(funn):
    print("俺也要装你来")
    def fun4():
        print("俺也是一个装饰器")
        return funn()
    return fun4

@fun
@fun3
def test():
    print("俺只是一个普通函数")

test()