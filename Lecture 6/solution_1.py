# 1. Write a program in Python to find the minimum mark in a list without using built-in function.

marks = [80, 70, 75, 76, 80, 65]

min_mark = marks[0]
for mark in marks:
    if mark < min_mark:
        min_mark = mark
print("The minimum mark is", min_mark)
