# 你想在字符串那种搜索和匹配指定的文本模式
# 对于简单的字面模式，直接使用str.replace()方法即可
text = 'yeah, but no, but yeah, but no, but yeah' 
text_replace = text.replace('yeah', 'tep')
print(text_replace) # tep, but no, but tep, but no, but tep

# 对于复杂的模式，使用re模块的sub()方法即可
# 假设你想将形 式为 11/27/2012的日期字符串改成 2012-11-27 
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.' 
import re
text_sub = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
print(text_sub) # Today is 2012-11-27. PyCon starts 2013-3-13.

# sub函数第一个参数是被匹配的模式，第二个参数是替换模式。
# 反斜杠\3指向前面模式的捕获分组
# 如果你打算用相同的模式做多次替换，考虑先编译它来提升性能。
# 比如:
import re
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepat.sub(r'\3-\1-\2', text))
# Today is 2012-11-27. PyCon starts 2013-3-13.
# 对于更加复杂的替换，可以传递一个替换回调函数来代替
# 比如:
from calendar import month_abbr
def change_date(m):
	month_name = month_abbr[int(m.group(1))]
	return '{} {} {}'.format(m.group(2), month_name, m.group(3))

print(datepat.sub(change_date, text))
# Today is 27 Nov 2012. PyCon starts 13 Mar 2013.
'''
一个替换回调函数的参数是一个 match 对象，也就是 match() 或者 find() 返回的对象。使用 group() 方法来提取特定的匹配部分。回调函数最后返回替换字符串。
'''