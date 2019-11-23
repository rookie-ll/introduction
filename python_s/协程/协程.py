import time
def test1():
    while True:
        print("test1")
        yield
        time.sleep(1)

def test2():
    while True:
        print("test2")
        yield
        time.sleep(1)
t1=test1()
t2=test2()
while True:
    next(t1)
    next(t2)