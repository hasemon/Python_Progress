# 2. Repeat the process to find 30 from the list.

alist = [20, 30, 40, 50, 60, 70, 80, 90]

lIndex = 0
hIndex = len(alist) - 1
search = 30


def binarySearch(theList, lowIndex, highIndex, searched):
    midIndex = (lowIndex + highIndex) // 2
    if highIndex >= lowIndex:
        if searched == theList[midIndex]:
            return midIndex
        elif searched > theList[midIndex]:
            return binarySearch(theList, midIndex + 1, highIndex, searched)
        else:
            return binarySearch(theList, lowIndex, midIndex - 1, searched)
    else:
        return -1


output = binarySearch(alist, lIndex, hIndex, search)

if output != -1:
    print(search, 'is found at index ', output)
else:
    print(search, 'is not found.')
