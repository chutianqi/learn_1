from threading import Thread

class Hello(Thread):
    def __init__(self,name):
        super().__init__()
        self.name = name

    def run(self):
        print('hello %s' % self.name)


t=Hello('我是一个线程的类')
t.start()
print('我是主线程')

