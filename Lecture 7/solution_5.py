# 5. Write a program to find area of surface based on a selection
# function define
def areaOfCircle(radius):
    area = 3.1416 * (radius ** 2)
    return area


def areaOfSquare(length):
    area = length ** 2
    return area


def areaOfRectangle(length, width):
    area = length * width
    return area


# function call

choice = int(input("Enter 1 circle or 2 square or 3 rectangle: "))

if choice == 1:
    r = float(input("Enter the radius: "))
    output = areaOfCircle(r)
    print('Area of circle is: ', output)
elif choice == 2:
    a = float(input("Enter the area: "))
    output = areaOfSquare(a)
    print('Area of square is: ', output)
elif choice == 3:
    lg = float(input("Enter the length: "))
    w = float(input("Enter the width: "))
    output = areaOfRectangle(lg, w)
    print('Area of rectangle is: ', output)
else:
    print('Enter valid choice')
