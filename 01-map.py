# 2017-03-19
# Python map用法

# ①对可迭代对象'iterable'中的每一个元素应用'function'方法
# 将结果作为list返回

def add100(x):
	return x+100

hh = [11,22,33]
hh_1 = list(map(add100,hh))
print(hh_1)
# [11, 22, 33]

# ②如果给出了额外的可迭代参数，则对每个可迭代参数中的元素'并行'应用'function'

def abc(a,b,c):
	return a*10000 + b*100 + c

list1 = [11, 22, 33]
list2 = [44, 55, 66]
list3 = [77, 88, 99]

List1 = list(map(abc, list1, list2, list3))
print(List1)
# [114477, 225588, 336699]
