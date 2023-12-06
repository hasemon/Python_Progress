numName = input("Enter a string: ")
if len(numName) < 3:
    print('String is smaller than 3')
else:
    newName = numName[:3] + numName[-3:]
    print(newName)