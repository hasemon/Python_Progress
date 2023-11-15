def factorial(n):
    if n > 0:
        return n * factorial(n-1)
    else:
        return 1


number = int(input("find the factorial: "))
output = factorial(number)
print('factorial of is:', output)