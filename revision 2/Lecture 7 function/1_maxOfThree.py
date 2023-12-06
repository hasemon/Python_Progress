# 1. Write a Python function to find the max of three numbers.

def maxOfThree(first, second, third):
    if first > second and first > third:
        maxNum = first
    elif second > first and second > third:
        maxNum = second
    else:
        maxNum = third
    return maxNum


num1 = int(input('Enter 1st Number: '))
num2 = int(input('Enter 2nd Number: '))
num3 = int(input('Enter 3rd Number: '))

print(maxOfThree(num1, num2, num3))
