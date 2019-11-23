class Cat():
    wode=list()
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

    def __del__(self):
        print("实例对象已被干掉了")

    def __str__(self):
        print("这里是打印类名显示的东西")

    @staticmethod
    def print():
        print("hahahah")

    def geta(self):
        print(self.a)

    @classmethod
    def getc(cls):
        print(cls.wode)

cat=Cat(1,2,3)
print(cat.a)
cat.print()
cat.geta()
Cat.getc()
print(Cat)
print(cat)