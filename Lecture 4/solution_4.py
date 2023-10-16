# 4. Find the largest and smallest mark in the list.

marks = [33, 34, 35, 50, 60, 70]

max_mark = marks[0]
min_mark = marks[0]

for mark in marks:
    if mark > max_mark:
        max_mark = mark
    else:
        min_mark = mark

print('largest mark is:', max_mark)
print('smallest mark is:', min_mark)
