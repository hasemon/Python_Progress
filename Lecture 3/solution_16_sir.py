N = int(input('Enter a number to Check Prime number: '))
i = 2
prime = True

while i < N:
    mod = N % i
    if mod == 0:
        prime = False
        break
    i += 1
if prime == True:
    print(f'{N} is a prime number.')
else:
    print(f'{N} is not a prime number.')