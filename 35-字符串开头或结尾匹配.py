# 你需要通过指定的文本模式去检查字符串的开头或者结尾
# 比如文件名后缀，URL Scheme等等

# 解决方案
# 检查字符串开头或结尾的一个简单方法是使用str.startwith()
# 或者是str.endwith()犯法。比如:
filename = 'spam.txt'
print(filename.endswith('.txt'))    # True
print(filename.startswith('file:')) # False

url = 'http://www.python.org'
print(url.startswith('http:'))      # True

# 如果你想检查多种匹配可能，只需要将所有的匹配项放入到一个元组中去
# 然后传给startswith()或者endswith()方法:
import os
filenames = os.listdir('.')
print(filenames)   # 读出当前文件夹中所有文件名
print(any(name.endswith('.py') for name in filenames))  # True

#**********************另外一个例子***************************
from urllib.request import urlopen
def read_data(name):
	if name.startswith(('http:', 'https:', 'ftp:')):
		return urlopen(name).read()
	else:
		with open(name) as f:
			return f.read()
#*************************************************************
choices = ['http:', 'ftp:']
url = 'http://www.python.org'
print(url.startswith(tuple(choices)))   # True

# discussion
# startswith()和endswith()方法提供了一个非常方便的方式去做字符串开头
# 和结尾的检查。类似的操作也可以使用切片来实现，但是代码看起来没有那么优雅
filename = 'spam.txt'
print(filename[-4:] == '.txt')   # True
# 还可以通过使用正则表达式去时间 
import re
url = 'http://www.python.org'
print(re.match('http:|https:|ftp:', url)) 
# <_sre.SRE_Match object; span=(0, 5), match='http:'>
