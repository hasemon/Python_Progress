# 6. Write a Python program to append text to a file and display the text.
f = open('lecture_10_problems', 'a+')
addText = input('Add a line: ')
f.write('\n' + addText)
f.close()


