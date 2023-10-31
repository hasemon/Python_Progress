# increment function

def increment(currentSalary):
    inc = currentSalary * 5 / 100
    print('Your next year increment is', inc)


cSalary = int(input('Enter your current salary: '))
increment(cSalary)


