# Binary search algorithm to find 80 from the following list:

alist = [20, 30, 40, 50, 60, 70, 80, 90]

search = int(input("Enter a number to search: "))
low = 0
high = len(alist) - 1


def binarySearch(lst, lw, hgh, src):
    if hgh >= lw:
        mid = (lw + hgh) // 2
        if lst[mid] == src:
            return mid
        elif src > lst[mid]:
            return binarySearch(lst, mid + 1, hgh, src)
        else:
            return binarySearch(lst, lw, mid - 1, src)

    else:
        return - 1


output = binarySearch(alist, low, high, search)

if output != -1:
    print(search, 'is found in index of the list', output)
else:
    print(search, 'is not found in the list')