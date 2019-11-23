from multiprocessing import Pool
import time,os,random

def worker(msg):
    s_start=time.time()
    print("%s开始执行，进程号为%d"%(msg,os.getpid()))
    time.sleep(random.random()*2)
    t_stop=time.time()
    print(msg,"执行完毕，耗时%0.2f"%(t_stop-s_start))


pDo=Pool(3)
for i in range(10):
    pDo.apply_async(worker,(i,))

print("start")
time.sleep(3)
pDo.close()

print("end")
