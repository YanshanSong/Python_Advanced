# 2017-03-21
# 如果一个可迭代对象的元素个数超过接受变量的个数时，会抛出ValueError
# Python的星号表达式可以用来解决这个问题。
s
'''
例如:
在学期末，你想统计下家庭作业的英俊成绩，但是排除第一个和最后一个分数。
设总计有24个分数
'''
def drop_first_last(grades):
	first, *middle, last = grades;
	return avg(middle)

# 另外一种情况，假设你现在有一些用户的记录列表
# 每条记录包含一个名字、邮件，接着就是不确定数量的电话号码
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212',)
name, email, *phone_numbers = record
print(name, email, phone_numbers)
# Dave dave@example.com ['773-555-1212', '847-555-1212']
# 值得注意的是，解压出的phone_numbers变量永远都是列表类型
# 不管解压的电话号码数量是多少(包括0个)

# 星号表达式也能用在列表的开始部分。
# 比如，你有一个公司前8个月销售数据的序列
# 但你想看下最近一个月数据和前面7个月的平均值的对比
sales_record =  [10, 8, 7, 1, 9, 5, 10, 3] 
*trailing_qtrs, current_qtr = sales_record
trailing_avg = sum(trailing_qtrs) / len(trailing_qtrs)
print(trailing_qtrs, current_qtr, trailing_avg)

# discussion
# ①星号表达式在迭代元素为可变长元组的序列时很有用的。
record = [
	('foo', 1, 2),
	('bar', 'hello'),
	('foo', 3, 4),
]

def do_foo(x, y):
	print('foo', x, y)

def do_bar(s):
	print('bar', s)

for tag, *args in record:
	if tag == 'foo':
		do_foo(*args)
	else:
		do_bar(*args)

for tag, *args in record:
	print(*args)

# ②型号解压语法在字符串操作的时候也会很有用，比如字符串的分割
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
# uname, *fields, *homedir, sh = line.split(':')
# 注意一个同级表达式中不能同时存在两个星号表达式
uname, *fields, homedir, sh = line.split(':')
print(uname, *fields, *homedir, sh) 

# ③有时候，你想解压一些元素后丢弃它们，就不能简单地使用*
# 可以使用一个普通的废弃名称，比如_或者ign
record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(name, year)

# ④在很多函数式语言中，星号解压语法跟列表处理有很多
# 相似之处。比如，如果你有一个列表，你可以很容易的将它分割成
# 前后两部分