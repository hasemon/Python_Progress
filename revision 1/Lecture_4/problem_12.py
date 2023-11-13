# 12. Write a program to print the reverse of a number.

N = int(input('Enter a number: '))
originalNum = N

i = 0
reversedNum = 0
while i < N:
    last_digit = N % 10
    reversedNum = reversedNum * 10 + last_digit
    N //= 10

print(reversedNum)