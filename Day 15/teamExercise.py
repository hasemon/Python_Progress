totalStudents = int(input('Total number of students: '))


def marksCalculator(attendMark, lbMark, midTMark, sfMark):
    totalMarks = attendMark + lbMark + midTMark + sfMark
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
    attendanceMarks = int(input(f'{i}th student\'s attendance marks out of 10: '))
    labMarks = int(input(f'{i}th student\'s lab marks out of 20: '))
    midTermMarks = int(input(f'{i}th student\'s mid term marks out of 30: '))
    semesterFinalMarks = int(input(f'{i}th student\'s semester final marks out of 40: '))
    result = marksCalculator(attendanceMarks, labMarks, midTermMarks, semesterFinalMarks)
    grade = gradeCalculator(result)
    print(f'{i}th student grade: {grade} and Total = {result} marks \n')
    i += 1
