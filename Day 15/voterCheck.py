def voterCheck(age):
    if age >= 18:
        return 'Voter'
    else:
        return 'not a Voter'


a = int(input('Enter age: '))
print(f'You are a {voterCheck(a)}')
