#yield 生成器
def yield_demo2():
    for x in range(3):
        yield x
        print('生成器最后一行代码')
    print('生成器外层')

a=yield_demo2()
print(a) #生成器

# for i in a:
#     print(a)

print(a.__next__)
print(a.__next__)
print(a.__next__)

def yield_demo2():
    a=1
    b=2
    c=3
    for i in range(3):
        yield a  #存储的指针，省内存
        print('生成a之后')
        yield b
        print('生成b之后')
        yield c
        print('生成c之后')

x=yield_demo2()
for g in x:
    print(g)