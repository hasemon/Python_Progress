aString = input('Enter a string: ')

mid = (len(aString) - 1) // 2

firstPart = aString[:mid+1]
lastPart = aString[mid+1:]

print(lastPart + firstPart)


