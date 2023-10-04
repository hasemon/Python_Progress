print('if elif else - Exercise')
# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs


firstNumber = int(input('Enter the first number: '))
operation = input('Enter the operation: ')
secondNumber = int(input('Enter the second number: '))

result = 0
if operation == '+':
    result = firstNumber + secondNumber
elif operation == '-':
    result = firstNumber - secondNumber
elif operation == '*':
    result = firstNumber * secondNumber
elif operation == '/':
    result = firstNumber / secondNumber
else:
    print('invalid operation')

print('Result is: ', result)
