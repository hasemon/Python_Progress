def power(x, y):
    if y == 0:
        return 1
    else:
        return x * power(x, y - 1)


a = int(input("Enter main number: "))
b = int(input("Enter power number: "))
output = power(a, b)
print(a, 'power', b, 'is:', output)
