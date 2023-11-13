# 5. Write a program to calculate the factorial of a given number.

givenNumber = int(input('Give a number: '))

factorial = 1
i = 1
while i <= givenNumber:
    factorial *= i
    i += 1

print('Factorial of ', givenNumber, 'is', factorial)

