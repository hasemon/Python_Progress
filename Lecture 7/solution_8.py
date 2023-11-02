# 8. Write a Python function to calculate the factorial of a number using recursive function.

# example of a recursive function

def count_down(n):
    print(n)
    if n > 1:
        n -= 1
        count_down(n)


# funtion call
number = int(input('Enter the number to count: '))
count_down(number)


# normal way of printing factorial
def factorial(n):
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1
    return result


print('factorial is:', factorial(5))

# recursive way of printing factorial
