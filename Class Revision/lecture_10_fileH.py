f = open('info.txt', 'r')
content = f.read()
print(content)
f.close()

f = open('info.txt', 'a')
newStr = input('Enter a string: ')
f.write(newStr)
f.close()

print('After adding string')

f = open('info.txt', 'r')
content = f.read()
print(content)
f.close()