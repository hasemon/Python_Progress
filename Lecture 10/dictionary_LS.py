# file open
f = open("C:\Ant-Dev\RoadToPython\Python_Progress\Lecture 10\File handling\demo.txt", 'r')
print(f.read())
f.close()

# file write append
fw = open("C:\Ant-Dev\RoadToPython\Python_Progress\Lecture 10\File handling\demoWrite.txt", 'a')
fw.write("Now the file has one more line.")
fw.close()

# file overwrite
fwo = open("C:\Ant-Dev\RoadToPython\Python_Progress\Lecture 10\File handling\demoOverWrite.txt", 'w')
fwo.write("Now the file has overwritten")
fwo.close()

fwo = open("C:\Ant-Dev\RoadToPython\Python_Progress\Lecture 10\File handling\demoOverWrite.txt", 'r')
print(fwo.read())
