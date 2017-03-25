# 怎样从一个集合中获得最大或者最小的N个元素列表
# heapq模块有两个函数有两个函数:nlargest()和nsmallest()可以完美解决这个问题
import heapq
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))  # [42, 37, 23]
print(heapq.nsmallest(3, nums)) # [-4, 1, 2]

# 两个函数都能接受一个关键字参数，用于更复杂的数据结构中
portfolio = [ {'name': 'IBM', 'shares': 100, 'price': 91.1}, 
			  {'name': 'AAPL', 'shares': 50, 'price': 543.22}, 
			  {'name': 'FB', 'shares': 200, 'price': 21.09}, 
			  {'name': 'HPQ', 'shares': 35, 'price': 31.75}, 
			  {'name': 'YHOO', 'shares': 45, 'price': 16.35}, 
			  {'name': 'ACME', 'shares': 75, 'price': 115.65} ]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])

print(cheap)
print(expensive)

# 如果你想在一个集合中查找最小祸最大的N个元素，并且N小于集合元素数量，
# 那么这些函数提供了很好的性能。因为在底层实现里面，首先会将集合数据进行排序后放入一个列表中

numbers = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heapq.heapify(numbers)
print(numbers)

# 堆数据结构最重要的特征是heapq[0]永远是最小的元素。
# 并且剩余的元素可以很容易的通过调用heapq.heappop()方法得到
# 该方法会先将第一个元素弹出来，然后用下一个最小的元素来取代被弹出元素
# (这种操作时间复杂度仅仅是O(logN), N是堆大小)。
# 比如，如果想要查找最小的3个元素，可以连续调用heapq.heappop()三次