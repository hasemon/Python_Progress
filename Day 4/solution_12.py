# 12. A student will not be allowed to sit in exam if his/her attendance is less than 70%.
# Take following input from user & print percentage of class attended.
# Is student is allowed to sit in exam or not?
# • Number of classes held
# • Number of classes attended.

total_classes_held = int(input('Total classes held: '))
classes_attended = int(input('Total classes attended: '))

percentage_of_attendance = (classes_attended * 100) / total_classes_held

if percentage_of_attendance < 70:
    print(f'Your attendance is : {int(percentage_of_attendance)} percent')
    print('Attendance is low!, You are not allowed to sit in exam.')
else:
    print('You are allowed to sit in the exam.')
