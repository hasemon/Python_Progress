listOfPrices = [100, 200, 300, 400]

sumOfListOfPrices = sum(listOfPrices)

average = sumOfListOfPrices / len(listOfPrices)
print('Average is', average)

midPosition = len(listOfPrices) // 2
listOfPrices.insert(midPosition, average)
print('Average in the middle', listOfPrices)
listOfPrices.sort()
print('Sorted in ascending order', listOfPrices)
