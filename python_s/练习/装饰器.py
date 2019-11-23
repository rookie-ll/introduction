def fun(fun):
    def fun2():
        fun()
        print("hello")
        return fun
    return fun2



@fun
def test():
    print("hi")

test()