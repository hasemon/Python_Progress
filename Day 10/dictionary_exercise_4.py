n = int(input('Enter a value: '))

numbers = {}

for i in range(1, n):
    value = i ** 2
    numbers.update({i: value})

print(numbers)
