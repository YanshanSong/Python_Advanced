# any()
# doc:return True if any element of the iterable is true. If the iterable is empty, return False 只要迭代器中有一个元素为真就为真
a = [True, False]
print(any(a))

b = ['good', 'bad', 'good', 'good']
print(any(i == 'bad' for i in b)) # True

# all()
# doc:return True if all elements of the iterable are true(of if the iterable is empty)
print(all(a))
print(all('good' == i for i in b)) # False
