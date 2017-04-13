# 格式化字符串函数str.format()
# 通过{}和:来代替%

# 通过位置，数字代表format中元祖索引
print('{0}, {1}'.format('kzc', 18))
# kzc, 18
print('{1}, {0}'.format('kzc', 18))
# 18, kzc

# 通过关键字参数
print('{name}, {age}'.format(age=18, name='kzx'))
# kzx, 18

# 通过对象属性
class Person:
	def __init__(self, name, age):
		self.name, self.age = name, age
	def __str__(self):
		return 'This guy is {self.name}, is {self.age} old'.format(self=self)

print(Person('kzx', 18))  # This guy is kzx, is 18 old

# 通过下标
p = ['kzx', 18]
print('{0[0]},{0[1]}'.format(p))  # kzx, 18

# 格式限定符
# 它有着丰富的"格式限定符"(语法是{}带:号), 比如:
# ^ < > 分别是居中、左对齐、右对齐，后面带宽度，默认左对齐
# :号带填充的字符，只能是一个字符，不指定的话默认是用空格填充
print('{:>8}'.format('189'))    # 占8位，右对齐，用空格填充空白
print('{:0>8}'.format('189'))   # 占8位，右对齐，用0填充空白
print('{:a>8}'.format('189'))   # 占8位，右对齐，用a填充空白

# 精度与类型f
# 精度常跟类型f一起使用
print('{:.2f}'.format(321.33345))    # 保留保留2位小数
print('{:>8.2f}'.format(321.33345))  # 占8位，右对齐，保留保留2位小数

# 其他类型
# 主要就是进制，b、d、o、x分别是二进制、十进制、八进制、十六进制
print('{:b}'.format(17))  # 10001
print('{:d}'.format(17))  # 17
print('{:o}'.format(17))  # 21
print('{:x}'.format(17))  # 11

# ，表示千位分割符
print('{:,}'.format(1234567890))
# 1,234,567,890


