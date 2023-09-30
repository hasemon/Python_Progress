# 16. Write a program to determine whether a given number is prime or not.

number = int(input('Check if the number is prime or not: '))

primeNumber = 0
i = 1
while i <= number:
    if number % i == 0:
        primeNumber += 1
    i += 1
if primeNumber == 2:
    print(f'{number} is prime number.')
else:
    print(f'{number} is prime not a number.')

# write a program how many prime number is there below given number.


