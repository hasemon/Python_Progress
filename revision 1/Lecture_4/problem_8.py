# 8. Write a program to find the sum of all even numbers from 1 to N

N = int(input('Number: '))

sumOfEven = 0
i = 2
while i <= N:
    sumOfEven += i
    i += 2

print('sum Of Even is', sumOfEven)