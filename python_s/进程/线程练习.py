import multiprocessing
import time
def test(a):
    while True:
        print("我是一个进程%d"%a)
        time.sleep(1)

def test2(a):
    while True:
        print("我是第二个进程%d"%a)
        time.sleep(1)

def main():

    m1=multiprocessing.Process(target=test,args=(2,))
    m1.start()
    test2(222)

if __name__=="__main__":
    main()
