marks = [3, 4, 6, 7, 9, 5, 7]
totalMarks = 0

for mark in marks:
    totalMarks += mark

print('Total marks: ', totalMarks)
averageMarks = totalMarks // len(marks)

print('Average marks: ', averageMarks)
