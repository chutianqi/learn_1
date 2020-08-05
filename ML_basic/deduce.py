#列表推倒式 x for x in a
y=[x+1 for x in [1,2,3,4]]
print(y)
print(list(x + 1 for x in [1,2,3,4] if x > 2))

def qsort(my_list):
    if len(my_list) <= 1:return my_list
    return qsort([l_list for l_list in my_list[1:] if l_list < my_list[0]]) + \
           my_list[0:1]+\
           qsort([r_list for r_list in my_list[1:] if r_list >= my_list[0]])

a=[25,3,6,83,92,100,22]
print(qsort(a))
c=a[0:1]  #左闭右开
print(c)

def quick_sort(my_list):
    if len(my_list) <= 1:
        return my_list
    else :
        first=my_list[0]
        left_list = quick_sort([l for l in my_list[1:] if l < first])
        right_list = quick_sort([r for r in my_list[1:] if r >= first])
        return left_list+[first]+right_list


#集合推倒式
y={x+1 for x in [1,2,3,4]}
print(y)
print(type(y))

#字典推倒式
d={x:y  for x, y in {'a':1, 'b':2}.items()}
print(d)
print(type(d))
dd={x for x, y in {'a':1, 'b':2}.items()}
print(dd)
print(type(dd))

