# 2. Write a Python function to check whether a number falls within a given range.

range1 = int(input("Enter first number of the range: "))
range2 = int(input("Enter second number of the range: "))
number = int(input("Enter the number: "))


def find_range(input_number, starting, ending):
    return input_number in range(starting, ending + 1)


result = find_range(number, range1, range2)
if result:
    print(f'{number} is in the RANGE of {range1} and {range2}')
else:
    print(f'{number} is not in the RANGE of {range1} and {range2}')
