# 6. Write two Python function as sum() & average() to find the average of three numbers.

# Defining Functions

def sumOfThreeNumbers(a, b, c):
    sumResult = a + b + c
    return sumResult


def averageOfThreeNumbers(a, b, c):
    averageResult = sumOfThreeNumbers(a, b, c) / 3
    return averageResult


# Calling functions

num1 = int(input("Enter 1st Number: "))
num2 = int(input("Enter 2nd Number: "))
num3 = int(input("Enter 3rd Number: "))

sumOfThreeNumbers(num1, num2, num3)

averaging = averageOfThreeNumbers(num1, num2, num3)

print('The average of three numbers is: ', averaging)
