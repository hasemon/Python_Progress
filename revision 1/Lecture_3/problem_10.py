# 10. A company decided to give bonus to employees based on the following conditions:
# i. 10% of salary if year of service is more than 5 years
# ii. 5% of salary if year of service is more than 3 years.
# • Ask user for their salary and year of service and print the total amount.

salary = int(input('Enter the salary: '))
yearOfSer = int(input('Enter the year of service: '))

if yearOfSer > 5:
    bonus = salary * 10 / 100
    salaryWithBonus = salary + bonus
    print('salary With Bonus', salaryWithBonus)
elif yearOfSer > 3:
    bonus = salary * 5 / 100
    salaryWithBonus = salary + bonus
    print('Salary with bonus is : ', salaryWithBonus)
else:
    print('You are not eligible for bonus')