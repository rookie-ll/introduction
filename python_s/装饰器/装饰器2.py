import time

def fun(fun):
    def fun2():
        s=time.time()
        fun()
        st=time.time()
        print(st-s)
    return fun2

@fun
def text():
    for i in range(233333):
        print()

text()