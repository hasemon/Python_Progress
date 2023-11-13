# 12. A student will not be allowed to sit in exam if his/her attendance is less than 70%.
# Take following input from user & print percentage of class attended.
# Is student is allowed to sit in exam or not?
# • Number of classes held
# • Number of classes attended

totalClass = int(input('Total  class: '))
attendedClass = int(input('Attended class: '))

percentOfClass = (attendedClass / totalClass) * 100

if percentOfClass > 70:
    print('Allowed to sit in the exam.')
else:
    print('Attendance is low, Not allowed to sit in the exam.')


