def fun(fun):
    def fun2(*args,**kwargs):
        print("俺可是装饰器哦")
        return fun(*args,**kwargs)
    return fun2

@fun
def text(a,*args,**kwargs):
    print("我是被装饰的函数")
    return "ojbk"

ret=text(1,3,4,5,d=22)
print(ret)