# 9. Write a program to find the sum of all odd numbers from 1 to N.

number = int(input('Enter a number: '))

sumOfOddNumber = 0
i = 1
while i <= number:
    sumOfOddNumber += i
    i += 2
print(sumOfOddNumber)
