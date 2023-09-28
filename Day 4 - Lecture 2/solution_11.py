# 11. Take input of age of 3 people by user and determine oldest and youngest among them.

personOne_age = int(input('Enter person one age: '))
personTwo_age = int(input('Enter person two age: '))
personThree_age = int(input('Enter person three age: '))

oldest = max(personOne_age, personTwo_age, personThree_age)
youngest = min(personOne_age, personTwo_age, personThree_age)

if oldest == personOne_age:
    print('Person one is the oldest, his age is', oldest)
elif oldest == personTwo_age:
    print('Person two is the oldest, his age is', oldest)
else:
    print('Person three is the oldest, his age is', oldest)

if youngest == personOne_age:
    print('Person one is youngest,  his age is', youngest)
elif youngest == personTwo_age:
    print('Person two is youngest,  his age is', youngest)
else:
    print('Person three is youngest, his age is', youngest)
