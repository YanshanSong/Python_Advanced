# Python中，如果函数体是一个单独的return expression语句
# 开发者可以选择使用特殊的lambda表达式替换该函数
# lambda parameters : expression

# lambda表达式相当于函数体为单个return语句的普通函数的匿名函数
# 注意:默认返回 所以不用再加return返回值

f = lambda x, y, z : x + y + z
print(f(1, 2, 3))  # 6

g = lambda x, y=2, z=3 : x + y + z
print(g(1))  # 6
print(g(1, y=4, z=5)) # 10

# lambda常用高效操作列表
# map()
# 将序列中的元素依次通过处理函数处理后返回一个新的列表
li = [1, 2, 3, 4, 5]
# 序列中的每个元素加1
print(list(map(lambda x : x+1, li)))  # [2, 3, 4, 5]

def f1(x):
	return x+1
print(list(map(f1, li)))

# filter()
# 将序列中的元素依次通过布尔函数过滤后返回一个新的列表
print(list(filter(lambda x : x % 2 == 0, li))) # [2, 4]

# reduce
# 注意 python3 调用reduce
from functools import reduce
# 将序列中的元素通过一个二元函数进行累积，返回一个结果
# reduce(function, sequence[,initial]) 
# function参数是一个二元函数
# reduce依次从sequence中取一个元素，和上一次调用function的结果
# 做参数再次返回function
# 第一次调用function时，如果提供initial参数
# 会以sequence中的第一个元素和initial作为参数调用function
# 否则会以sequence中的前两个元素做参数调用function
print(reduce(lambda x, y : x * y,li)) # 1*2*3*4*5 = 120
print(reduce(lambda x, y : x*y, li, 100)) # 100*1*2*3*4*5 = 120000

print(reduce(lambda x, y : x + y,li)) # 1+2+3+4+5 = 15
print(reduce(lambda x, y : x + y,li, 100)) # 115

