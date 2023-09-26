# 8. Write a program to find the sum of all even numbers from 1 to N.

number = int(input('Enter a number: '))

sumOfEvenNumber = 0
i = 2
while i <= number:
    sumOfEvenNumber += i
    i += 2
print(sumOfEvenNumber)


