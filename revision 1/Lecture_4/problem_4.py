# 4. Write a program to find the sum of first N natural numbers.

N = int(input('Number: '))

sumOfFirstN = 0
i = 0
while i <= N:
    sumOfFirstN += i
    i += 1

print('Sum of first N natural numbers: ', sumOfFirstN)
