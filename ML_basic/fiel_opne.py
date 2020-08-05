
def read_fiel():
    f=open('excption.py','r',encoding='UTF-8')
    # print(f.read())  #一次性读取所有内容，弊端：文件很大时，会占用很大内存
    print(read(10)) #指定大小的读取

    while True:    #内存占用资源较小
        z=read(10)
        print(z)
        if z=='':
            break

    f.close() #文件有打开有关闭


# read_fiel()

#with open 帮助我们自动关闭文件的输入输出流
def read_file2(filename:str):  #filename:str 解释说明
    with open(filename,'r',encoding='UTF-8') as f:
        lines=f.readlines()
        print(lines)

# read_file2(('excption.py'))

def read_file3(filename):
    print(filename)
    print(read_file3.__annotations__)
    read_file3.__annotations__['info']='动态注释'
    print(read_file3.__annotations__)

# read_file3('aaa')

def write_file():
    with open('1.txt','w',encoding='UTF-8') as f:
        for i in range(100):
            f.write(str(i))
            f.flush()#将内存（缓存区）的数据存储到磁盘上


