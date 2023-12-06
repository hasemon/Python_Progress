# 4. Write a Python program to print the even numbers from a given list.
alist = [10, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def evenNmList(lst):
    evenLst = []
    for nm in lst:
        if nm % 2 == 0:
            evenLst.append(nm)
    return evenLst


result = evenNmList(alist)

print('Even number list: ', result)
