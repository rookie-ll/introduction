# 单继承
class People(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def says(self):
        print(self.name, self.age)


class Student(People):
    def __init__(self, classid, xuehao, name, age):
        People.__init__(self, name, age)
        self.classid = classid
        self.xuehao = xuehao

    def says(self):
        print(self.classid, self.xuehao, self.name, self.age)


people = People("刘大拿", 12)
people.says()
# 实例化
student = Student(123123, 111111, "刘二拿", 12)
print(student)
student.says()


# 多继承
class ClassA(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def hello(self):
        print( self.a, self.b)


class ClassB(object):
    def __init__(self, c):
        self.c = c

    def hello(self):
        print(self.c)


class ClassC(ClassA, ClassB):
    def __init__(self, a, b, c):
        ClassA.__init__(self, a, b)
        ClassB.__init__(self, c)

    def hello(self):
        print( self.a, self.b, self.c)

# 实例化
a=ClassA(1,3)
b=ClassB(22222)
c=ClassC(1,2,3)
a.hello()
b.hello()
c.hello()

print(c.__dict__)
print(ClassC.__mro__)