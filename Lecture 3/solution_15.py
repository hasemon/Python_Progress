# 15. Write a program to check whether a given number is a 'Perfect' number or not.
# Perfect number, a positive integer that is equal to the sum of its proper divisors.
# The smallest perfect number is 6, which is the sum of 1, 2, and 3.

number = int(input("Enter a number: "))

sumOfNumber = 0
divisor = 1

while divisor < number:
    if number % divisor == 0:
        sumOfNumber += divisor
    divisor += 1

if sumOfNumber == number:
    print(f'{number} is perfect number.')
else:
    print(f'{number} is not a perfect number.')
