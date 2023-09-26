# 1. Write a program to print your name N times.

yourName = input('Please enter your name: ')
numOfPrint = int(input('Number of prints: '))

i = 1
while i <= numOfPrint:
    print(i, yourName)
    i += 1
