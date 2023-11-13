# 1. Write a program in Python to find the minimum mark in a list without using built-in function.

marks = [10, 20, 30, 40, 50, 60]

minMark = marks[0]
for mark in marks:
    if mark < minMark:
        minMark = mark
print('Minimum mark is: ', minMark)