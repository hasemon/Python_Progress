# 4. Write a program to find the sum of first N natural numbers.

number = int(input('Enter a number: '))

factOfNumber = 0
i = 1

while i <= number:
    factOfNumber += i
    i += 1
print(f'The sum of the first N natural numbers is: {factOfNumber}')


