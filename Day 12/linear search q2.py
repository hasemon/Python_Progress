fruits = ['Apple', 'Pineapple', 'Banana', 'Guava', 'Lichi', 'Banana', 'Mango', 'Apple', 'Banana', 'Orange']

search_fruit = input('Enter fruit name: ')
found = False
count = 0

for fruit in fruits:
    if fruit == search_fruit:
        found = True
        count += 1
if found:
    print(search_fruit, 'is found', count, 'times')
else:
    print('There is no such fruit in the list')
