import multiprocessing


def main():
    #put放数据，get取数据，
    q=multiprocessing.Queue(3)
    q.put(2222)
    q.put("wwww")
    q.put([22,33])

if __name__=="__main__":
    main()
