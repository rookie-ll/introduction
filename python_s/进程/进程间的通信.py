import multiprocessing


def download_date(q):
    date=[1,2,3,4,5]
    for i in date:
        q.put(i)

def cl(q):
    newdate=list()
    while True:
        date=q.get()
        newdate.append(date)
        if q.empty():
            break
    print(newdate)

def main():
    q=multiprocessing.Queue()
    p1=multiprocessing.Process(target=download_date,args=(q,))
    p2=multiprocessing.Process(target=cl,args=(q,))
    p1.start()
    p2.start()

if __name__=="__main__":
    main()
