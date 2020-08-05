#时间复杂度
a=0
b=0
c=1
n=100
while a<n:
    while b<n:
        c=(c+1)**2  #计算表达式 时间复杂度是o(n^2)
        b=b+1
    a=a+1

a=0
b=0
n=100
while a<n:
    while b<n:
        c=(c+1)**2  #时间复杂度的标识 o(nlogn)
        b=b+2
    a=a+1
