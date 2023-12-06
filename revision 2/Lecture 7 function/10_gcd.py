a = int(input('Enter a number: '))
b = int(input('Enter another number: '))


def gcd(x, y):
    if x == y:
        return x
    elif x < y:
        return gcd(y, x)
    else:
        return gcd(y, x - y)


print(gcd(a, b))