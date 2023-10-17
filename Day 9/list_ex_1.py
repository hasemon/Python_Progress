marks = [3, 4, 6, 8, 6]

maxMarks = max(marks)
print('Maximum marks is: ', maxMarks)

minMarks = min(marks)
print('Minimum marks is: ', minMarks)

marks.sort()
print('Ascending order is: ', marks)
marks.sort(reverse=True)
print('Descending order is: ', marks)

marks.remove(minMarks)
print('Removing minMarks is: ', marks)

marks2 = [4, 6, 7, 8, 9, 4, 3]

allMarks = marks + marks2
print('All marks is: ', allMarks)

# mark 1 extending
marks.extend(marks2)
print('Extended list is: ', marks)
