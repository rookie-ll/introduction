class Text(object):
    def __init__(self,fun):
        self.fun=fun

    def __call__(self, *args, **kwargs):
        print(args)
        print(kwargs)
        print("俺是装饰器鸭")
        return self.fun(*args,**kwargs)

@Text
def fun(a,b,c=22):
    return "hahaha%d%d%d"%(a,b,c)

print(fun(1,2.3))