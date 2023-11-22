userName = input('Enter your name: ')
userPass = input('Enter your password: ')

# one way
# if len(userPass) >= 8:
#     if userPass.isalpha():
#         print('Valid password for', userName)
#     elif userPass.isalnum():
#         print('Valid password for', userName)
#     elif userPass.isdigit():
#         print('Valid password for', userName)
#     else:
#         print('Invalid Password')
# else:
#     print('Invalid Password')

# other way

if len(userPass) >= 8 and userPass.isalnum():
    print('Valid password for', userName)
else:
    print('Not valid  password!')
