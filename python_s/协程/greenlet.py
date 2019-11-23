import greenlet
import time
def test1():
    while True:
        print("1")
        gr2.switch()
        time.sleep(1)


def test2():
    while True:
        print("2")
        gr2.switch()
        time.sleep(1)

gr1=greenlet.greenlet(test1)
gr2=greenlet.greenlet(test2)

#切换到gr1中运行
gr1.switch()