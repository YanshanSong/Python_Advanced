import calendar
# 返回指定年的某月
def get_month(year, month):
    return calendar.month(year, month)

# 返回指定年的日历
def get_calendar(year):
	return calendar.calendar(year)

# 判断某一年是否为闰年，如果是，返回True，如果不是，返回False
def is_leap(year):
	return calendar.isleap(year)

# 返回某个月的weekend的第一天和这个月的所有天数
def get_month_range(year, month):
	return calendar.monthrange(year, month)

# 返回某个月以每一周为元素的序列
def get_month_calendar(year, month):
	return calendar.monthcalendar(year, month)

def main():
	year = 2013
	month = 8
	test_month = get_month(year, month)
	print(test_month)
	print('#'*50)
	print('{0}这一年是否为闰年?:{1}'.format(year, is_leap(year)))
	print(get_month_range(year, month))
	print(get_month_calendar(year, month))

if __name__ == '__main__':
	main()
'''
    August 2013
Mo Tu We Th Fr Sa Su
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30 31

##################################################
2013这一年是否为闰年?:False
(3, 31)
[[0, 0, 0, 1, 2, 3, 4], [5, 6, 7, 8, 9, 10, 11], [12, 13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24, 25], [26, 27, 28, 29, 30, 31, 0]]
'''