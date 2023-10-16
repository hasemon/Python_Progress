# 8. Remove the smallest mark from the list.

marks = [33, 34, 35, 50, 60, 70]

min_mark = marks[0]

for mark in marks:
    if mark < min_mark:
        min_mark = mark

marks.remove(min_mark)
print(f'New list after removing smallest: {marks}')
