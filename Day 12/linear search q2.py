fruits = ['Apple', 'Pineapple', 'Banana', 'Guava', 'Lichi', 'Banana', 'Mango', 'Apple', 'Banana', 'Orange']

search = input('Enter fruit name: ')
found = False
count = 0

for fruit in fruits:
    if fruit == search:
        found = True
        count += 1
if found:
    print(search, 'is found', count, 'times')
else:
    print('There is no such fruit in the list')
