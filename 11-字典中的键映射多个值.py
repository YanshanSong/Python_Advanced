# 怎样实现一个键对应多个值的字典(也叫multidict)
# 一个字典就是一个键对应一个单值的映射。如果你想要一个键映射多个值，那么就需要将多个值放到另外的容易中，比如列表或者集合里面。
# 比如
a = {
	'a' : [1, 2, 3],
	'b' : [4, 5]
}
b = {
	'a' : [1, 2, 3],
	'b' : [4, 5]
}

# 选择使用列表还是集合取决于你的实际需求。
# 如果你想保持元素的插入顺序就应该使用列表
# 如果想去掉重复元素就使用集合(并且不关心元素的顺序问题)

# 可以很方便的使用collections模块中的defaultdict来构造这样的字典
# defaultdict的一个特征是它会自动初始化每个key刚开始对应的值
# 所有只需要关注添加元素操作。

from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

print(d.get('a')) # [1]

for key, value in d.items():
	print(key + ":" ,value)

# 需要注意的是， defaultdict会自动为将要访问的键 (就算目前字典中并不存在这样的键) 创建映射实体。

# 在普通字典上也可采用setdefault方法创建一个多值字典
# dict.get(key[,v=None])      
# 找到key返回value,找不到key返回v

# dict.setdefault(key[,value=None])
# 先执行dict.get(key[,value=None],若key不在dict中执行dict[key]=value

e = {}
# print(e.setdefault('a',[]))  # []
e.setdefault('a', []).append(1) 
e.setdefault('a', []).append(2) 
e.setdefault('b', []).append(4)

# 但是很多程序员觉得 setdefault() 用起来有点别扭。因为每次调用都得创建一个 新的初始值的实例 (例子程序中的空列表 [])。

# comparison
pairs = [('sam',1),('sam',2),('sam',3),('Tom',1),('Tom',2),('Amy',2)]
f = {}  # regular
for key, value in pairs:
	if key not in f:
		f[key] = []
	f[key].append(value)
# print(d['c'])  # Keyerror  # 换用d.get('c')即可
print(f)

g = {}
for key, value in pairs:
	g.setdefault(key,[]).append(value)
print(g)

h = defaultdict(list) 
for key, value in pairs: 
	h[key].append(value)
print(h['c'])    # []
print(h)