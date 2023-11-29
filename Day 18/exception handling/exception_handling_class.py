import os

# over writing in a file or creating
f = open('demo.txt', 'w')
f.write('Bangladesh is my motherland.')
f.close()

# appending in a file
f = open('demo.txt', 'a')
f.write(' I love my country.')
f.close()

# open a file read only
f = open('demo.txt', 'r')
content = f.read()
print(content)
f.close()

# file delete
try:
    os.remove('demo.txt')
except FileNotFoundError:
    print('File does not exits. Create the file first.')





