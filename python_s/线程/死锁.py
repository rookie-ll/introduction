import threading
import  time
suoA=threading.Lock()
suoB=threading.Lock()

def test1():
    suoA.acquire()
    time.sleep(1)
    print("test1")
    suoB.acquire()
    suoB.release()


def test2():
    suoB.acquire()
    time.sleep(1)
    print("sest2")
    suoA.acquire()
    suoA.release()


def main():
    t1=threading.Thread(target=test1)
    t2=threading.Thread(target=test2())
    t1.start()
    t2.start()


if __name__=="__main__":
    main()