a = 30
b = 20
c = 10

def sumOftheNumbers(*numbers):
    sumOfNumber = 0
    for num in numbers:
        sumOfNumber += num
    return sumOfNumber

def averageOftheNumbers(*allNumbers):
    return sumOftheNumbers(*allNumbers) / len(allNumbers)


ava = averageOftheNumbers(a, b, c)
print(ava)