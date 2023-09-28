# 10. A company decided to give bonus to employees based on the following conditions:
# i. 10% of salary if year of service is more than 5 years
# ii. 5% of salary if year of service is more than 3 years.
# • Ask user for their salary and year of service and print the total amount.

salary = int(input('Enter your salary: '))
year_of_service = int(input('Enter your year of service: '))

if year_of_service > 5:
    bonus = salary * 0.1
    print(f'Your bonus is: {bonus}')
    print(f'Your salary with bonus is: {salary + bonus}')
elif year_of_service > 3:
    bonus = salary * 0.05
    print(f'Your bonus is: {bonus}')
    print(f'Your salary with bonus is: {salary + bonus}')
else:
    print('Service year is not enough to receive bonus.')
