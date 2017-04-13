'''
Python中有join()和os.path.join()两个函数，具体作用如下:
join():连接字符串数组。将字符串、元组、列表中的元素以指定的字符(分隔符)连接生成一个新的字符串
os.path.join():将多个路径组合后返回
'''
# 1.join()函数
# 语法:'sep'.join(seq)
# 参数说明
# sep:分隔符，可以为空
# seq:要连接的元素序列、字符串、元组、字典
# 上面的语法即：以sep作为分隔符，将seq所有的元素合并成一个新的字符串
# 返回值:返回一个以分隔符sep连接各个元素后生成的字符串

# 2.os.path.join()函数
# 语法os.path.join(path1[,path2[,...]])
# 返回值:将多个路径组合后返回

# 对序列进行操作(分别使用''与':'作为分隔符)
seq1 = ['hello','good','boy','doiido']
print(' '.join(seq1))      # hello good boy doiido
print(','.join(seq1))      # hello,good,boy,doiido

# 对字符串进行操作
seq2 = "hello good boy doiido"
print(':'.join(seq2))      # h:e:l:l:o: :g:o:o:d: :b:o:y: :d:o:i:i:d:o

# 对元组进行操作
seq3 = ('hello','good','boy','doiido')
print(':'.join(seq3))      # hello:good:boy:doiido

# 对字典进行操作
seq4 = {'hello':1,'good':2,'boy':3,'doiido':4}
print(':'.join(seq4))       # boy:good:hello:doiido

# 合并目录
import os
str1 = os.path.join('/hello/', 'good/boy/', 'doiido')
print(str1)                 # /hello/good/boy/doiido