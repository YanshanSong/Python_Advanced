# 怎样找出一个序列中出现次数最多的元素呢？

# collections.Counter 类就是专门为这类问题而设计的，它甚至有一个有用的 most common() 方法直接给了你答案。 

words = [ 'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes', 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into', 'my', 'eyes', "you're", 'under' ]

from collections import Counter
word_counts = Counter(words)
# 出现平率最高的3个单词
top_three = word_counts.most_common(3)
print(top_three)
# [('eyes', 8), ('the', 5), ('look', 4)]

# 作为输出，Counter对象可以接受任意的hashable序列对象。
# 在底层实现上，一个Counter对象就是一个字典，将元素映射到它出现的次数上。
print(word_counts['not'])
print(word_counts['eyes'])

# 如果想手动增加计数，可以简单的用加法
# 例如:
morewords = ['why','are','you','not','looking','in','my','eyes'] 
for word in morewords:
	word_counts[word] += 1
print(word_counts['eyes'])

# 或者可以使用update()方法(推荐):
word_counts.update(morewords)
# print(word_counts)

# Counter实例一个鲜有人知的特性是它们可以很容易的跟数学运算操作相结合。比如：

a = Counter(words)
b = Counter(morewords)
print(a)
print(b)
c = a + b
print(c)

# Subtract counts
d = a - b
print(d)
# 毫无疑问 Counter 对象在几乎所有需要制表或者计数数据的场合是非常有用的工具。


