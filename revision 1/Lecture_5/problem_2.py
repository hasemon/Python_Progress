# 2. Write a program to find the avg marks of students in a class using list.
list1 = [20,30, 40, 50, 60]

sumOfList = 0

for item in list1:
    sumOfList += item

average = sumOfList / len(list1)

print('Average is :', average)