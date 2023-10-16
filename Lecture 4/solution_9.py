# 9. Insert the average mark at the mid-position of the list.

marksList = [80, 70, 60, 50, 40, 30]

marksSum = 0
for mark in marksList:
    marksSum += mark

average = marksSum / len(marksList)
middleIndex = len(marksList)//2

marksList.insert(middleIndex, int(average))
print('Average mark at the mid-position list: ', marksList)
