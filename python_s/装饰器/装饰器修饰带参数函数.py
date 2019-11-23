def fun1(fun):
    def fun2():
        print("hello")
        return fun()
    return fun2

#@fun1
def text():
    print("hello,hahahahge")

#text()

text=fun1(text)
#text()

#带参数

def funn1(vl):
    def funn2(fun):
        def funn3(*args,**kwargs):
            a,b,c=args
            print("hello%s%s%s%s"%(a,b,c,vl))
            return fun(*args,**kwargs)
        return funn3
    return funn2
@funn1("ll")
def test(a,b,c):
    print("nmbwcnm")

test("a","b","c")