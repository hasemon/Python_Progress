# A company decided to give bonus to employees based on the following conditions.
# a) 15% of salary if year of service is more than 10 years.
# b) 10% of salary if year of service is more than 5 years.
# c) 5% of salary otherwise.
# Ask user for their salary and year of service.

salary = int(input("Enter your salary: "))
yearOfService = int(input('Enter year of service: '))

if yearOfService > 10:
    bonus = salary * 15 / 100
elif yearOfService > 5:
    bonus = salary * 10 / 100
else:
    bonus = salary * 5 / 100

print(f'Salary with bonus is: {salary + bonus}')
