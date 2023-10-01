# 5. Write a program to calculate the factorial of a given number.

number = int(input("Enter a number: "))

factorial = 1
i = 1
while i <= number:
    factorial = factorial * i
    i += 1
print(f'The factorial of {number} number is {factorial}')
