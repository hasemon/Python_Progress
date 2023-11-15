# 9. Write a program in Python to calculate the sum of numbers from 1 to n using recursion.

def sumOfNumbers(n):
    if n > 0:
        return n + sumOfNumbers(n - 1)
    else:
        return 0


print(sumOfNumbers(10))
