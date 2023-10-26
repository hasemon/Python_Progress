marksList = [80, 90, 70, 60, 50, 85, 95, 75, 65, 55]

maxMark = max(marksList)
minMark = min(marksList)
print(f'Largest mark is: {maxMark} and smallest mark is: {minMark}')

average = sum(marksList) // len(marksList)
print('Average is:', average)

marksList.sort()
print('Marks is ascending order:', marksList)
marksList.sort(reverse=True)
print('Marks is descending order:', marksList)

marksList.remove(minMark)
print('Deleted smallest mark:', marksList)

middleIndex = len(marksList) // 2

marksList.insert(middleIndex, average)
print('Average in the middle:', marksList)

marksList2 = [50, 60, 70, 80, 90]

marksList.extend(marksList2)
print(marksList)




