# define function
def binary_search(alist, low, high, search):
    mid = (low + high) // 2
    if high >= low:
        if search == alist[mid]:
            return mid
        elif search < alist[mid]:
            return binary_search(alist, low, mid - 1, search)
        else:
            return binary_search(alist, mid + 1, high, search)
    else:
        return - 1


oneList = [10, 14, 18, 22, 30, 35, 40]
lw = 0
h = len(oneList) - 1
mySearch = int(input('Enter number to search: '))
output = binary_search(oneList, lw, h, mySearch)

if output != -1:
    print(mySearch, 'is found in location', binary_search(oneList, lw, h, mySearch))
else:
    print(mySearch, 'is not found.')
