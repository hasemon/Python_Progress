# 4. Write a program to find the sum of first N natural numbers.

number = int(input('Enter a number: '))

sumOfNumber = 0
i = 1

while i <= number:
    sumOfNumber += i
    i += 1
print(f'The sum of the first N natural numbers is: {sumOfNumber}')


