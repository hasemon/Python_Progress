print('python101 - Enumerate')
friends = ['Brian', 'Judith', 'Reg', 'Loretta', 'Colin']

for num, friend in enumerate(friends, 1):
    print(num, friend)

print(type(friends))
print(type(enumerate(friends)))
