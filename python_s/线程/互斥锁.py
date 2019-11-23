import threading
hucisuo=threading.Lock()
sum=0

def test1(sums):
    global sum
    #上锁
    hucisuo.acquire()
    for i in range(sums):
        sum+=1
    #解锁
    hucisuo.release()
    print(sum)

def test2(sums):
    global sum
    hucisuo.acquire()
    for i in range(sums):
        sum+=1
    hucisuo.release()
    print(sum)


def main():
    t=threading.Thread(target=test1,args=(1000000,))
    t2=threading.Thread(target=test2,args=(1000000,))
    t.start()
    t2.start()


if __name__=="__main__":
    main()