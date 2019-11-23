from collections import Iterable
from collections import Iterator
import time
class Classmate(object):
    def __init__(self,):
        self.names=list()
        self.num=0

    def add(self,name):
        self.names.append(name)

    def __iter__(self):
        return self

    def __next__(self):
        if self.num<len(self.names):
            dd=self.names[self.num]
            self.num+=1
            return dd
        else:
            raise StopAsyncIteration
classmate=Classmate()
classmate.add("老王")
classmate.add("王二")
classmate.add("张三")
print("判断对象是否为可迭代对象",isinstance(classmate,Iterable))

#classmate_interator=iter(classmate)
#print("判断对象是否为迭代器",isinstance(classmate_interator,Iterator))
#print(next(classmate_interator))
for name in classmate:
    time.sleep(1)
    print(name)