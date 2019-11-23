class Cat(object):
    lis = [1,2,3,4,5,6]

    def __init__(self, name):
        self.name = name
        self.__age = 23

    def cat_say(self):
        print(self.name)

    @classmethod
    def get_lists(cls):
        return cls.lis


tom = Cat("tom")
'''print(tom)
addr = id(tom)
print("%x", addr)
print(tom._Cat__age)'''
s=tom.get_lists()[1]
print(s)