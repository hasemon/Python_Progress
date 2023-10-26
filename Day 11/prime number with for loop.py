firstRange = int(input('Enter the first number of the range: '))
lastRange = int(input('Enter the last number of the range: '))

primeList = []
nonPrimeList = []

for number in range(firstRange, lastRange + 1):
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    if len(divisors) == 2:
        primeList.append(number)
    else:
        nonPrimeList.append(number)

print('Prime Number list: ', primeList)
print('Non Prime Number list: ', nonPrimeList)