# 6. Write two Python function as sum() & average() to find the average of three numbers.

def sumOfThree(*allNumber):
    sumOfNumbers = 0
    for num in allNumber:
        sumOfNumbers += num
    return sumOfNumbers


def average(*numbers):
    myAverage = sumOfThree(*numbers) / len(numbers)
    return myAverage


num1 = int(input('Enter number one: '))
num2 = int(input('Enter number two: '))
num3 = int(input('Enter number three: '))
numbersAvg = average(num1, num2, num3)
print(numbersAvg)
