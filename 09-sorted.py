# 函数原型:
# sorter(iterable, cmp=None, key=None, reverse=False)

# iterable:可迭代对象(iterable)

#----------------------------------------
# cmp:用于比较的函数，这个函数接受两个参数(iterable)
# 如果第一个参数小于第二个参数，返回一个负数
# 如果第一个参数等于第二个参数，返回零
# 如果第一个参数大于第二个参数，返回一个正数
# -----python3中cmp已经删除

# key:指定一个接受一个参数的函数
# 这个函数用于从每个元素中提取一个用于比较的关键字。

# reverse:排序规则，正排还是倒排。默认reverse=False即正排

# 返回值：是一个经过排序的列表

# 一般来说，cmp和key可以使用lambda表达式

# sort与sorted()的不同在于，sort是在原位重新排列列表
# 而sorted()是产生一个新的列表。

# example:
# 现有两个列表，每个列表中都有一个字典([{}, {}])要求将两个这样的列表
# 合并后按照时间排序，两个列表中的时间为了能够通过json输出
# 已经由时间格式转换为字符串格式。字段名为sort_time
# 现在将他们按照倒序排列
# sorted(data, key=lambda dict : dict['sort_time'], reverse=True)

# example:
# 元组
student_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'B', 10),
]
print(sorted(student_tuples, key=lambda student: student[2]))  
# sort by age

# 对象
class Student:
        def __init__(self, name, grade, age):
                self.name = name
                self.grade = grade
                self.age = age
        def __repr__(self):
                return repr((self.name, self.grade, self.age))

student_objects = [
        Student('john', 'A', 15),
        Student('jane', 'B', 12),
        Student('dave', 'B', 10),
]

# 字典
student_dicts = [
        {"name":'john', "grade":'A', "age": 15},
        {"name":'jane', "grade":'B', "age": 12},
        {"name":'dave', "grade":'B', "age": 10},
]

print(sorted(student_objects, key=lambda student:student.name))

# operator模块函数
# 上面key参数的使用非常广泛，因此python提供一些方便的函数
# 使得访问方法更加容易和快速
from operator import itemgetter, attrgetter
# itemgetter用于序列、字典(item-->迭代)
print("序列:", sorted(student_tuples, key=itemgetter(2)))
print("字典:", sorted(student_dicts, key=itemgetter("age")))
# attrgetter用于对象(attr属性-->对象)
print("对象:", sorted(student_objects, key=attrgetter('age')))

# operator模块还允许多级的排序，例如，先以grade，然后再以age来排序
print("多级排序:", sorted(student_tuples,key=itemgetter(1, 2)))
print("对象多级排序:", sorted(student_objects, key=attrgetter('grade', 'age')))

# key函数不仅可以访问需要排序元素的内部数据，还可以访问外部的资源，例如，如果学生的成绩是存储在dictionary中的，则可以使用此dictionary来对学生名字的list排序，如下：
students = ['dave', 'john', 'jane']
newgrades = {'john': 'F', 'jane':'A', 'dave': 'C'}
print(sorted(students, key=newgrades.__getitem__))