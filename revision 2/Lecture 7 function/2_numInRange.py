# 2. Write a Python function to check whether a number falls within a given range.

def numInRange(minNum, givenNum, MaxNum):
    if minNum <= givenNum <= MaxNum:
        return f'{givenNum} is in the Range'
    else:
        return f'{givenNum} is Not in Range'


smallNum = int(input('Enter small number: '))
rangeNum = int(input('Enter search number: '))
bigNum = int(input('Enter Maximum number: '))

print(numInRange(smallNum, rangeNum, bigNum))

