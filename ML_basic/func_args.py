'''
函数的参数
- 必须参数、默认参数、组合参数
- 函数作为参数
- 对象作为参数
- **kargs 关键字参数
- *args 可变参数
'''

def function(a,b,*arg,**kwarg):  #关键性参数必须在最后面
    print(a,b)
    print(arg)
    print(type(arg))
    print(kwarg)
    print(type(kwarg))

# function(1,2,3,4,5,name='hi',age=18)

#命名关键字参数，*后买呢必须要写名字
#命名关键字参数是必须参数，如果不需要他是默认参数，可以给一个默认值
def func2(a,b,*,c,d):
    print(a)
    print(b)
    print(c)
    print(d)

# func2(1,2,c=1,d=5)
# func2(1,6,d=1,c=5)

def func3(a,b,c):
    print(a)
    print(b)
    print(c)

#tuple\list传入到函数中用*
s = (1,2,3)
func3(*s)
s1 = [4,5,6]
func3(*s1)

kw = {'a':1,'b':2,'c':3}
func3(*kw)
kw = func3(**kw)  #一般我们传入字典类型，用** key要和函数参数名字保持一致
