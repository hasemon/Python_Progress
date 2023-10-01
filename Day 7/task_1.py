# take input employee iD , work hour and salary per hour then output total salary with their id.

emoployeID = int(input("Enter ID: "))
workHour = int(input("Enter working hour: "))
salaryPerHour = int(input("Enter salary per hour: "))

totalSalary = workHour * salaryPerHour

print(f'ID- {emoployeID}, Salary- {totalSalary}')
