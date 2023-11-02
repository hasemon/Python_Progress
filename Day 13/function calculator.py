def add(num1, num2):
    result = num1 + num2
    return result


def sub(num1, num2):
    result = num1 - num2
    return result


def mul(num1, num2):
    result = num1 * num2
    return result


def div(num1, num2):
    result = num1 / num2
    return result


# function call

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
operation = input('Enter +,-,*,/ operation: ')

if operation == '+':
    print('Addition is', add(number1, number2))
elif operation == '-':
    print('Subtraction is', sub(number1, number2))
elif operation == '*':
    print('Multiplication is', mul(number1, number2))
elif operation == '/':
    print('Division is', div(number1, number2))
else:
    print('Enter a valid operation.')
