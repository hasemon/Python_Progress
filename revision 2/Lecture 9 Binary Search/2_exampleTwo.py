aList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

low = 0
high = len(aList) - 1
search = 3


def binarySearch(lst, lw, hgh, src):
    if hgh >= lw:
        mid = (lw + hgh) // 2
        if src == lst[mid]:
            return mid
        elif src > lst[mid]:
            return binarySearch(lst, mid + 1, hgh, src)
        else:
            return binarySearch(lst, lw, mid - 1, src)
    else:
        return -1


output = binarySearch(aList, low, high, search)

if output != -1:
    print(search, 'is found at index', output)
else:
    print(search, 'is not found in List')
