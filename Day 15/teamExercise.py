totalStudents = int(input('Total number of students: '))


def marksCalculator(a, lb, m, s):
    totalMarks = a + lb + m + s
    return totalMarks


def gradeCalculator(marks):
    if marks > 80:
        return 'A+'
    elif marks > 70:
        return 'A'
    elif marks > 60:
        return 'B'
    elif marks > 50:
        return 'C'
    elif marks > 40:
        return 'D'
    else:
        return 'F'


i = 1
while i <= totalStudents:
    attendanceMarks = int(input(f'{i}th student\'s attendance marks out of 10: '))
    labMarks = int(input(f'{i}th student\'s lab marks out of 20: '))
    midTermMarks = int(input(f'{i}th student\'s mid term marks out of 30: '))
    semesterFinalMarks = int(input(f'{i}th student\'s semester final marks out of 40: '))
    result = marksCalculator(attendanceMarks, labMarks, midTermMarks, semesterFinalMarks)
    grade = gradeCalculator(result)
    print(f'Grade of {i}th student is: {grade} with Total = {result} marks')
    i += 1
