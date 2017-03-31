# 你的程序已经出现了一大堆无法直视的硬编码切片下标，然后你想清理下代码。
# 假定你有一段代码要从一个记录字符串中几个固定位置提取出特定的数据字段(比如文件或类似格式)
record = '....................100 .......513.25 ..........' 
cost = int(record[20:23]) * float(record[31:37])
print(cost)

# 第二种写法
SHARES = slice(20, 23)
PRICE = slice(31, 37)
cost = int(record[SHARES]) * float(record[PRICE])
print(cost)
# 第二种版本中，你避免了大量无法理解的硬编码下标，是的你的代码
# 更加清晰可读。

# 内置的slice()函数创建了一个切片对象，可以被用在任何切片允许使用的地方。
# 比如:
items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
print(items[2:4]) # [2, 3]
print(items[a])   # [2, 3]

items[a] = [10, 11]
print(items)  # [0, 1, 10, 11, 4, 5, 6]

del items[a]
print(items)  # [0, 1, 4, 5, 6]

# 假如你有一个切片对象s, 你可以分别调用它的s.start, s.stop, s.step属性来获取更多的信息。
s = slice(5, 50, 2)
print(s.start, s.stop, s.step) # 5, 50, 2


