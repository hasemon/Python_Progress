# write a program to read marks of n students and find their average mark.

N = int(input('Enter the number of students: '))

sumOfMarks = 0
i = 1
while i <= N:
    marks = int(input('Enter marks: '))
    sumOfMarks += marks
    i += 1

average = sumOfMarks / N
print(f'Their average is: {average} marks')
