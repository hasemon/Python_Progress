# 11. Write a program to display the multiplication table of a given integer.

number = int(input('Enter a number: '))

i = 1
multiplier = 1
while i < 10:
    i += 1
    multiplier = number * i
    print(f'{number} * {i} = {multiplier}')


