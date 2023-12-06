# 5. Write a program to find area of surface based on a selection.

def aOfSqr(x):
    result = x ** 2
    return result


def aOfCircle(r):
    pi = 3.1416
    result = pi * (r ** 2)
    return result


def aOfRec(x, y):
    result = x * y
    return result


def aOfTriangle(b, h):
    result = 0.5 * (b * h)
    return result


surface = input('Enter base to get Area: ')
if surface == 'circle':
    radius = int(input('Enter the radius of circle: '))
    print('Area of Circle is: ', aOfCircle(radius))
elif surface == 'rectangle':
    length = int(input('Enter length: '))
    width = int(input('Enter width: '))
    print('Area of Rectangle is: ', aOfRec(length, width))
elif surface == 'square':
    length = int(input('Enter length: '))
    print('Area of Square: ', aOfSqr(length))
elif surface == 'triangle':
    base = int(input('Enter base: '))
    height = int(input('Enter height: '))
    print('Area of Triangle: ', aOfTriangle(base, height))
else:
    print('Enter correct surface name.')