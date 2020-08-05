from multiprocessing import Process
import os
import threading

def work():
    #开启多个进程，每个进程都有独立的pid
    p1 =Process(target = work)
    p2 =Process(target = work)
    p3 =Process(target = work)
    p1.start()
    p2.start()
    p3.start()
    print('主进程-----》》线程PID', os.getpid())

    #在主进程开启多个线程，每个线程pid都一样，所以都在一个进程下工作
    t1=threading.Thread(target = work)
    t2=threading.Thread(target = work)
    t3=threading.Thread(target = work)
    t1.start()
    t2.start()
    t3.start()
    print('主进程-----》》线程pid',os.getpid())


