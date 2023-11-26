fName = input('Enter first name: ')
lName = input('Enter last name: ')
userId = input('Enter user ID: ')
password = input('Enter password: ')

if userId.isalpha():
    if password.isalnum() and len(password) > 6:
        print(fName + ' ' + lName, 'Congratulation')
    else:
        print('Invalid password')
else:
    print('Invalid user ID')