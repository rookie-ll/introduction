def fun(fun):
    def fun1():
        print("验证1")
        fun()
    return fun1
#@fun
def text():
    print("我是原函数")

text=fun(text)
text()