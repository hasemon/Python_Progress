def listEvenSum(lst):
    sumOfEven = 0
    for i in lst:
        if i % 2 == 0:
            sumOfEven += i
    return sumOfEven


list1 = [1, 2, 3, 4, 5, 6, 7, 8]
output = listEvenSum(list1)
print('Sum of Evens: ', output)
