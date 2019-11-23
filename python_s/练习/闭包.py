def fun(ass):
    a=ass
    def fun2():
        print("hello"+a)
    return fun2
a=fun("刘大拿")
a()
fun("刘大拿")()