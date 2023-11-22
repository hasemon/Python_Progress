str1 = 'Hello'
str2 = 'Bangladesh'

s = str1 + ' ' + str2 + ' '

# concatenation
print(s)
print(s * 5)

# membership
print('x' in s)
print('x' not in s)

# slice
print(str2[:-4])
print(str2[6:])

# string methods

print(s.lower())
print(s.upper())
print(s.capitalize())
print(s.isalpha())
print(str2.isalpha())
print(s.isdigit())
print(s.isalnum())
print(s.isdigit())

me = 'I am from Dhaka Bangladesh.'
lenMe = len(me)
print(lenMe)
search = input('Enter search value: ')
output = me.find(search)

if output == -1:
    print(search, ' not found')
else:
    print(search, 'found in location: ', output)



