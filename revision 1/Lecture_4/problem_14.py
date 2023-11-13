# 14. Write a program to display Fibonacci series up to 10 terms.

N = int(input('Enter a Number: '))
a = 0
b = 1
print(a)
print(b)
count = 3
print(count)
while count <= N:
    c = a + b
    print(c)
    a=b
    b=c
    count += 1