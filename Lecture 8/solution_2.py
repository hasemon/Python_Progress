# 2. Write a Python program to get a string made of the first 2 and last 2
# characters of a given string. If the string length is less than 2, return the empty string instead.

def nwStr(oStr):
    if len(oStr) < 2:
        return ""
    else:
        return oStr[:2] + oStr[-2:]


print(nwStr('A'))
