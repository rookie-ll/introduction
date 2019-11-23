#第一种实现生成器的方式
#a=(2*2 for i in range(10))
#print(a)


#第二种实现生成器的方式
def num(s):
    a, b=0, 1
    n=0
    while n<s:
        #print(a)
        yield a   #如果一个函数中有yield，那么这个函数就不是函数，而是一个生成器模板
        a,b=b,a+b
        n+=1
#如果调用函数的时候发现函数里面有yield，那么就不是调用函数，而是创建一个生成器对象
obj=num(10)
for i in obj:
    print(i)
