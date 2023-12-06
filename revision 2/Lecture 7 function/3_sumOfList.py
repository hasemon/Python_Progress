# 3. Write a Python function to sum all the numbers in a list.
alist = [10, 20, 30, 40, 50, 60]


def sumOfList(lst):
    sumOfNum = 0
    for num in lst:
        sumOfNum += num
    return sumOfNum


result = sumOfList(alist)
print('The sum of list is: ', result)