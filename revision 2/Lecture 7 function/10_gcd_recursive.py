# 10. Write a program in Python to find the GCD of two numbers using recursion.

def gcdFunc(a, b):
    if a == b:
        return a
    elif a < b:
        return gcdFunc(b, a)
    else:
        return gcdFunc(b, a - b)


num1 = int(input('Enter a number: '))
num2 = int(input('Enter b number: '))

result = gcdFunc(num1, num2)

print(f'The GCD of {num1} and {num2} is : {result}')
