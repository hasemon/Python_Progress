district = ['Mymensingh', 'Coxbazar', 'Gaibandha', 'Munsigong', 'Chattagram', 'Mymensingh', 'Sherpur', 'Noakhali',
            'Mymensingh']

search = input('Enter the location: ')
found = False
count = 0

for item in district:
    if item == search:
        found = True
        count += 1
if found:
    print(f'There are {count} student from {search}')
else:
    print(f'There are no students from {search}')
