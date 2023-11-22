myStr = input('Enter the string: ')
myStyle = int(input('1 for Uppercase, 2 for lowercase, 3  for capitalize: '))


if myStyle == 1:
    print(myStr.upper())
elif myStyle == 2:
    print(myStr.lower())
elif myStyle == 3:
    print(myStr.capitalize())
else:
    print('Invalid selection.')