# 3. Write a Python program to check whether a given key already exists in a dictionary.

python = {'John': 35, 'Eric': 36, 'Michael': 35, 'Terry': 38, 'Graham': 37, 'TerryG': 34}
name = input('What is your name? : ').lower().capitalize()

if name in python:
    print(name, 'is found')
else:
    print('Not found', name)
