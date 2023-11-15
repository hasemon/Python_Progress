# GCD: Greatest common divisor

def gcd(a, b):
    if a == b:
        return a
    elif a < b:
        return gcd(b, a)
    elif a > b:
        return gcd(b, a - b)


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
output = gcd(num1, num2)
print(f'GCD of {num1} and {num2} is {output}')