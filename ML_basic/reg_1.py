'''
正则表达式的高级应用
贪婪与懒惰  贪婪与非贪婪
非贪婪：尽可能少的匹配
非贪婪操作符 ?
这个非贪婪操作符可以使用在 * + ?后面
* 重复0次或者多次  *? 0次重复
+ 重复1次或者多次  +? 一次重复
？ 重复0次或1次   ??  0次重复
'''
import re
s='greedyaiiii'
# reg='greedyai*'
# reg='greedyai*?'
# reg='greedyai+?'
reg='greedyai??'
print(re.findall(reg,s))

'''
分之条件匹配
操作符 |  （或者的意思）
管道符号 将第一个运行后的结果反馈给第二个一次进行
'''
s='我的电话号码： 010-89764528 0431-89765491 0432-8965423'
reg='0\d{2}-\d{8}|0\d{3}-\d{8}|0\d{3}-\d{7}'
print(re.findall(reg,s))
s1='010-89764528'
s2='0431-89765491'
s3='0432-8965423'
reg='^0\d{2,3}-\d{7,8}'
print(re.findall(reg,s2))

#零宽断言
'''
(?=reg 匹配reg前边的位置)
(?<=reg 匹配reg后边的位置)
(?！=reg 匹配后边跟的不是reg的位置)
(?<！=reg 匹配前边跟的不是reg的位置)
'''
s='hellogreedyailoove'
# reg='l{2}o(?=greedyai)'
# print(re.findall(reg,s))
reg='(?<=greedyai)[a-z]*'
print(re.findall(reg,s))