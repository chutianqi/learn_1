'''
名词：类、对象、实例、实例化
类：类代表了具有相同特征的一类事物（人）
对象和实例：具体的一个事物或者是人（张三、李四）
实例化：将类变成对象的一个过程，new一个对象
'''

'''
python命名规范
类：驼峰命名法  PersonStudio
其他：包含模块、方法名、函数名、变量名，全部采用小蛇儿命名法：persong_studio
'''
#函数、方法
def func1(): #函数，特点是在模块中声明的
    pass
class persion:
    def func1(self):#方法，特点是在类中声明
        pass
    #类变量
    name='女娲'
    age=10000
    #类私有变量
    __private_args='class_private'
    def __init__(self,name,age):
        print(name)
        print(age)
        # print(self.name)
        # print(self.age)

b=persion('fuxi',235)

