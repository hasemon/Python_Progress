import os

# file read
print('Before entering new data: ')
f = open('data.txt', 'r')
content = f.read()
print(content)
f.close()

# file write with overwrite
f = open('data.txt', 'w')
myStr = input('Enter text to Add: ')
f.write(myStr)
f.close()

# file write without overwriting
f = open('data.txt', 'a')
newStr = '\n' + myStr
f.write(newStr)
f.close()

# file read after write
print('After entering new data: ')
f = open('data.txt', 'r')
content = f.read()
print(content)
f.close()

# Delete a file
# os.remove('data.txt')
