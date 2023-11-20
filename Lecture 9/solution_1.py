# 1. Show the simulation of the Binary search algorithm to find 80 from the following list:
# list = [20, 30, 40, 50, 60, 70, 80, 90]

aList = [20, 30, 40, 50, 60, 70, 80, 90]
sorted_aList = sorted(aList)

searchItem = int(input('Enter search item: '))
lowest = 0
highest = len(sorted_aList) - 1


def binary_search(lst, lw, hg, slt):
    if hg >= lw:
        mid = (hg + lw) // 2
        if sorted_aList[mid] == searchItem:
            return mid
        elif sorted_aList[mid] > searchItem:
            return binary_search(lst, lw, mid - 1, slt)
        else:
            return binary_search(lst, mid + 1, hg, slt)
    else:
        return -1


output = binary_search(sorted_aList, lowest, highest, searchItem)

if output != -1:
    print('Element is present at index: ', str(output))
else:
    print('Element is not present in list')
