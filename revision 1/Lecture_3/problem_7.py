# 7. Write a program to accept a coordinate point in a XY coordinate system and determine in which quadrant the
# coordinate point lies.

x = int(input('Enter the X coordinate: '))
y = int(input('Enter the Y coordinate: '))

if x > 0 and y > 0:
    print(' Point lies in first coordinate')
elif x < 0 and y > 0:
    print(' Point lies in second coordinate')
elif x < 0 and  y < 0:
    print(' Point lies in third coordinate')
else:
    print('Point lies  in fourth coordinate')
