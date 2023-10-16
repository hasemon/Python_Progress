# 3. Create a list of marks of ten students.

markOfStudents = []
for student in range(10):
    mark = int(input(f"Enter {student + 1} th student mark: "))
    markOfStudents.append(mark)

print('Marks of 10 students are: ', markOfStudents)
