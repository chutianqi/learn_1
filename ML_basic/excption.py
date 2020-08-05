'''
异常：运行时发生了错误，代码出现了一个错误
BaseException 所有异常的基类
object 父类
异常的处理方式
try:
   代码块
except 异常名字
else:
   代码块
'''
try:
    file=open('aaa','r')
except FileNotFoundError as e:
    print(e)
except ReferenceError as b:
    print(b)
except Exception:
    print('文件有异常')
else:
    print('没有异常')
finally:
    print('这个无论如何都会被打印')
#手动抛出异常
try:
    raise Exception('手动跑出异常')
except:
    print('捕获了一个异常')

#自定义异常MySlefDefine
class MySlefDefine(BaseException):
    pass
raise MySlefDefine('抛出一个自定义的异常')




'''
异常的处理原则
能处理的异常直接捕捉，不能处理的抛出去
'''