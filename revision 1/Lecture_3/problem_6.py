# 6. write a program using python to create a simple calculator

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

operation = input("Enter operation: ")

result = 0
if operation == '+':
    result = num1 + num2
    print("Sum is ", result)
elif operation == '-':
    result = num1 - num2
    print("Sub is ", result)
elif operation == '*':
    result = num1 * num2
    print("Mul is ", result)
elif operation == "/":
    result = num1 // num2
    print("Div is ", result)
elif operation == "%":
    result = num1 % num2
    print("Modules is", result)
else:
    print("Enter correct operation")

