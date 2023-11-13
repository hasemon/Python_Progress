# 2. Write a Python program to search your roll from a list of class rolls.

roll = [10, 12, 13, 14, 15, 16]

searchRoll = int(input('Enter roll: '))
loc = 0
found = False

for i in roll:
    if i == searchRoll:
        found = True
        break
    else:
        loc += 1

if found:
    print("Roll is found on location: ", loc + 1)
else:
    print('Roll is not found')