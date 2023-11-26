aString = input('Enter a string: ')

length = (len(aString) - 1) // 2

firstPart = aString[:length+1]
lastPart = aString[length+1:]

output = lastPart + firstPart
print(output)
