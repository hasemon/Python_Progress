fruits = ['Apple', 'Pineapple', 'Banana', 'Guava', 'Lichi', 'Banana', 'Mango', 'Apple', 'Banana', 'Orange']

searchItem = input('Search item: ')
found = False
count = 0
for i in fruits:
    if i == searchItem:
        found = True
        count += 1

if found:
    print('The search item is found', count)
else:
    print('Search item is not found')
