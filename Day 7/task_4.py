# write a program to convert specified days into years, months and days.

days = int(input('Enter the number of days: '))

years = days // 365
remainingDays = days % 365
months = remainingDays // 30
dueDays = remainingDays % 30

print(f'{years} year {months} month {dueDays} days.')

