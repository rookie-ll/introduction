
a=10
b=11
a=a+b
b=a-b
a=a-b
print(a)
print(b)

lis=[1,2,3,4,5,6,7,8]
s=lis[::-1]
s.reverse()
print(s)

class Class(object):
    def __init__(self,name,s):
        self.name=name
        self.s=s

    def prints(self):
        print(self.name)
        print(self.s)

class Student(Class):
    def __init__(self,sname):
        self.sname=sname
        Class.__init__(self,name,s)



#匿名函数的应用

def sun(a,b,fun):
    s=fun(a,b)
    return s


print(sun(1, 2, lambda x, y: x + y))
