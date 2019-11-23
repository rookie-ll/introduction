import  threading
import time

def jump():
    print("1")
    time.sleep(2)


def sing():
    print("2")
    time.sleep(2)


def main():
    t1=threading.Thread(target=sing)
    t2=threading.Thread(target=jump)
    t1.start()
    t2.start()

if __name__=="__main__":
    main()