'''
闭包：外部函数返回值是内部函数的引用
'''

def outer(a):
    b=10
    def inner():
        print(a+b)
        #外部函数的返回值是内部函数的额引用
    return inner

c=outer((5))
c()