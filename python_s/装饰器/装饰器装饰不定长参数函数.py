def fun(fun):
    def fun2(*args,**kwargs):
        print("俺是个装饰器")
        #fun(args,kwargs)
        fun(*args,**kwargs)
    return fun2

@fun
def text(a,*args,**kwargs):
    print("hahahahhage%d"%(a))
    print("sssss",args)
    print("sssss",kwargs)

text(122)
text(122,333,444)
text(123,444,555,m=22)