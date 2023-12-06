# 8. Write a Python function to calculate the factorial of a number using recursive function.

def factorial(number):
    if number == 1:
        return 1
    else:
        number = number * factorial(number - 1)
        return number


print('Factorial number is: ', factorial(5))
