N = int(input('Enter the value of N: '))

sumOfN = 0
i = 1
while i < N:
    sumOfN += i
    i += 3
print(f'The sum of N is {sumOfN}')