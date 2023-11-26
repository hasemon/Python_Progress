aString = input('Enter a string: ')

reverseAString = ''

for letter in aString:
    reverseAString = letter + reverseAString


print(reverseAString)
if reverseAString == aString:
    print('This is a palindrome')
else:
    print('This is not a palindrome')
