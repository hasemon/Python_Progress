# index method
listA = [123, 'ABC', 'XYZ', 'PER']

indexABC = listA.index('PER')
print(indexABC)

# count method

listB = [123, 'ABC', 'XYZ', 'PER', 123, 'ABC', 'XYZ', 'PER']
print(listB.count(123))

# reverse method

listC = [123, 'ABC', 'XYZ', 'PER']
listC.reverse()
print(listC)

# sort method

listD = [100, 200, 300, 400, 500]
listD.sort()
print(listD)
listD.sort(reverse=True)
print(listD)
