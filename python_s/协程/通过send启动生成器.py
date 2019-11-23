def num(s):
    a, b=0, 1
    n=0
    while n<s:
        yield a
        a,b=b,a+b
        n+=1
obj=num(2)
ret=next(obj)
print(ret)

ret=obj.send("hahahha")
print(ret)