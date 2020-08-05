'''
装饰器（语法糖、注解）
'''
def func_1(x):
    return x*2

def func_2(y):
    return y*3

def func_3(x,y,i,j):
    return x(i)+y(j)

# r=func_3(func_1,func_2,2,3)
# print(r)

import time
def runtime_noargs(function_name):
    def wrapper():
        start_time=time.time()
        print('函数运行前')
        function_name()
        print('函数运行后')
        end_time=time.time()
        print(end_time-start_time)
    return wrapper()


@runtime_noargs
def function_demo1():
    time.sleep(1)
    print('demo1函数运行')

# function_demo1()
def arg_is_str(function_name):
    def wrapper(a):
        t=type(a)
        if not isinstance(t(),str):
            print('参数错误')
        else:
            function_name(a)
    return wrapper


@arg_is_str #装饰器先跑
def function_demo2(args):
    print(args)

# function_demo2(1)

#多个参数
def many_args(function_name):
    def wrapper(*a):
        print(*a)
    return wrapper

@many_args
def function_demo3(*args):
    print(*args)

# function_demo3(1,2,3)

 #多个key参数
def dict_args(function_name):
    def a(**dict):
        print(dict)
    return a


@dict_args
def function_demo4(**kwags):
    print(kwags)
    pass

# function_demo4(name='hillo',age=21,address='北京')

def combo_args(function_name):
    def w(*a,**ka):
        print(*a,ka)
    return w


@combo_args
def function_demo5(*args,**kargs):
    pass

function_demo5(1,2,name='hillo',age=21,address='北京')

#终极模拟器
def max_runtime(timeout):
    def wrapper(func_name):
        def kk(*args,**kargs):
            start_time = time.time()
            i=func_name()
            end_time = time.time()
            use_time = end_time-start_time
            if use_time > timeout:
                print('函数运行超时')
                raise RuntimeError('函数运行超时')
            return i#这里是函数返回值
        return kk
    return wrapper


@max_runtime(timeout=3)
def function_demo6(*args,**kargs):
    time.sleep(2)
    print('demo6运行')
    return 1
r = function_demo6()
print(r)