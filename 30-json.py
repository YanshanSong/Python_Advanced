import json
data = {
	'name' : 'ACME',
	'shares' : 100,
	'price' : 542.23
}
json_str = json.dumps(data)
print(json_str)  # {"price": 542.23, "shares": 100, "name": "ACME"}
data = json.loads(json_str)
print(data)      # {'shares': 100, 'price': 542.23, 'name': 'ACME'}

# 例如你要处理的是文件而不是字符串，你可以使用json.dump()和json.load()
# 来编码和解码JSON数据。例如:
# writing JSON data
with open('data.json', 'w') as f:
	json.dump(data, f)
# writing data back
with open('data.json', 'r') as f:
	data = json.load(f)

# JSON编码支持的数据基本类型为None，bool，int，float和str
# 以及包含这些数据类型的lists, tuples, dictionaries。
# 对于dictionaries, keys需要是字符串类型(字典中任何非字符串类型的key在编码时会先转换为字符串)
# 为了遵循JSON规范，你应该只编码Python的lists和dictionaries。而且，在web应用程序中，顶层
# 对象被编码为一个字典是一个标准做法。

# JSON编码的格式对于Python语法而已几乎是完全一样的。
# 除了一些小的差异之外，比如:True-->true，False-->fales，而None-->null
# 下面是一个例子，演示了编码后的字符串效果。
print(json.dumps(False))  # false
d = {
	'a' : True,
	'b' : 'Hello',
	'c' : None
}
print(json.dumps(d))      # {"c": null, "b": "Hello", "a": true}
'''
如果你试着去检查 JSON 解码后的数据，你通常很难通过简单的打印来确定它的 结构，特别是当数据的嵌套结构层次很深或者包含大量的字段时。为了解决这个问题， 可以考虑使用 pprint 模块的 pprint() 函数来代替普通的 print() 函数。它会按照key的字母顺序并以一种更加美观的方式输出。
下面是一个演示如何漂亮地打印输出Twitter上搜索结果的例子:
'''
import requests
import json
from pprint import pprint
r = requests.get(url='http://api.douban.com/v2/movie/in_theaters?count=3')
resp = json.loads(r.text)
pprint(resp)
'''
一般来讲，JSON 解码会根据提供的数据创建 dicts 或 lists。如果你想要创建其他 类型的对象，可以给 json.loads() 传递 object pairs hook 或 object hook 参数。例如， 下面是演示如何解码 JSON 数据并在一个 OrderedDict 中保留其顺序的例子：
'''
s = '{"name": "ACME", "shares": 50, "price": 490.1}' 
from collections import OrderedDict
data = json.loads(s, object_pairs_hook=OrderedDict)
print(data)
# OrderedDict([('name', 'ACME'), ('shares', 50), ('price', 490.1)])

# 下面是如何将一个JSON字典转换为一个Python对象例子
class JSONObject:
	def __init__(self, d):
		self.__dict__ = d
data = json.loads(s, object_hook=JSONObject)
print(data.name)  # ACME
# 在编码JSON的时候，还有以下选项很有用。如果你想获得漂亮的格式化字符串后输出
# 可以使用json.dumps()的indent参数。它会使得输出和pprint()函数效果类似。
data = json.loads(s)
print(json.dumps(data, indent=4))
'''
{
    "price": 490.1,
    "name": "ACME",
    "shares": 50
}
'''









