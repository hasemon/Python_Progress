# 13. Write a program to print the sum of digits in a number.

number = int(input('Enter a number to find its sum of its digits: '))

sumOfDigits = 0
while number > 0:
    digit = number % 10
    sumOfDigits += digit
    number //= 10

print(f'The sum of digits is : {sumOfDigits}')
