aString = input('Enter a string: ')

mid = len(aString) // 2
output = aString[mid:] + aString[:mid]

print(output)
if output == aString:
    print('This is a symmetric')
else:
    print('Not a symmetric')