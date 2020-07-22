#增加
list1=[1,2,3,'a','b']
list1.append('c')
print(list1)
print(type(list1))

#更新
list1[1]='l1'
print(list1)

#删除
del list1[0]
print(list1)

#嵌套列表
list_1=[1,2,3]

#冒泡循环
a=[3,24,1,52,30,26]
for i in range(len(a)-1):
    for j in range(len(a)-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]

print(a)

a=set('abcd')
b=set('wert')
print(a|b) #并集
print(a&b) #交集
print(a)
#如果需要不分开
myset1=set(('jack','andy'))
print(myset1)
#集合的crud(增删更改）
# 增加
myset1.add('ni')
print(myset1)
#删除
myset1.remove('andy')
print(myset1 )
#清楚所有元素
myset1.clear()
print(myset1)

'''
字典是一种可变容器模型，他可以存储任意类型的对象
set_param={'1','2','3'}
d={k1:v1,k2:v2}
'''
d={1:'wangming',2:'zhangsan'}
print(d)
keys=d.keys()
print(keys)
for i in keys:
    print(i)
    print(d[i])
#更新方法：无则添加有则更新
d[3]='nancy'
print(d)
d[3]='will'
print(d)
#pop删除 del也可以删除
r=d.pop(3)
print(r)
print(d)
del d[2]
print(d)

'''
list;[]
dic/set:{}
tuple:() 一旦生成，不可改变
'''
#tuple需要（） 一个元素 （1，）
t=(1,)
print(t)


