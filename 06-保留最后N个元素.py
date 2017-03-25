# 在迭代元素或者其他操作的时候，怎样只保留最后有限几个元素的历史记录呢?
# 使用deque(maxlen=N)构造函数会新建一个固定大小的队列。
# 当新的元素加入并且这个队列已满的时候，最老的元素会自动被移除掉。
from collections import deque
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)   # deque([1, 2, 3], maxlen=3)
q.append(4)
print(q)   # deque([2, 3, 4], maxlen=3)
q.append(5)
print(q)   # deque([3, 4, 5], maxlen=3)
# 尽管也可以手动在一个列表上实现这一操作(比如增加、删除等等)。
# 但是这里的队列方案会更加优雅并且运行得更快些。

# 更一般的，deque类可以被用在任何你只需要一个简单队列数据结构的场合。
# 如果不设置最大队列大小，那么就会得到一个无限大小队列，你可以在队列的
# 两端执行添加和弹出元素的操作。
q = deque()
q.append(1)
q.append(2)
q.append(3)
print(q)  # deque([1, 2, 3])
q.appendleft(4)
print(q)  # deque([4, 1, 2, 3])
print(q.pop()) # 3
print(q)  # deque([4, 1, 2])
print(q.popleft()) # 4
print(q)