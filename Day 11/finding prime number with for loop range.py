primeNumber = []
nonPrimeNumber = [1]

for number in range(2, 101):
    i = 2
    prime = True
    while i <= (number // 2):
        if number % i == 0:
            prime = False
            break
        i += 1
    if prime:
        primeNumber.append(number)
    else:
        nonPrimeNumber.append(number)

print('Prime number', primeNumber)
print('NonPrime number', nonPrimeNumber)
