# 1. Write a program in Python to find the maximum mark in a list without using built-in function.

marks = [80, 70, 75, 76, 80, 65]

max_mark = marks[0]
for mark in marks:
    if mark > max_mark:
        max_mark = mark
print('Max mark is', max_mark)

