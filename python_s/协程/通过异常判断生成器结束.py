def num(s):
    a, b=0, 1
    n=0
    while n<s:
        #print(a)
        yield a   #如果一个函数中有yield，那么这个函数就不是函数，而是一个生成器模板
        a,b=b,a+b
        n+=1
#如果调用函数的时候发现函数里面有yield，那么就不是调用函数，而是创建一个生成器对象
obj=num(2)
while True:
    try:
        ret=next(obj)
        print(ret)
    except Exception as ret:
        break
