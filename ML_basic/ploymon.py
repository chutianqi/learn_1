'''
多态：一个类有多种类型
'''
from abc import ABCMeta, abstractmethod


class animal:
    def run(self):
        raise AttributeError('子类必须实现这个方法')
class person(animal):
    def run(self):
        print('人跑')
class pig(animal):
    def run(self):
        print('猪跑')
class dog(animal):
    def run(self):
        print('狗跑')
# person=person()
# person.run()
# pig=pig()
# pig.run()
# dog=dog()
# dog.run()
#
# def func(obj):
#     obj.run()
#
# person=person()
# pig=pig()
# dog=dog()
# #这里就相当于我们往usb接口上插入了一些设备
# func(person)
# func(pig)
# func(dog)

#我是电脑的厂商，比如联想、苹果、戴尔
class computer(metaclass=ABCMeta):
    @abstractmethod
    def usb_insert(self):
        pass
class thinkpad(computer):
    def usb_insert(self):
        pass
    def usb_run(self,sub_computer):
        sub_computer.usb_insert()

#这是鼠标生成商
class mouse(computer):
    def usb_insert(self):
        print('插入了鼠标')

#这是键盘生成商
class keyboard(computer):
    def usb_insert(self):
        print('插入了键盘')

#我买了一个电脑
computer=thinkpad()

#我买了一个鼠标
m=mouse()
#插入电脑上
computer.usb_run(m)
#我买了一个键盘
k=keyboard()
#把键盘插入电脑上
computer.usb_run(k)
