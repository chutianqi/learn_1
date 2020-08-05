#第一种方法
def quick_sort(sort_list,start_index,end_index):
    print(sort_list)
    #如果角标左侧小于右侧则开始排序，否则退出
    if start_index<end_index:
        basic,i,j=sort_list[start_index],start_index,end_index
        while i < j : #确保左侧index一定比右小
            while i<j and basic <= sort_list[j]:#基准值比j小，那么不做任何运算
                #角标左移
                j -= 1
            while i<j and basic >=sort_list[i]: #基准值比i大，那么不做任何运算
                #角标右移
                i += 1
            sort_list[i],sort_list[j]=sort_list[j],sort_list[i]
        sort_list[i],sort_list[start_index]=sort_list[start_index],sort_list[i]
        #左边递归
        quick_sort(sort_list,start_index,i-1)
        #右边递归
        quick_sort(sort_list,i+1,end_index)

l = [10,23,52,12,15,7,18]
# r=quick_sort(l,0,len(l)-1)

#第二种方法
def quick_sort2(quick_list):
    if quick_list == []:
        return []
    else:
        first=quick_list[0]
        less=quick_sort2([l for l in quick_list[1:] if l < first])
        more=quick_sort2([m for m in quick_list[1:] if m >= first])
        return less+[first]+more

s=quick_sort2(l)
print(s)








