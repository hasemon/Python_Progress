
aString = "Hello World!"

choice = input('Enter your choice upper or lower: ')

if choice == 'upper':
    print(aString.upper())
elif choice == 'lower':
    print(aString.lower())
else:
    print('Invalid choice')