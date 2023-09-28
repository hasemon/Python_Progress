# 7. Write a program to accept a coordinate point in a XY coordinate system and
# determine in which quadrant the coordinate point lies.

x_coordinate = float(input('Enter X coordinate: '))
y_coordinate = float(input('Enter Y coordinate: '))

if x_coordinate > 0 and y_coordinate > 0:
    print('The 1st quadrant')
elif x_coordinate < 0 and y_coordinate > 0:
    print('The 2nd quadrant')
elif x_coordinate > 0 and y_coordinate < 0:
    print('The 3rd quadrant')
elif x_coordinate < 0 and y_coordinate < 0:
    print('The 4th quadrant')
elif x_coordinate == 0 and y_coordinate != 0:
    print('Quadrant lies on X coordinate')
elif y_coordinate == 0 and x_coordinate != 0:
    print('Quadrant lies on X coordinate')
else:
    print('Quadrant lies on the origin.')
