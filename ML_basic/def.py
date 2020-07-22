'''
行参：形式参数，是一种意义上的参数。定义时并不占用具体内存地址
实参：实际参数
'''
def func_1(p1, p2):
    print(p1)
    print(p2)


func_1(1, 2)

#默认参数
def func_2(name,age=23):
    print(name)
    print(age)

func_2(2)

#输出时需要确认参数时完整的，默认参数输出


#递归：直接或间接调用函数本身，必须明确递归结束条件(return)
#无限递归
# def func_3(x):
#     print(x)
#     func_3(x+1)
#
# func_3(1)

#先压后弹，对内存消耗极大
# def f(x):
#     if x==1:
#         return 1
#     return x+f(x-1)
# r=f(5)
# print(r)

#函数的返回可以是函数
#第一轮c函数没有被调用，返回的是inner_func,第二轮z调用了内部函数
def func_l(x):
    if x==2:
        def inner_func(y):
            print('函数1被调用')
            return y*y
    if x==3:
        def inner_func(y):
            print('函数2被调用')
            return y*y*y
    return inner_func #括号要去掉，return到内部函数名称
c=func_l(3)
z=c(5)
print(z)

#循环的中断
i=1
#continue:结束本次循环，开始下一次循环
while True:
    i=i+1
    if i==10:
        print('此时i的值是10')
        continue
    if i==15:
        break

