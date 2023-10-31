def marksSum(m1, m2, m3):
    total = m1 + m2 + m3
    return total


def average(m1, m2, m3):
    total = marksSum(m1, m2, m3)
    marksAverage = total / 3
    return marksAverage


marks1 = float(input("Enter first mark: "))
marks2 = float(input("Enter second mark: "))
marks3 = float(input("Enter third mark: "))

result = average(marks1, marks2, marks3)
print('Total average is', result)
