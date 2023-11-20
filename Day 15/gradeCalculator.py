totalStudents = int(input('Total number of students: '))
allStudentsTotalMarks = []


def marksCalculator(attendMark, lbMark, midTMark, sfMark):
    totalMarks = attendMark + lbMark + midTMark + sfMark
    allStudentsTotalMarks.append(totalMarks)
    return totalMarks


def gradeCalculator(marks):
    if 80 <= marks <= 100:
        return 'A+'
    elif 70 <= marks < 80:
        return 'A'
    elif 60 <= marks < 70:
        return 'B'
    elif 50 <= marks < 60:
        return 'C'
    elif 40 <= marks < 50:
        return 'D'
    elif 40 <= marks < 0:
        return 'F'
    else:
        return 'Invalid Grade'


i = 1
while i <= totalStudents:
    while True:
        attendanceMarks = int(input(f'{i}th student\'s attendance marks out of 10: '))
        if 0 <= attendanceMarks <= 10:
            break
        else:
            print("Invalid input. Please enter a value between 0 and 10.")
    while True:
        labMarks = int(input(f'{i}th student\'s lab marks out of 20: '))
        if 0 <= labMarks <= 20:
            break
        else:
            print("Invalid input. Please enter a value between 0 and 20.")
    while True:
        midTermMarks = int(input(f'{i}th student\'s mid term marks out of 30: '))
        if 0 <= midTermMarks <= 30:
            break
        else:
            print("Invalid input. Please enter a value between 0 and 30.")
    while True:
        semesterFinalMarks = int(input(f'{i}th student\'s semester final marks out of 40: '))
        if 0 <= semesterFinalMarks <= 40:
            break
        else:
            print("Invalid input. Please enter a value between 0 and 40.")

    result = marksCalculator(attendanceMarks, labMarks, midTermMarks, semesterFinalMarks)
    grade = gradeCalculator(result)
    print(f'{i}th student grade: {grade} and Total = {result} marks')
    i += 1

maximumNum = max(allStudentsTotalMarks)
studentWhoGetMaximum = allStudentsTotalMarks.index(maximumNum)
print(f'Student No: {studentWhoGetMaximum + 1} got the maximum with {maximumNum} number.')
