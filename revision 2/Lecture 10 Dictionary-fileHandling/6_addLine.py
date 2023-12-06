# 6. Write a Python program to append text to a file and display the text.
# Added a line for solution 6

f = open('dummyFile', 'a')
f.write('\nThis is no 5 line added')
f.close()


f = open('dummyFile', 'r')
content = f.read()
print(content)
f.close()