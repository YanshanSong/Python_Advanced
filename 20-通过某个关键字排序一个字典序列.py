# 通过使用 operator 模块的 itemgetter 函数，可以非常容易的排序这样的数据结构。假设你从数据库中检索出来网站会员信息列表，并且以下列的数据结构返回： 
rows = [ {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
		 {'fname': 'David', 'lname': 'Beazley', 'uid': 1002}, 
		 {'fname': 'John', 'lname': 'Cleese', 'uid': 1001}, 
		 {'fname': 'Big', 'lname': 'Jones', 'uid': 1004} ]

from operator import itemgetter
rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_fname, rows_by_uid)

# itemgetter() 函数也支持多个 keys，比如下面的代码 
rows_by_lfname = sorted(rows, key=itemgetter('lname','fname')) 
print(rows_by_lfname)

# itemgetter() 有时候也可以用lambda表达式代替
# 比如:
rows_by_fname = sorted(rows, key=lambda r: r['fname']) 
rows_by_lfname = sorted(rows, key=lambda r: (r['lname'],r['fname']))

#这种方案也不错。但是，使用 itemgetter() 方式会运行的稍微快点。因此，如果 你对性能要求比较高的话就使用 itemgetter() 方式。 

# 这节中展示的技术也同样适用于 min() 和 max() 等函数
print(min(rows, key=itemgetter('uid')))
# {'uid': 1001, 'lname': 'Cleese', 'fname': 'John'}
print(max(rows, key=itemgetter('uid')))
# {'lname': 'Jones', 'fname': 'Big', 'uid': 1004}
