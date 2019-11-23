import  threading
import time
lis=[1,1,2,2,3,3]
def test():
    print("我是一个任务")
    print(lis)
    time.sleep(1)

def test2():
    print("我是另一个任务")
    print(lis)
    lis.append(11)
    time.sleep(1)
for i in range(10):
    T=threading.Thread(target=test)
    s=threading.Thread(target=test2)
    T.start()
    s.start()
