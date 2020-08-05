'''
进程：每个进程有自己独立的内存，例如在windows中，一个运行的.exe就是一个进程
多线程：一个进程有多个线程，多个线程可以共享数据
'''
import threading
import time
import random

num=100

def my_print(info):
    # time.sleep(random.randint(1,10))
    global num
    num=num-1
    print(num)
if __name__ == "__main__":
    t1 = threading.Thread(target=my_print, args=('线程1',))
    t2 = threading.Thread(target=my_print, args=('线程2',))
    t3 = threading.Thread(target=my_print, args=('线程3',))
    t4 = threading.Thread(target=my_print, args=('线程4',))
    t5 = threading.Thread(target=my_print, args=('线程5',))

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    print('do something')

