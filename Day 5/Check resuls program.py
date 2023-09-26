marks_Bangla = int(input('Enter Bangla marks: '))
marks_English = int(input('Enter English marks: '))
marks_Mathematics = int(input('Enter Mathematics marks: '))

count = 0
if marks_Bangla >= 33:
    count += 1
    print('you are passed in bangla')
else:
    print('you are failed in bangla')
if marks_English >= 33:
    count += 1
    print('you are passed in english')
else:
    print('you are failed in english')
if marks_Mathematics >= 33:
    count += 1
    print('you are passed in mathematics')
else:
    print('You are failed in math')

if count > 0 :
    print(f'You are passed in {count} subjects')
else:
    print('You are failed in all subjects')
