class Classmate(object):
    def __init__(self,s):
        self.nums=s
        self.num=0
        self.a=0
        self.b=1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num<self.nums:
            dd=self.a
            self.a,self.b=self.b,self.a+self.b
            self.num+=1
            return dd
        else:
            raise StopAsyncIteration
classmate=Classmate(10)
for name in classmate:
    new.append(name)
    print(name)