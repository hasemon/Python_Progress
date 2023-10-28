fruits = ['Apple', 'Pineapple', 'Banana', 'Guava', 'Lichi', 'Banana', 'Mango', 'Apple', 'Banana', 'Orange']

search = input('Enter fruit name: ')
found = False
location = 0

for fruit in fruits:
    if fruit == search:
        found = True
        break
    else:
        location += 1
if found:
    print(search, 'is found at Index:', location)
else:
    print(search, 'is not found')