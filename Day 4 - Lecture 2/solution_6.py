# 6. write a program using python to create a simple calculator.

print('Calculator started')

first_number = int(input('Enter first number: '))
operation = input('Sum / Subtraction / Multiplication / Division / Modulus : ')
second_number = int(input('Enter second number: '))

if operation == 'sum' or operation == '+':
    print('Sum is: ', first_number + second_number)
elif operation == 'subtraction' or operation == 'sub' or operation == '-':
    print('Subtraction is: ', first_number - second_number)
elif operation == 'multiplication' or operation == 'mul' or operation == '*':
    print('Multiplication is: ', first_number * second_number)
elif operation == 'division' or operation == 'div' or operation == '/':
    print('Division is: ', first_number / second_number)
elif operation == 'modulus' or operation == 'mod' or operation == '%':
    print('Modulus is: ', first_number % second_number)
else:
    print('Enter correct Operation.')
