#事件（Event)
'''
线程间的通信
'''
import threading, time


class Boss(threading.Thread):
    def run(self):
        print('boss : 从现在开始996')
        #事件设置
        print(event.isSet())
        event.set()
        time.sleep(3)
        print('boss : 你被辞退了')

if __name__ =='__main__':
    event=threading.Event()

class worker(threading.Thread):
    def run(self):
        event.wait()
        print('worker : 不想干')
        event.clear()
        event.wait()
        print('worker : oh year')

if __name__ =='__main__':
    event=threading.Event()

    threads=[]
    for i in range(5):
        threads.append(worker())
    threads.append(Boss())

    for t in threads:
        t.start()