def fun():
    a=122
    def fun2():
        nonlocal a
        print(a)
        a=100
        print(a)
    return fun2

fun()()