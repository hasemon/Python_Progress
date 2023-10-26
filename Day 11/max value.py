marks = [18, 19, 17, 16, 15, 20]

large = marks[0]

for item in marks:
    if item > large:
        large = item
print(large, 'is the largest')
