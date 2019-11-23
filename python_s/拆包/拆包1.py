a=(12,12,33,44,55,66)
b={"a":"www","b":"ssdfd"}
for i in a:
    print(i)

def fun(s,**f):
    print(s)
    print(*s)
    print(f)
    print(*f)


fun(a,**b)

