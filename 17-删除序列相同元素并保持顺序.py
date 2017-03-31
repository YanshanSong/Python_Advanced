# 怎样在一个序列上面保持元素顺序的同时消除重复的值？
# 如果序列上的值都是hashable类型，那么可以很简单的利用集合或者
# 生成器来解决这个问题。

# 不改变顺序
# def dedupe(items):
# 	seen = set()
# 	for item in items:
# 		if item not in seen:
# 			yield item
# 			seen.add(item)

a = [1, 5, 2, 1, 9, 1, 5, 10]
# print(list(dedupe(a)))  # [1, 5, 2, 9, 10]

# 这个方法仅仅在序列中元素为hashable的时候才管用。
# 如果你想要消除元素不可哈希(比如dict类型)的序列中重复元素的话。
# 需要将上述代码稍微改变一下。
def dedupe(items, key=None):
	seen = set()
	for item in items:
		# 比上面的depude更完善
		# 可将非hashable元素换换为hashable
		val = item if key is None else key(item)
		# print(val)
		if val not in seen:
			yield item     # 注意yield的对象
			seen.add(val)

# 这里的key指定了一个函数，将序列元素转换成hashable类型。
# 下面是它的用法实例。
b = [
 	{'x':1, 'y':2},
 	{'x':1, 'y':3},
 	{'x':1, 'y':2},
 	{'x':2, 'y':4}
 ]

print(list(dedupe(a)))
print(list(dedupe(b, key=lambda d: (d['x'], d['y']))))
# [{'y': 2, 'x': 1}, {'y': 3, 'x': 1}, {'y': 4, 'x': 2}]

# 如果你想给予单个字段，属性或者谋改革更大的数据结构来小数重复元素，第二种方案同样可以胜任。
print(list(dedupe(b, key=lambda d: d['x'])))
# [{'y': 2, 'x': 1}, {'y': 4, 'x': 2}]

# discussion
# 如果仅仅就是想消除重复元素，通常可以简单的构造一个集合。
# 比如:
a = [1, 5, 2, 1, 9, 1, 5, 10]
print(set(a))
# 然而这种方法不能维护元素的顺序，生成的结果中的元素位置被打乱。

# 本节中，我们使用了生成器函数让我们的函数更加通用，不仅仅局限于
# 列表处理。比如，如果你想读取一个文件，消除重复行，可以很容易像
# 这样做:
# with open(somefile, 'r') as f:
# 	for line in dedupe(f):

