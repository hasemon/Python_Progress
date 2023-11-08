# Write a program in that takes minutes as input, and display the total number of hours and minutes.

minutes = int(input('Enter total minutes: '))

hours = minutes // 60
remainderMinutes = minutes % 60
print('Total is ', hours, 'hours and', remainderMinutes, 'minutes')
