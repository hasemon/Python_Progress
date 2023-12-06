alist = [20, 30, 40, 50, 60, 70, 80, 90]

low = 0
high = len(alist) - 1
search = 75


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


output = binarySearch(alist, low, high, search)

if output != -1:
    print(search, "is found at index", output)
else:
    print(search, 'is not found')
