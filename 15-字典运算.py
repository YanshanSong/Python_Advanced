# 怎样在数据字典中执行一些操作(比如求最小值、最小值、排序等等)
# 解决方案
prices = {
	'ACME':45.23,
	'AAPL':612.78,
	'IBM':205.55,
	'HPQ':37.20,
	'FB':10.75
}
# 每次执行程序时，字典都会随机排序
print(sorted(prices)) 
# ['AAPL', 'ACME', 'FB', 'HPQ', 'IBM']  # 仅仅作用于键

# 为了对字典值执行计算操作、通常需要使用zip()函数先将键和值反转过来。
# 比如，下面是查找最小和最大股票价格和股票值的代码：
print(prices.values())  
print(prices.keys()) 
# 键值同步性
print(list(zip(prices.values(), prices.keys()))) # zip并行生成元组
min_prices = min(zip(prices.values(), prices.keys()))
print(min_prices)   # (10.75, 'FB')
max_prices = max(zip(prices.values(), prices.keys()))
print(max_prices)   # (612.78, 'AAPL')

# 排序
prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)
# [(10.75, 'FB'), (37.2, 'HPQ'), (45.23, 'ACME'), (205.55, 'IBM'), (612.78, 'AAPL')]

# 执行这些操作的时候，需要注意的是zip()函数创建的是一个只能访问一次的
# 迭代器。(python2中返回包含元组的序列，python3返回zip对象的迭代器)

# 比如，下面的代码就会产生错误:
prices_and_values = zip(prices.values(), prices.keys())
print(min(prices_and_values))  # OK
# print(max(prices_and_values))  # ValueError: max() arg is an empty sequence

# 解决方法，将zip对象序列化
prices_and_values = list(zip(prices.values(), prices.keys()))
print(min(prices_and_values))   # OK 
print(max(prices_and_values))   # OK

#--------------discussion---------------
print('--------------discussion---------------')
# 如果在一个字典上执行普通的数学运算，你会发现它们仅仅作用于键
# 而不是值
print(max(prices)) # IBM
print(min(prices)) # AAPL

# 这个结果可能并不是想要的，因为你想要在字典的值集合上执行这些计算。
print(max(prices.values()))
print(min(prices.values()))


# 你可能还想要知道对应的键的信息
# 可以在min()和max()函数提供key()函数来获取最小值和最大值对应的键的信息
print(max(prices, key=lambda k: prices[k]))  # 'AAPL'
print(min(prices, key=lambda k: prices[k]))  # 'FB'

# 但是，如果还想要得到最小值，你又得执行一次查询操作
# min_value = prices[min(prices, key=lambda k: prices[k])] 

# 前面的zip()函数通过将字典"反转"为 (值，键) 元组序列来解决了上述问题


# 需要注意的是，在计算操作汇中使用到了(值，键)对。当多个实体拥有相同
# 的值的时候，键会决定返回结果。比如，在执行min()和max()操作的时候，
# 如果恰巧最小或最大值有重复的，那么拥有最小或最大键的实体会返回： 
prices = { 'AAA' : 45.23, 'ZZZ': 45.23 } 
print(min(zip(prices.values(), prices.keys()))) # (45.23, 'AAA')
print(max(zip(prices.values(), prices.keys()))) # (45.23, 'ZZZ')