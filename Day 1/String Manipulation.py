#String slicing and making a new string from another string
msg = 'welcome to Python 101: Strings'
newMsg = msg[18] + " " + msg[:8] + msg[25:-1] + msg[7:11] + msg[8] + msg[12] + msg[2] + msg[1] + msg[-5]

#Using title string method and reversing a string with slice method
print(newMsg.title())
print(newMsg[::-1].title())

print('')
#Multiline string with triple quotes
mulMsg = """Dear Terry,,
You must cut down the mightiest 
tree in the forest with…
a herring! <3"""
print(mulMsg)

print('')
#Find and replace methods
print(msg.find('Python'))
javaScript_Version = msg.replace('Python', 'JavaScript')
print(javaScript_Version)
print('JavaScript' in msg)
print('JavaScript' not in msg)
print('')


#String formating
name= 'Ant-Dev'
age = 26

print(f'My name is {name} and i am {age}')