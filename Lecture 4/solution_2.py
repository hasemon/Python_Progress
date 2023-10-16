# 2. Write a program to find the avg marks of students in a class using list.

marksList = [80, 70, 60, 50, 40, 30]

marksSum = 0
for mark in marksList:
    marksSum += mark

print('Total marks: ', marksSum)
average = marksSum / len(marksList)
print('Average mark: ', average)

