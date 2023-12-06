# 9. Write a program in Python to calculate the sum of numbers from 1 to n using recursion.

def sumOfNumber(num):
    if num > 0:
        return num + sumOfNumber(num - 1)
    else:
        return 0


number = int(input('Enter a number: '))
print('Sum of Number: ', sumOfNumber(number))
