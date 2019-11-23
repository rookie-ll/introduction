def fun(fun):
    print("哈哈哈哈嗝，我要开始装饰你了")
    def fun2(n):
        print("我是装饰器，你已被装饰了")
        fun(n)
    return fun2

@fun
def text(n):
    print(n)

@fun
def text2(s):
    print(s)

text(2)
text2(3)