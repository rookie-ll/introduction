class A():
    def __init__(self):
        self.name="hello"
        self.__age=2

    def __test(self):
        print(self.__age)

class B(A):
    def __init__(self):
        super(B, self).__init__()

b=B()
print(b)

