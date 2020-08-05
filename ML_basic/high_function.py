# lambda表达式  又叫匿名函数
#格式： lambda 参数列表：表达式


#map函数
map_demo=map(lambda x:x + x, [1,2,3,4])
# print(map_demo)
# print(list(map_demo))
# print(list(map(str,[1,2,3,4])))

#reduce函数
from functools import reduce
r = reduce(lambda x,y: x + y , [1,2,3,4,5])
# print(r)  #reduce原理：(1+2)+3)+4)+5)

#filter函数
print(list(filter(lambda x:x and x.strip(),['1','2','',None])))
print(list(lambda x:x and x.strip(),['3','7','',None]))