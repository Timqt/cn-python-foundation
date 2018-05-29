"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"There are <count> different telephone numbers in the records."
"""
tel_set = set()

for tel in calls:
	tel_set.add(tel[0])
	tel_set.add(tel[1])

for tel in texts:
	tel_set.add(tel[0])
	tel_set.add(tel[1])

print("There are {} different telephone numbers in the records.".format(len(tel_set)))