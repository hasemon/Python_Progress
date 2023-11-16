# 11. Write a Python program to calculate the value of 'a' to the power of 'b' using recursion.

# def power(a, b):
#     if b == 0:
#         return 1
#     else:
#         return a * power(a, b-1)


def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b-1)


baseNum = int(input("Enter base number: "))
powerNum = int(input("Enter power number: "))

result = power(baseNum, powerNum)
print('Result:', result)
