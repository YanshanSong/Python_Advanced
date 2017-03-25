# 2017-03-22
# Python  yield与实现
'''
yield的功能让类似于return, 但是不同之处在于它返回的是生成器。
生成器是由一个或多个yield表达式构成的函数，每一个生成器
都是一个迭代器Iterator(但是迭代器不一定是生成器)。
如果一个函数包含yield关键字，这个函数就是一个生成器。
生成器并不会一次性返回所有结果，而是每次遇到yield关键字后返回相应结果，并保留函数当前的运行状态，等待一下次代用。
由于生成器是一个迭代器，那么它就应该支持next方法来获取下一个值。
'''
# 通过'yield'来创建生成器
def func():
	for i in range(3):
		yield i

f = func() # 返回一个生成器
print(f)   # 此时生成器还没有运行
# <generator object func at 0×0000015933F0B888>

print(f.__next__())  #  python3中，next() --> ___next__()
# 当i = 0时，遇到yield关键字，直接返回

print(f.__next__())
# 继续上一次执行的位置，进入下一层循环

print(f.__next__())

# print(f.__next__())
# 当执行完最后一次循环后，结束yield语句，生成StopIteration异常

# 除了next函数，生成器还支持send函数。该函数可以像生成器传递参数。
def func():
	n = 0;
	while 1:
		n = yield n # 可以通过send函数向n赋值

f = func()
print(f.__next__())

print(f.send(1))   # n赋值1

print(f.send(2))   # n赋值2

# 应用
# 最经典的例子，生成无限序列
# 常规的解决方法是，生成一个满足要求的很大的列表，这个列表
# 需要保存在内存中，很明显内存限制了这个问题。

# def get_primes(start):
#     for element in magical_infinite_range(start):
#         if is_prime(element):
#             return element

# 如果使用生成器就不需要返回整个列表，每次都只是返回一个数据，避免了内存的限制问题。
# def get_primes(number):
#     while True:
#         if is_prime(number):
#             yield number
#         number += 1


# 补充
def simple_generator_function():
	yield 1
	yield 2 
	yield 3

# 调用它的两种方法
# 每一个生成器(generator)都是迭代器(iterator)
# 可迭代对象，可直接作用于for循环
for value in simple_generator_function():
	print(value)

# 可以通过调用iter()函数或者__next__()方法来迭代
f = simple_generator_function()
print(f.__next__())  # 1
print(f.__next__())  # 2
print(f.__next__())  # 3
