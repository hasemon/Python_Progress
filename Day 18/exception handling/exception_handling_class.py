import os

try:
    f = open('demo.txt', 'r')
    content = f.read()
    print(content)
    f.close()
except:
    print('Create the file first.')

f = open('demo.txt', 'a')
f.write('I live in Bangladesh')
print(content)
f.close()

file = 'demo.txt'
os.remove('demo.txt')

try:
    os.remove('demo.txt')
except:
    print(file, 'does not exits')
