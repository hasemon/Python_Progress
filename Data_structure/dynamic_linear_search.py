arrayLength = int(input("Enter array length: "))
myArray = []

print('Enter array elements: ')
for i in range(arrayLength):
    arrayElement = int(input())
    myArray.append(arrayElement)

print('Array: ', myArray)
search = int(input('Enter a number to search: '))


found = False
location = 0
indexes = []
for i in range(len(myArray)):
    indexes.append(i)
    if myArray[i] == search:
        found = True
        break
    else:
        location += 1


print('Index: ', indexes)
print('Array: ', myArray)

if found:
    print('The number', search, 'is in the array at location: ', location)
else:
    print('The number', search, 'does not exist in the array')


