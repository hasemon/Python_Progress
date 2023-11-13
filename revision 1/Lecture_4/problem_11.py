# 11. Write a program to display the multiplication table of a given integer.

givenNumber = int(input('Enter a number: '))

i = 0
multiplier = 1
while i < 10:
    i += 1
    multiplier = givenNumber * i
    print(givenNumber, '*', i, '=', multiplier)