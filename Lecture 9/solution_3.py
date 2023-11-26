# 3. Repeat the process to find 75 from the list.

alist = [20, 30, 40, 50, 60, 70, 80, 90]

lwIndex = 0
hgIndex = len(alist) - 1
search = 75


def binarySearch(theList, low, high, searched):
    midIndex = (low + high) // 2
    if high >= low:
        if theList[midIndex] == searched:
            return midIndex
        elif theList[midIndex] > searched:
            return binarySearch(theList, low, midIndex - 1, searched)
        else:
            return binarySearch(theList, midIndex + 1, high, searched)
    else:
        return -1


output = binarySearch(alist, lwIndex, hgIndex, search)

if output == -1:
    print(search, 'is not found.')
else:
    print(search, 'is found at location', output)
