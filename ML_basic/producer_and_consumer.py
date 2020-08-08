import threading, time

condition=threading.Condition()
product=10

class producer(threading.Thread):
    def run(self) -> None:
        global condition,product
        while True:
            if condition.acquire():
                if product <= 1:
                    product +=1
                    print('{}:{}库存不足，商品数量小于10，努力生产中，现在总商品数量是{}'.format('生产者',threading.currentThread().getName(),product))
                    condition.notify() #从等待池中唤醒一个等待的线程，notifyall是指唤醒所有线程
                else:
                    print('{}:{}库存充足，商品数量大于10，休息一会，现在总商品数量是{}'.format('生产者', threading.currentThread().getName(), product))
                    condition.release()
                    time.sleep(2)

class consumer(threading.Thread):
    def run(self) -> None:
        global condition, product
        while True:
            if condition.acquire():
                if product >= 1:
                    product -= 1
                    print('{}:{}我消费了一件商品，现在商品数量是{}'.format('消费者',threading.currentThread().getName(),product))
                    condition.notify()
                else:
                    print('{}:{}->库存不足，现在商品数量是{}'.format('消费者',threading.currentThread().getName(),product))
                    condition.wait()
                condition.release()
                time.sleep(2)

if __name__ == '__main__':
    for i in range(2):
        t = producer()
        t.start()

if __name__ == '__main__':
    for s in range(5):
        f = consumer()
        f.start()














