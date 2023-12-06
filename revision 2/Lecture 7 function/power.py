a = int(input('Enter base number: '))
b = int(input('Enter power number: '))

def power(base, pwer):
    if pwer == 0:
        return 1
    else:
        return base * power(base, pwer - 1)


print(power(a, b))