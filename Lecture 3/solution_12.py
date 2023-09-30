# 12. Write a program to print the reverse of a number.

number = int(input('Enter a number: '))
newNumber = 0

s1 = ''
if number % 10 == 0:
    s1 = '0'
orginalNumber = number
while number != 0:
    digit = number % 10
    newNumber = newNumber * 10 + digit
    number //= 10
s2 = str(newNumber)


reversed_number = int(s1 + s2)
print(f'The reversed number is: {reversed_number}')
if reversed_number == orginalNumber:
    print('This number  is a palindrome.')
else:
    print('This number is not a palindrome.')
