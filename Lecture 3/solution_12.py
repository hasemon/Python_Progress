# 12. Write a program to print the reverse of a number.

number = int(input('Enter a number: '))
newNumber = 0

s1 = ''
if number % 10 == 0:
    s1 = '0'
while number != 0:
    digit = number % 10
    newNumber = newNumber * 10 + digit
    number //= 10
s2 = str(newNumber)
print(s1 + s2)
