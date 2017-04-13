# 你想排序类型相同的对象，但是他们不支持原生的比较操作。
'''
内置的sorted() 函数有一个关键字参数 key ，可以传入一个callable 对象给它callable 对象对每个传入的对象返回一个值，这个值会被 sorted 用来排序这些 对象。
比如:
'''
class User:
	def __init__(self, user_id):
		self.user_id = user_id
	def __repr__(self):
		return 'Use({})'.format(self.user_id)

def sort_norcompare():
	users = [User(23), User(3), User(99)]
	print(users)
	print(sorted(users, key=lambda u:u.user_id))

sort_norcompare()

from operator import attrgetter
users = [User(23), User(3), User(99)]
print(sorted(users, key=attrgetter('user_id')))
'''
选择使用 lambda 函数或者是 attrgetter() 可能取决于个人喜好。但是， attrgetter() 函数通常会运行的快点，并且还能同时允许多个字段进行比较。
'''