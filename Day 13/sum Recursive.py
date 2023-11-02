def sumOfRange(n):
    if n >= 0:
        return n + sumOfRange(n - 1)
    else:
        return 0


N = int(input("Enter the  value of  N: "))
print('Sum of Range: ', sumOfRange(N))
