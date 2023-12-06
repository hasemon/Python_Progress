# 10. Write a program in Python to find the GCD of two numbers using recursion.

def gcdOfTwoNumbers(a, b):
    if a == b:
        return a
    elif a < b:
        return gcdOfTwoNumbers(b, a)
    elif a > b:
        return gcdOfTwoNumbers(b, a - b)


# another way

def nwGcdOfTwoNumbers(a, b):
    if a == b:
        return a
    elif a < b:
        return nwGcdOfTwoNumbers(b, a)
    else:
        return nwGcdOfTwoNumbers(b, b % a)


num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
result = gcdOfTwoNumbers(num1, num2)
print(f'GCD of {num1} and {num2} is: {result}')

print(nwGcdOfTwoNumbers(num1, num2))
