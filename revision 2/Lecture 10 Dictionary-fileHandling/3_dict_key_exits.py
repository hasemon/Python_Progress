# 3. Write a Python program to check whether a given key already exists in a dictionary.

carNDealer = {'Brand': 'Ford', 'Model': 'Mustang', 'Year': 1964, 'Dhaka': 'Hasan', 'Sylhet': 'Karim', 'Cumilla':
    'Rahima'}

searchKey = input('Enter a key: ').lower().capitalize()

if searchKey in carNDealer:
    print(searchKey, 'is found')
else:
    print(searchKey, 'not found')
