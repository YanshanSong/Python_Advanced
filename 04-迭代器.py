'''
什么是迭代？
①可以直接作用于for循环的对象称为可迭代对象(Iterable)
②可以被next()函数调用或者调用__next__()方法并不断返回下一个值的对象称为迭代器(Iterator)
③所有的Iterable均可以通过内置函数iter()或者电泳__iter__()来转变为Iterator
'''
L = [1, 2, 3]
# print(next(L))
I = iter(L)
# I = L.__iter__()
# print(next(I))
print(I.__next__())
print(I.__next__())
print(I.__next__())

# 上面例子中，列表L可以被for进行循环但是不能被内置函数next()用来
# 查找下一个值，所以L是Iterable
# L通过iter进行包装后成为I，I可以被next()函数或者调用__next__()
# 方法用来查找
# 下一个值，所以L是Iterator

'''
# 补充说明
1.内置函数iter()仅仅是调用了对象的__iter__()方法，
所以list对象内部一定存在__iter__()
2.内置函数next()仅仅是调用了对象的__next__()，所以list对象
内部一定不存在方法__next__()，但是Iterator中一定存在这个方法。
3.for循环内部事实上就是先调用iter()把iterable变成Iterator在进行迭代循环的。
'''
from collections import Iterable, Iterator
print(isinstance(L, Iterable))
print(isinstance(L, Iterator))
print(isinstance(I, Iterable))
print(isinstance(I, Iterator))

# Iterator继承自Iterable
# Iterable包含__iter__()方法
# Iterator包含__iter__()方法，__next__()方法