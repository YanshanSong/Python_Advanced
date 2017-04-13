# 你想匹配或者搜索特定模式的文本
# 如果你想匹配的是字面字符串，那么你通常只需要调用基本字符串就行
# 比如str.find(), str.endswith(), str.startswith()或者类似的方法
text = 'yeah, but no, but yeah, but no, but yeah'
# Exact match
print(text == 'yeah')           # false
# Match at start or end
print(text.startswith('yeah'))  # True
print(text.endswith('no'))      # False

# Search for the location of the first orrurrence
print(text.find('no'))          # 10

'''
对于复杂的匹配需要使用正则表达式和re模块。为了解释正则表达式的基本原理， 假设你想匹配数字格式的日期字符串比如 11/27/2012 ，你可以这样做： 
'''
text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

import re
# Simple matching: \d+ means match one or more digits
if re.match(r'\d+/\d+/\d+', text1):
	print('yes')
else:
	print('no')

if re.match(r'\d+/\d+/\d+', text2):
	print('yes')
else:
	print('no')

# 如果你想使用同一个模式去做多次匹配，你应该先将模式字符串
# 预编译为对象。比如:
datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
	print('yes')
else:
	print('no')   # yes

if datepat.match(text2):
	print('yes')
else:
	print('no')   # no

# match()总是从字符串开始去匹配，如果你想查找字符串任意的模式出现位置
# 使用findall()方法去替代
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(datepat.findall(text))  # ['11/27/2012', '3/13/2013']

# 在定义正则式的时候，通常会利用括号去捕获分组
# 比如:
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('11/27/2012')
print(m)
print(m.group(0), m.group(1), m.group(2), m.group(3))
# 11/27/2012 11 27 2012
print(m.groups())  # ('11', '27', '2012')
month, day, year = m.groups()
print(month, day, year) # 11 27 2012

print(datepat.findall(text)) # [('11', '27', '2012'), ('3', '13', '2013')]
for month, day, year in datepat.findall(text):
	print('{}-{}-{}'.format(year, day, year))
# 2012-27-2012
# 2013-13-2013

# discussion
# 如果你想要精确匹配，确保你的正则表达式以$结尾，就像这样:
datepat = re.compile(r'(\d+)/(\d+)/(\d+)$') 
print(datepat.match('11/27/2012abcdef'))
print(datepat.match('11/27/2012'))