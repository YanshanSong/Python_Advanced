# 你想构造一个字典，它是另外一个字典的子集。
# 最简单的方式是使用字典推导:
prices = { 'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75 } 
# Make a dictionary of all prices over 2000
p1 = {key:value for key, value in prices.items() if value > 200}
print(p1)
# {'AAPL': 612.78, 'IBM': 205.55}
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'} 
p2 = {key: value for key, value in prices.items() if key in tech_names}
print(p2)
# {'IBM': 205.55, 'HPQ': 37.2, 'AAPL': 612.78}

# 大多数情况下字典推导能做到的，通过创建一个元组序列然后把它传给 dict() 函数也能实现。比如：
p3 = dict((key, value) for key, value in prices.items() if value > 200)
# 但是，字典推导表意更加清晰，并且实际上也会运行的更快些 (在这个例子中， 实际测试几乎比 dcit() 函数方式快整整一倍)。

# 有时候完成同一件是会有多种方式。比如，第二个例子程序也可以像这样重写
# Make a dictionary of tech stocks
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p4 = {key:prices[key] for key in prices.keys() & tech_names }
# {'AAPL': 612.78, 'HPQ': 37.2, 'IBM': 205.55}
print(p4)