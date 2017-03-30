# python的set是一个无序不重复元素集，基本功能包括关系测试和消除重复元素。集合对象还支持并、交、差、对称差等。

# sets支持 x in set, len(set), for x in set。
# 作为无序的集合，sets不仅记录元素位置或插入点。
# 因此，sets不支持indexing, slicing, 或其他类序列(sequence-like)的操作、

x = set('jihite')
print(x)  
# 把字符串转化为set, 去重了
# {'i', 't', 'e', 'j', 'h'}

y = set(['d', 'i', 'm', 'i', 't', 'e'])
print(y)
# {'m', 'i', 'd', 'e', 't'}
# 把序列转化set

# 注意由于是无序的，所以每次print的顺序都不一样
print(x & y)  # 交
# {'i', 't', 'e'}

print(x | y)  # 并
# {'j', 'h', 'd', 't', 'e', 'm', 'i'}

print(x - y)  # 差
# {'h', 'j'} 

print(y - x)  # 差
# {'m', 'd'}

print(x ^ y)  # 对称差
# {'h', 'j', 'm', 'd'}


