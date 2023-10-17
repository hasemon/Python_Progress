listC = ['ABC', 'XYZ', 'PER']
listN = [1, 2, 3, 4, 5]

# append in the list
listC.append(listN)
print(listC)

listN.insert(0, 7)
print(listN)

# insert in the last
lastIndex = len(listN)
listN.insert(lastIndex, 11)
print(listN)

# using extends
listC.extend(listN)
print(listC)
