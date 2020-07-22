'''
reg正则表达式是一种用来操作字符串的逻辑
. 换行符以外的任意字符
\w 匹配数字、字母、下划线、汉字
\s 匹配任意空白符
\d 匹配任意数字0-9
tab键匹配四个空格
^ shift+6 匹配字符串的开始
$ shift+4 匹配字符串的结束
'''

#反义代码
"""
\W
\S
\D
"""

# import re
# s='rtyuijh__还不错 g456$%*'
# print(re.findall('\w',s))
# print(re.findall('\d',s))
# print(re.findall('\s',s))
# print(re.findall('^r',s))  #限定后面表达式必须是整个字符串开头

#限定符
'''
* 代表他前面的正则表达式重复0次或者多次
+ 代表他前面的正则表达式重复1次或者多次
？ 代表他前面的正则表达式重复0次或1次
{n}重复n次
{n,}重复n次或多次
{n,m}重复n次-m次
'''
# import re
# s1='我的qq号是：9646728956'
# reg='\d{5,12}'
# print(re.findall(reg,s1))

#分组匹配
import re
s='我的qq号是：9646728956,我的邮编是：40201'
reg='(\d{10}).*(\d{5})'
print(re.findall(reg,s))
print(re.search(reg,s))
print(re.search(reg,s).group(0))
print(re.search(reg,s).group(1))
print(re.search(reg,s) .group(2))

phonereg=