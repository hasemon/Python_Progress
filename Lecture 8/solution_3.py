# 3. Write a Python program to remove the nth index character from a nonempty string.

def removeIndexNum(inputStr, indexNthNum):
    return inputStr[:indexNthNum] + inputStr[indexNthNum+1:]


print(removeIndexNum('Alphanumeric', 5))
