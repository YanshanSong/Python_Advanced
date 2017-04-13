# -*-coding:utf-8-*-
import yaml
from pprint import pprint
with open('31-test.yaml', 'r') as f:
	data = yaml.load(f)
pprint(data)

s = 'I have an apple'
print(yaml.dump(s))   
# I have an apple
#　...
lists = ['zhangsan', 'lisi', 'wangwu', 'zhaoliu']
print(yaml.dump(lists))  # [zhangsan, lisi, wangwu, zhaoliu]

class Person(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age

p1 = Person('zhangsan', 19)
p2 = Person('lisi', 20)
p3 = Person('wangwu', 21)
persons = [p1, p2, p3]

print(yaml.dump(persons))
'''
- !!python/object:__main__.Person {age: 19, name: zhangsan}
- !!python/object:__main__.Person {age: 20, name: lisi}
- !!python/object:__main__.Person {age: 21, name: wangwu}
'''