def fun(a):
    def fun2():
        s=0
        s=a+1
        return s
    return fun2
sss=fun(2)
sss()

sa=fun(12)()
print(sa)
#我觉得像一个函数生成器
