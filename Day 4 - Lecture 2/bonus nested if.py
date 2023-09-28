age = int(input("Enter your age: "))
gender = input('Enter your gender: ')

if gender == 'male':
    if age >= 21:
        print('You can marry.')
    else:
        print('Sorry!')
elif gender == 'female':
    if age >= 18:
        print('You can marry.')
    else:
        print('Sorry!')
else:
    print('Not eligible')
