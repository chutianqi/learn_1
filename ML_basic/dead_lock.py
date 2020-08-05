from threading import Thread,currentThread,RLock,Lock

import time

mutexA=RLock()
mutexB=RLock()

class house(Thread):
    def run(self):
        self.room1()
        self.room2()

    def room1(self):
        mutexA.acquire()
        print(currentThread().name+'房间1拿到a锁')
        mutexB.acquire()
        print(currentThread().name+'房间1拿到b锁')
        mutexA.release()
        print(currentThread().name + '房间1释放a锁')
        mutexB.release()
        print(currentThread().name + '房间1释放b锁')


    def room2(self):
        mutexB.acquire()
        print(currentThread().name+'房间2拿到b锁')
        time.sleep(1)
        mutexA.acquire()
        print(currentThread().name + '房间2拿到a锁')
        mutexB.release()
        print(currentThread().name + '房间2释放b锁')
        mutexA.release()
        print(currentThread().name + '房间2释放a锁')


if __name__ == '__main__':
    for i in range(10):
        t = house()
        t.start()
