# 13. Write a program to print the sum of digits in a number.

number = int(input('Number: '))

sumOfDigits = 0

while number > 0:
    lastDigit = number % 10
    sumOfDigits += lastDigit
    number //= 10

print(sumOfDigits)
