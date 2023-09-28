# 3. Write a program to read the age of a candidate and determine whether s/he is eligible for casting vote.

print('Check if you are eligible to vote.')

age = int(input('Enter your age: '))

if age >= 18:
    print('Congratulations! You are eligible to vote.')
else:
    print('Sorry! You are not eligible to vote.')
