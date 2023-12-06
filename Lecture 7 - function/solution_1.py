# 1. Write a Python function to find the max of three numbers.

def max_num(first, second, third):
    if first > second and first > third:
        max_number = first
    elif second > first and second > third:
        max_number = second
    else:
        max_number = third
    return max_number


# another way with build in method


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

maximum_number = max_num(num1, num2, num3)


def max_num_method(first, second, third):
    max_number = max(first, second, third)
    return max_number


maximum_number_method = max_num_method(num1, num2, num3)

print(f'The maximum of {num1} , {num2} and {num3} is: {maximum_number}')
print(f'The maximum of {num1} , {num2} and {num3} with method is: {maximum_number_method}')
