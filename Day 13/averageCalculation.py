mark1 = int(input("Enter mark one: "))
mark2 = int(input("Enter mark two: "))
mark3 = int(input("Enter mark three: "))


def average(m1, m2, m3):
    markSum = m1 + m2 + m3
    markAverage = markSum / 3
    return markAverage


marks = average(mark1, mark2, mark3)
print('Average marks is: ', marks)