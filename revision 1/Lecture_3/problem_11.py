# 11. Take input of age of 3 people by user and determine oldest and youngest among them.

firstP = int(input('Enter first person age: '))
secondP = int(input('Enter second person age: '))
thirdP = int(input('Enter third person age: '))

if firstP > secondP and firstP > thirdP:
    print('The first person is the oldest')
elif secondP > firstP and secondP > thirdP:
    print('The second person is the oldest')
else:
    print('The third person is the oldest')

if firstP < secondP and firstP < thirdP:
    print('The first person is the youngest')
elif secondP < firstP and secondP < thirdP:
    print('The second person is the youngest')
else:
    print('The third person is the youngest')
