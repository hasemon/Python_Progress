# using if else condition with logical operators
a = -10
if a == 0:
    print('a is zero')
elif a > 0:
    print('a is positive number')
else:
    print('a is negative number')

# using "and" keyword -> "and" returns True if both conditions are true

gender = 'female'
age = 19

if gender == 'male' and age > 21:
    print('You can marry.')
elif gender == 'female' and age > 18:
    print('You can be married.')
else:
    print('Wait until your age is legal')

# using "or" keyword -> "or" returns True if only condition is true

age = 18
if age < 18 or age > 40:
    print('You can not attend the program.')
else:
    print('You can attend.')

# using nested if condition

gender = input('Enter your gender: ')
age = 20
if gender == 'male':
    if age >= 21:
        print('You can marry')
    else:
        print("You don't have the legal age")
elif gender == 'female':
    if age >= 18:
        print('You can get married.')
    else:
        print("You don't have the legal age")


