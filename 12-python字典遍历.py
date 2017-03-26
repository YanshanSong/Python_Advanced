# python遍历字典dict的几种方法
dict={"a":"apple","b":"banana","o":"orange"} 

# No1:
print("No1:---------------------------------")
for key in dict:
	print(key + ":" + dict[key])

# No2:
print("No2:---------------------------------")
for key, value in dict.items():
	print(key + ":" + value)

# No3:  # Python3删除了iteritems()
# print("No3:---------------------------------")
# for key, value in dict.iteritems():
# 	print(key + ":" + value)

# No4   # Python3删除了iterkeys(), itervalues()
# print("No3:---------------------------------")
# for k,v in zip(dict.iterkeys(),dict.itervalues()): 
#         print("dict[%s]=" % k,v)